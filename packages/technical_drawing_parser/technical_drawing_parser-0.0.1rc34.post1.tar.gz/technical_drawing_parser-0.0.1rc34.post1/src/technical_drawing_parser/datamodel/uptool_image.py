"""This module contains the UptoolImage class which is used to process the image and extract the blocks from it."""

import base64

from dataclasses import dataclass, field
from typing import Tuple, List, Dict, Deque, Optional
from collections import deque
import cv2
import pytesseract
from PIL import Image
import numpy as np
from rtree import index

from technical_drawing_parser.datamodel.image_block import ImageBlock

color_palatte = {
    0: (255, 0, 0),  # Red
    1: (0, 255, 0),  # Green
    2: (0, 0, 255),  # Blue
    3: (255, 255, 0),  # Yellow
    4: (255, 165, 0),  # Orange
    5: (128, 0, 128),  # Purple
    6: (0, 255, 255),  # Cyan
    7: (255, 192, 203),  # Pink
    8: (165, 42, 42),  # Brown
    9: (0, 128, 128),  # Teal
    10: (128, 128, 0),  # Olive
    11: (75, 0, 130),  # Indigo
    12: (173, 216, 230),  # Light Blue
    13: (255, 20, 147),  # Deep Pink
    14: (46, 139, 87),  # Sea Green
    15: (139, 69, 19),  # Saddle Brown
    16: (210, 105, 30),  # Chocolate
    17: (105, 105, 105),  # Dim Gray
    18: (192, 192, 192),  # Silver
    19: (240, 230, 140),  # Khaki
}


