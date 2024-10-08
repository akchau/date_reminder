import logging
import time

import schedule

from src.init_app import get_app_data

logger = logging.getLogger(__name__)


schedule.every().day.at("18:29").do(get_app_data().controller.daily_reminder)


def start_reminder():
    try:
        logger.critical("Запущены уведомления!")
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logger.critical("Завершение работы программы.")
