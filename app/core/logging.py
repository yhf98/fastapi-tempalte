import logging
import os
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
from app.core.config import settings

def setup_logger():
    # 日志目录
    log_dir = settings.LOG_DIR
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 当前日期
    current_date = datetime.now().strftime("%Y-%m-%d")

    # 日志文件名
    log_filename = os.path.join(log_dir, f"log_{current_date}.log")

    # 配置日志格式
    log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 创建一个处理程序，用于按天滚动日志文件
    file_handler = TimedRotatingFileHandler(log_filename, when="midnight", interval=1)
    file_handler.setFormatter(log_formatter)
    file_handler.suffix = "%Y-%m-%d"

    # 清除现有处理程序
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # 将处理程序添加到根记录器
    logging.basicConfig(level=settings.LOG_LEVEL, handlers=[file_handler])

    # 创建一个 FastAPI 日志记录器
    logger = logging.getLogger("fastapi")

    # 添加控制台处理程序（可选）
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    logging.getLogger().addHandler(console_handler)

setup_logger()
