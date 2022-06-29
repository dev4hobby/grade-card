import boto3
from core.config import S3_BUCKET_NAME, CF_URL

s3 = boto3.resource("s3")

def upload_bytes_to_s3(bucket_name, key, bytes):
    s3.Bucket(bucket_name).put_object(Key=key, Body=bytes, ContentType="image/jpeg")
    return f"{CF_URL}/{key}"
