import os

BASE_URL = os.getenv("BASE_URL", "https://www.automationexercise.com")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
BROWSER = os.getenv("BROWSER", "chromium")
TIMEOUT = int(os.getenv("TIMEOUT", "5000"))
