import os

BASE_URL = os.getenv("BASE_URL", "https://automationexercise.com")
API_BASE_URL = os.getenv("API_BASE_URL", "https://automationexercise.com/api")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
ENV_NAME = os.getenv("ENV_NAME", "prod")
