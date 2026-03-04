from datetime import UTC, datetime


def unique_email():
    timestamp  = datetime.now(UTC).strftime("%Y%m%d%H%M%S%f")
    return f"test_{timestamp}@example.com"

def create_dummy_user() -> dict:
    return {
        "name": "Mirko",
        "email": unique_email(),
        "password": "Test123!",  # NOSONAR
        "first_name": "Mirko",
        "last_name": "Milanovic",
        "address": "Test Street 1",
        "country": "Australia",
        "state": "TestState",
        "city": "TestCity",
        "zipcode": "11000",
        "mobile_number": "123456789",
    }
