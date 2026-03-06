from datetime import UTC, datetime


def unique_email() -> str:
    """Generate a unique email address for registration tests."""
    timestamp = datetime.now(UTC).strftime("%Y%m%d%H%M%S%f")
    return f"test_{timestamp}@example.com"


def create_dummy_user() -> dict[str, str]:
    """Return test data for a newly registered user."""
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


def pre_existing_dummy_user() -> dict[str, str]:
    """Return credentials for an existing user account used in login tests."""
    return {
        "name": "Mirko",
        "email": "mirko@email.com",
        "password": "Test123!",  # NOSONAR
    }
