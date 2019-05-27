import time

from flask import Blueprint, request, jsonify
from app.celery_services.long_running_task import celery_logging_task
from app import celery
from app.utilities.util import get_tasks, set_task, get_now_str

bp = Blueprint('long_running_task', __name__, url_prefix='/long_running_task')


@bp.route('/status', methods=['GET'])
def status():

    task_list = get_tasks()
    for task in task_list:
        celery_task = celery.AsyncResult(task['task_id'])
        task['status'] = not celery_task.status
    return jsonify(task_list)


@bp.route('/start', methods=['POST'])
def start():

    task_obj = celery_logging_task.delay(request.json['key'], request.json['sleep'])

    print(f'task id:{task_obj.task_id}')
    task_list = get_tasks()
    dt = get_now_str()
    task_list.append({"task_id": task_obj.task_id, "key": request.json['key'],
                      "sleep": request.json['sleep'], "update_dt": dt, "status": task_obj.state})
    set_task(task_list)

    return jsonify({"status": "success", "task_id": str(task_obj.id)})


@bp.route('/stop', methods=['POST'])
def stop():
    key = request.json['key']

    task_list = get_tasks()

    for i in range(len(task_list)):
        task = task_list[i]

        if task['key'] == key:
            task_id = task['task_id']
            celery.control.revoke(task_id, terminate=True)

            del task_list[i]
            set_task(task_list)

            return jsonify({"status": "success"})

    return jsonify({"status": "fail"})
