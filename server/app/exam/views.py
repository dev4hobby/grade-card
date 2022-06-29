from fastapi import APIRouter, File, UploadFile, HTTPException
from typing import Optional

from app.exam.services import (
    convert_document_to_images,
)

exam_router = APIRouter()

@exam_router.post(path="/convert", status_code=200)
async def convert(pdf_file: UploadFile = File(...), min_line_length: Optional[int] = 5000, max_line_gap: Optional[int] = 1000, margin: Optional[int] = 15):
    try:
        urls = await convert_document_to_images(pdf_file, min_line_length, max_line_gap, margin)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"status": "ok", "urls": urls}
