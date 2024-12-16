import logging
import os

def get_logger(name, log_file='tpshop_test.log', level=logging.DEBUG):
    # 定义日志格式，将其定义为（日志级别、时间戳、模块名、函数名、记录日志的代码行号、日志消息）
    LOG_FORMAT = '[%(levelname)s][%(asctime)s][%(module)s.%(funcName)s] [%(lineno)d]: %(message)s'

    # 创建日志记录器
    logger = logging.getLogger(name)
    logger.setLevel(level)  # 设置日志记录级别

    # 日志文件路径
    log_dir = '../log'
    log_file_path = os.path.join(log_dir, log_file)

    # 确保日志目录存在
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 判断是否有处理器
    if not logger.handlers:
        formatter = logging.Formatter(LOG_FORMAT)  # 创建日志格式器

        # 创建文件处理器
        file_handler = logging.FileHandler(log_file_path, encoding='utf-8')
        file_handler.setLevel(level)  # 文件处理器级别
        file_handler.setFormatter(formatter)  # 将格式器添加到文件处理器

        # 创建控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)

        # 将文件和控制台处理器添加到日志处理器
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

