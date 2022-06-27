from . import boto3
from .constants import S3_BUCKET_NAME

s3 = boto3.resource("s3")

def upload_bytes_to_s3(bucket_name, key, bytes):
    s3.Bucket(bucket_name).put_object(Key=key, Body=bytes, ContentType="image/jpeg", ContentEncoding="base64")
