import logging 
import os

# Log directory setup
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# File path
LOG_FILE = os.path.join(LOG_DIR, "system.log")

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),  # Save to file
        logging.StreamHandler()         # Print to console
    ]
)

logger = logging.getLogger("FunctionScheduler")

def log_result(result: dict):
    """
    Logs the result of a function execution.
    Example input:
    {
        "latency": 123,
        "success": True,
        "cpu": 15.5,
        "memory": 30.2
    }
    """
    status = "SUCCESS ✅" if result.get("success") else "FAILED ❌"
    logger.info(
        f"Execution: {status} | Latency={result.get('latency')}ms | "
        f"CPU={result.get('cpu')}% | Memory={result.get('memory')}MB"
    )
