import boto3
from app.core.config import settings

def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )

def upload_file_to_s3(file_path, key):
    s3 = get_s3_client()
    s3.upload_file(file_path, settings.AWS_S3_BUCKET, key)
