from app.utilities.util import get_now_str
import time


class LoggingToFile:
    def __init__(self, key):
        self.key = key

    def exec(self, sleep=5):

        while 1:
            with open('logging.txt', 'a') as f:
                f.write(f'key:{self.key}, {get_now_str()}\n')

            time.sleep(sleep)
