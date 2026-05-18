import sys
from loguru import logger

# Remove default handler
logger.remove()

# Add a customized stdout handler
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO"
)

# Add a file handler
logger.add(
    "logs/test_execution.log",
    rotation="10 MB",
    retention="10 days",
    level="DEBUG",
    encoding="utf-8"
)

def log_response(response):
    logger.info(f"Request: {response.request.method} {response.request.url}")
    logger.info(f"Status Code: {response.status_code}")
    try:
        logger.debug(f"Response Body: {response.json()}")
    except Exception:
        logger.debug(f"Response Body: {response.text}")
