import os
from flask import Flask
from celery import Celery
from app.config.celery_config import Config as config_celery

root_folder = os.path.dirname(os.path.abspath(__file__))

celery = Celery()
celery.config_from_object(config_celery)


def create_app():
    app = Flask(__name__)
    celery.conf.update(app.config)

    # blueprint
    from app.routes import long_running_task

    app.register_blueprint(long_running_task.bp)
    return app
