import boto3
from app.settings import (
    AWS_SECRET_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_REGION_NAME,
    AWS_CF_URL,
)

s3 = boto3.resource(
    "s3",
    aws_access_key_id=AWS_SECRET_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION_NAME,
)

def upload_bytes_to_s3(bucket_name, key, bytes):
    s3.Bucket(bucket_name).put_object(Key=key, Body=bytes, ContentType="image/jpeg")
    return f"{CF_URL}/{key}"
