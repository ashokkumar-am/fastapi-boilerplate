import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "FastAPI Professional App"
    MONGO_URL = os.getenv("MONGO_URL")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")

settings = Settings()
