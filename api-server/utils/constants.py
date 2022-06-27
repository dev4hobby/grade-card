from . import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
JPG_DIR = os.path.join(DATA_DIR, "jpg")
PDF_DIR = os.path.join(DATA_DIR, "pdf")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

S3_BUCKET_NAME = "grade-card"