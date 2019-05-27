import datetime
import time
import os
import json

from app import root_folder


def get_now_str():
    ts = time.time()
    return datetime.datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


def set_task(tasks):
    '''
    because backend_extended config is not working, we need to implement the mapping between task_id and keys by ourselves
    see https://github.com/celery/celery/pull/5498/commits
    '''
    file_path = os.path.join(root_folder, 'tasks.temp')

    with open(file_path, 'w') as outfile:
        json.dump(tasks, outfile)


def get_tasks():
    '''
    because backend_extended config is not working, we need to implement the mapping between task_id and keys by ourselves
    see https://github.com/celery/celery/pull/5498/commits
    '''
    file_path = os.path.join(root_folder, 'tasks.temp')

    try:
        with open(file_path) as json_file:
            task_list = json.load(json_file)
            return task_list

    except json.decoder.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
