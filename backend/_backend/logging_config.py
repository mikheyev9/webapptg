import logging
import os
from logging.handlers import TimedRotatingFileHandler

LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

log_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger("my_project")
logger.setLevel(logging.INFO)

file_handler = TimedRotatingFileHandler(
    os.path.join(LOG_DIR, "fastapi.log"),
    when="midnight",
    interval=1,
    backupCount=5
)
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.INFO)

# Добавление обработчика в логгер
logger.addHandler(file_handler)

# # Вывод логов в консоль
# console_handler = logging.StreamHandler()
# console_handler.setFormatter(log_formatter)
# console_handler.setLevel(logging.INFO)
# logger.addHandler(console_handler)