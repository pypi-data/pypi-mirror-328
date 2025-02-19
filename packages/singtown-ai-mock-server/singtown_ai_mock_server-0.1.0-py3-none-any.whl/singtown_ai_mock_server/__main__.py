from flask import Flask, abort, request
import os
import json
from functools import wraps

TOKEN = "1234567890"

with open(os.path.join(os.path.dirname(__file__), "task.json")) as f:
    task = json.load(f)

with open(os.path.join(os.path.dirname(__file__), "project.json")) as f:
    project = json.load(f)

app = Flask(__name__, static_url_path='/media', static_folder='media')

def require_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers.get('Authorization') != f'Bearer {TOKEN}':
            abort(401)
        return f(*args, **kwargs)
    return decorated_function

@app.get("/tasks/<id>")
@require_auth
def get_task(id:str):
    return task

@app.get("/tasks/<id>/project")
@require_auth
def get_project(id:str):
    return project

@app.post("/tasks/<id>/status")
@require_auth
def update_task_status(id:str):
    status = request.json['status']
    task['status'] = status
    print(status)
    return "OK", 200

@app.post("/tasks/<id>/upload")
@require_auth
def upload_task_result(id:str):
    result_path = os.path.join(app.static_folder, request.files['file'].filename)
    with open(result_path, 'wb') as f:
        f.write(request.files['file'].read())
    return "OK", 200

@app.post("/tasks/<id>/log")
@require_auth
def upload_task_log(id:str):
    log = request.json['log']
    task['log'] += log
    print(log)
    return "OK", 200

@app.post("/tasks/<id>/metrics")
@require_auth
def upload_task_metrics(id:str):
    metric = request.json
    task['metrics'].append(metric)
    print(metric)
    return "OK", 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)