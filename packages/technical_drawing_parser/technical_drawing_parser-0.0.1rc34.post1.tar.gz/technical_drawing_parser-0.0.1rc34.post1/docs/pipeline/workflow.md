```mermaid
flowchart LR
    LLM[LLM]
    PP[Preprocessing Pipeline]
    OCR[OCR]

    A[/PDF Drawing/]
    Img[/Image/]
    B[/Block/]
    C[/ParsedBlocks/]
    D[/BillOfMaterialsTable/]
    E[/ParsedBlock/]

    A -- convert each page to image --> Img --> PP --> B --> OCR --> E --> LLM
    LLM --> C
    LLM --> D    

```