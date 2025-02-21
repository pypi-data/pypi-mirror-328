FROM mcr.microsoft.com/devcontainers/python:3

RUN python -m pip install --upgrade pip \
    && python -m pip install 'flit>=3.8.0'

# Install system dependencies
RUN apt update && apt install -y \
    libgl1 \
    libglib2.0-0 \
    poppler-utils \
    tesseract-ocr

ENV FLIT_ROOT_INSTALL=1

COPY pyproject.toml .
RUN touch README.md \
    && mkdir -p src/technical_drawing_parser \
    && python -m flit install --only-deps --deps develop \
    && rm -r pyproject.toml README.md src
