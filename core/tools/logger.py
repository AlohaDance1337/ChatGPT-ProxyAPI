import logging
import os

from datetime import datetime


class Logger:
    def __init__(self, log_dir='logs', log_file='app.log', log_level=logging.INFO):
        # Создаем директорию для логов, если ее нет
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        self.log_file_path = os.path.join(log_dir, log_file)

        # Настраиваем формат логов
        log_format = '%(asctime)s - %(levelname)s - %(message)s'
        logging.basicConfig(filename=self.log_file_path, level=log_level, format=log_format)

        # Создаем логгер
        self.logger = logging.getLogger()

        # Добавляем вывод в консоль
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(log_format))
        self.logger.addHandler(console_handler)

    def info(self, message):
        """Логирование информационных сообщений"""
        self.logger.info(message)

    def warning(self, message):
        """Логирование предупреждений"""
        self.logger.warning(message)

    def error(self, message):
        """Логирование ошибок"""
        self.logger.error(message)

    def debug(self, message):
        """Логирование отладочных сообщений"""
        self.logger.debug(message)

    def critical(self, message):
        """Логирование критических ошибок"""
        self.logger.critical(message)