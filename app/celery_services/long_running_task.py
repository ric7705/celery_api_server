from app import celery

from app.tasks.logging_to_file import LoggingToFile


@celery.task(bind=True)
def celery_logging_task(self, key, sleep=None):
    logging = LoggingToFile(key)

    self.update_state(state='PROGRESS', meta={"key": key})
    logging.exec(sleep)
