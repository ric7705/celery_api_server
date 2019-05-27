class Config:
    BROKER_URL = 'redis://localhost'
    CELERY_RESULT_BACKEND = "db+sqlite:///celery.sqlite"

    CELERY_IMPORTS = ("app.celery_services.long_running_task",)

    CELERY_TRACK_STARTED = True
    CELERY_TASK_RESULT_EXPIRES = None

