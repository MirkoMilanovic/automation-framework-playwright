import logging
from pathlib import Path


def configure_logger() -> None:
    """Configure root logger for console and file output."""
    root_logger = logging.getLogger()

    if root_logger.handlers:
        return

    root_logger.setLevel(logging.INFO)

    log_dir = Path("artifacts/logs")
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / "test_run.log"

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
