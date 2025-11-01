import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "default_api_key")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default_jwt_secret")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

class Settings:
    PROJECT_NAME: str = "Car Price Prediction API"
    API_KEY: str = API_KEY
    JWT_SECRET_KEY: str = JWT_SECRET_KEY
    JWT_ALGORITHM: str = "HS256"
    REDIS_URL: str = REDIS_URL
    MODEL_PATH: str = "app/models/car_price_model.pkl"

settings = Settings()