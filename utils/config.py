import os

BASE_URL: str = os.getenv("BASE_URL", "https://www.automationexercise.com")
HEADLESS: bool = os.getenv("HEADLESS", "true").lower() == "true"
BROWSER: str = os.getenv("BROWSER", "chromium")
TIMEOUT: int = int(os.getenv("TIMEOUT", "5000"))