@dataclass
class UptoolImage:
    """Class for the UptoolImage, which is to process the image and extract the blocks from it"""

    page_num: int = field(default=0)
    image: Optional[Image.Image] = field(default=None)
    debug: bool = field(default=False)
    file_name: str = field(default="")
    dst_path: str = field(default="")

    opencv_image: np.ndarray = field(init=False)
    binary: np.ndarray = field(init=False)
    page_height: int = field(init=False)
    page_width: int = field(init=False)
    image_blocks: List[ImageBlock] = field(init=False)
    clusters: Dict[int, List[np.ndarray]] = field(init=False)

    def __post_init__(self):
        self.opencv_image: np.ndarray = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
        self.binary: np.ndarray = self.build_binary(self.opencv_image)
        self.page_height, self.page_width = self.binary.shape
        self.image_blocks: List[ImageBlock] = []
        avg_char_width, avg_char_height = self.get_avg_character_size(self.binary)
        if np.all(self.binary == 0):
            return
        self.ctx_base64_string = self.get_base64_string(self.binary)
        valid_contours = self.find_contours(self.binary)
        self.clusters = self.clustering_by_neighbor(valid_contours, (avg_char_width + avg_char_height) // 2)

        if self.debug:
            for key, value in self.clusters.items():
                cv2.drawContours(self.opencv_image, value, -1, color_palatte[key % 20], 2)
            cv2.imwrite(f"{self.dst_path}/{self.file_name}_{self.page_num}.png", self.opencv_image)

        # export image blocks
        for _, value in self.clusters.items():
            x, y, w, h, cluster_img = self.stencil(value)
            base64_string = self.get_base64_string(cluster_img)
            self.image_blocks.append(ImageBlock(x, y, w, h, base64_string))

    def build_binary(self, img: np.ndarray) -> np.ndarray:
        """Convert the image to binary image"""
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        mask = gray == 255
        # mask = (gray > 200)
        gray[~mask] = 0
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        sharp_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        binary = cv2.filter2D(binary, -1, sharp_kernel)
        return binary

    # def close_morph(self, img: np.ndarray, avg_w: int, avg_h: int) -> np.ndarray:
    #     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (avg_w, avg_h))
    #     img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    #     return img

    def find_contours(self, img: np.ndarray) -> List[np.ndarray]:
        """This function recursively examines the hierarchy tree of contours and return valid ones."""
        contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) == 1:
            return list(contours)
        valid_contours: List[np.ndarray] = []
        # append first level contours
        parent_map: Dict[int, List[int]] = {}
        for i in range(0, len(contours)):
            parent = hierarchy[0][i][3]
            if parent not in parent_map:
                parent_map[parent] = []
            parent_map[parent].append(i)

        q: Deque[int] = deque()
        for key in parent_map[-1]:
            q.append(key)
        while len(q) != 0:
            key = q.pop()
            cnt = contours[key]
            _, _, w, h = cv2.boundingRect(cnt)
            if w * h < self.page_height * self.page_width * 0.25:
                valid_contours.append(cnt)
                continue
            if key in parent_map:
                q.extend(parent_map[key])
        return valid_contours

    def fill_pixels_outside_border(self, img: np.ndarray, contours: List[np.ndarray]):
        """Fill the pixels outside of the border with black color"""
        mask = np.zeros_like(img)
        cv2.drawContours(mask, contours, -1, 255, cv2.FILLED)
        img = cv2.bitwise_and(img, img, mask=mask)
        return img

    def fill_pixels_inside_border(self, img: np.ndarray, contours: List[np.ndarray]):
        """Fill the pixels inside of the border with black color"""
        mask: np.ndarray = np.ones_like(img) * 255
        cv2.drawContours(mask, contours, -1, 0, cv2.FILLED)
        img = cv2.bitwise_and(img, img, mask=mask)
        return img

    def is_valid_contour(self, contour: np.ndarray) -> bool:
        """filter out contours based on its geometrical characteristic"""
        _, _, w, h = cv2.boundingRect(contour)
        return cv2.contourArea(contour) < 0.5 * w * h

    def clustering_by_neighbor(self, contours: List[np.ndarray], margin: int) -> Dict[int, List]:
        """clustering contours by their neighborhood"""
        clusters: dict[int, List] = {}
        cluster_index: int = 0
        for cnt in contours:
            nearest_intersection: bool = False
            nearest_key = 0
            nearest_dist_sq = self.page_height * self.page_width
            intersection_keys: List[int] = []
            for key, value in clusters.items():
                found_intersection, dist_sq = self.is_intersected(cnt, value, margin)
                if found_intersection:
                    intersection_keys.append(key)
                if dist_sq < nearest_dist_sq:
                    nearest_dist_sq = dist_sq
                    nearest_key = key
                    nearest_intersection = found_intersection
            if nearest_intersection:
                clusters[nearest_key].append(cnt)
                if len(intersection_keys) > 1:
                    for i in range(1, len(intersection_keys)):
                        clusters[intersection_keys[0]].extend(clusters[intersection_keys[i]])
                        clusters.pop(intersection_keys[i], None)
            else:
                clusters[cluster_index] = [cnt]
                cluster_index += 1
        return clusters

    # def clustering_by_density(self, contours: List[np.ndarray]) -> Dict[int, List]:
    #     """USe DBSCAN to cluster contours"""
    #     clusters: dict[int, List] = {}
    #     centroids = [self._get_bbox_center(cnt) for cnt in contours]
    #     centroids_array = np.array(centroids)

    #     # Apply DBSCAN
    #     db = DBSCAN(eps=(self.page_height + self.page_width) // 128, min_samples=1, metric="euclidean")
    #     db_labels = db.fit_predict(centroids_array)

    #     for contour, label in zip(contours, db_labels):
    #         if label in clusters:
    #             clusters[label].append(contour)
    #         else:
    #             clusters[label] = [contour]
    #     return clusters

    def is_intersected(self, contour: np.ndarray, group: List[np.ndarray], margin: int) -> Tuple[bool, float]:
        """Test if a contour is intersected with the contour bbox inside the group and return nearest distance"""
        rtree_index = index.Index()
        for i, cnt in enumerate(group):
            x, y, w, h = cv2.boundingRect(cnt)
            rtree_index.insert(i, (x, y, w + x, h + y))
        x, y, w, h = cv2.boundingRect(contour)
        hits = list(rtree_index.intersection((x - margin, y - margin, x + w + margin, y + h + margin)))
        squared_distance = self.page_height * self.page_width
        # if the connected contour is too far away from the center of the group, return false
        x_g, y_g, w_g, h_g = cv2.boundingRect(np.vstack(group))
        dist = ((x + w // 2) - (x_g + w_g // 2)) * ((x + w // 2) - (x_g + w_g // 2)) + (
            (y + h // 2) - (y_g + h_g // 2)
        ) * ((y + h // 2) - (y_g + h_g // 2))
        if dist > ((self.page_height + self.page_width) // 8) * ((self.page_height + self.page_width) // 8):
            return (False, squared_distance)

        if len(hits) > 0:
            squared_distance = self._get_nearest_dist_sq(rtree_index, (x, y, w, h), margin)
            return (True, squared_distance)
        return (False, squared_distance)

    def _get_nearest_dist_sq(
        self, rtree_index: index.Index, coordinate: Tuple[int, int, int, int], margin: int
    ) -> float:
        x0, y0, w0, h0 = coordinate
        nearest_obj = next(
            rtree_index.nearest((x0 - margin, y0 - margin, x0 + w0 + margin, y0 + h0 + margin), 1, objects=True)
        )
        box1 = np.array([x0, y0, x0 + w0, y0 + h0])
        box2 = np.array(nearest_obj.bbox)
        center1 = (box1[::2] + box1[1::2]) / 2
        center2 = (box2[::2] + box2[1::2]) / 2
        squared_distance = np.sum((center1 - center2) ** 2)
        return squared_distance

    def _get_bbox_center(self, contour: np.ndarray) -> Tuple[int, int]:
        x, y, w, h = cv2.boundingRect(contour)
        return (x + w // 2, y + h // w)

    # def _is_rectangle(self, contour: np.ndarray):
    #     """Check if a given contour is a rectangle."""
    #     # Approximate the contour
    #     x, y, w, h = cv2.boundingRect(contour)
    #     if (
    #         self.binary[y, x] != 0
    #         and self.binary[y + h - 1, x] != 0
    #         and self.binary[y, x + w - 1] != 0
    #         and self.binary[y + h, x + w] != 0
    #     ):
    #         return True

    # if cv2.contourArea(contour) > w * h * 0.95:
    #     return True

    # return False

    # peri = cv2.arcLength(contour, True)  # Compute perimeter
    # area = cv2.contourArea(contour)
    # area_bbox = w * h
    # return (np.abs(peri - 2 * (w + h)) / (2 * (w + h))) < 0.1 and area > area_bbox * 0.9

    # hull = cv2.convexHull(contour)
    # peri = cv2.arcLength(hull, True)  # Compute perimeter
    # approx = cv2.approxPolyDP(hull, 0.05 * peri, True)

    # A rectangle must have 4 vertices
    # if len(approx) != 4:
    #     return False
    # for i in range(4):
    #     pt1, pt2, pt3 = approx[i - 1][0], approx[i][0], approx[(i + 1) % 4][0]
    #     ang = self._angle(pt1, pt2, pt3)
    #     if not (90 - 10 <= ang <= 90 + 10):
    #         return False
    # return True

    def _angle(self, pt1, pt2, pt3):
        """Calculate the angle between three points (in degrees)."""
        v1 = pt1 - pt2
        v2 = pt3 - pt2
        angle_rad = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
        return np.degrees(angle_rad)

    def ocr(self, img: np.ndarray) -> str:
        """Perform OCR on the image"""
        return pytesseract.image_to_string(img, lang="eng+equ", config="--oem 1 --psm 6")

    def get_avg_character_size(self, img: np.ndarray) -> Tuple[int, int]:
        """Use pytesseract to calculate average character size"""
        boxes: str = pytesseract.image_to_boxes(img)
        char_sizes = []
        avg_width: int = 0
        avg_height: int = 0
        for box in boxes.splitlines():
            b = box.split()
            x, y, x2, y2 = map(int, b[1:5])
            char_sizes.append((x2 - x, y2 - y))
        if char_sizes:
            avg_width = int(np.mean([size[0] for size in char_sizes]))
            avg_height = int(np.mean([size[1] for size in char_sizes]))
        return (avg_width, avg_height)

    def get_average_kernel_size(self, img: np.ndarray) -> Tuple[int, int]:
        """Get the average kernel size of the image"""
        contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        avg_width, avg_height = np.mean([(w, h) for (_, _, w, h) in map(cv2.boundingRect, contours)], axis=0)
        return (int(avg_width), int(avg_height))

    def get_base64_string(self, img) -> str:
        """Convert the image to base64 string"""
        _, buffer = cv2.imencode(".png", img)
        base64_string: str = base64.b64encode(buffer.tobytes()).decode("utf-8")
        return base64_string

    def stencil(self, contours: List[np.ndarray]) -> Tuple[int, int, int, int, np.ndarray]:
        """Stencil the image based on the contours"""
        x, y, w, h = cv2.boundingRect(np.vstack(contours))
        isolated = self.fill_pixels_outside_border(self.binary, contours)
        return (x, y, w, h, isolated[y : y + h, x : x + w])

    def remove_connected_components_by_area(self, img: np.ndarray, area_separator: int) -> np.ndarray:
        """This function removes the connected components by area,
        if the component box is large, it is likely not"""
        if np.all(img == 0):
            return img

        num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(img, connectivity=8)
        output = np.zeros_like(img)
        for i in range(1, num_labels):  # Skip the background (label 0)
            w0 = stats[i, cv2.CC_STAT_WIDTH]
            h0 = stats[i, cv2.CC_STAT_HEIGHT]
            # area = stats[i, cv2.CC_STAT_AREA]
            # ratio = area / (w0 * h0)

            if w0 * h0 > area_separator:
                continue
            # if ratio < 0.1:
            #     continue
            # if w0 == 1 or h0 == 1:
            #     continue
            # if area == w0 * h0 and w0 == h0:
            #     continue
            # if w0 / h0 > 5:
            #     continue

            output[labels == i] = 255  # Keep this component

        return output
