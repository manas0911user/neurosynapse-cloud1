from utils.logger import log_result
from db.models import init_db, save_execution

# Init DB
init_db()

# Fake result
result = {
    "latency": 145,
    "success": True,
    "cpu": 17.5,
    "memory": 25.3
}

# Log + Save
log_result(result)
save_execution(result)
print("✅ Result logged and saved to DB!")
