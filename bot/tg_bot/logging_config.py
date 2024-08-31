import logging
import os
from logging.handlers import TimedRotatingFileHandler

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
log_file = os.path.join(LOG_DIR, "bot.log")

handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=5)
handler.setFormatter(log_formatter)
handler.setLevel(logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)