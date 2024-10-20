from flask import Flask, request, jsonify
from db import db
from models import TaskModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.get('/tasks')
def get_tasks():
    tasks = TaskModel.query.all()
    tasks_list = [{'id': task.id, 'name': task.name} for task in tasks]
    return jsonify(tasks_list)


@app.post('/tasks')
def create_task():
    task_data = request.get_json()
    if 'name' not in task_data:
        return {'message': 'Bad request. Ensure "name"" are included in the JSON payload'}, 404

    existing_task = TaskModel.query.filter_by(name=task_data['name']).first()

    if existing_task:
        return {'message': 'Task with this name already exists'}, 404

    new_task = TaskModel(name=task_data['name'])
    db.session.add(new_task)
    db.session.commit()

    return jsonify({'id': new_task.id, 'name': new_task.name}), 201


@app.get('/tasks/<int:task_id>')
def get_specific_task(task_id):
    task = TaskModel.query.get(task_id)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404

    return jsonify({'id': task.id, 'name': task.name})


@app.delete('/tasks/<int:task_id>')
def delete_task(task_id):
    task = TaskModel.query.get(task_id)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({'message': 'Task deleted'})


@app.put('/tasks/<int:task_id>')
def update_task(task_id):
    task_data = request.get_json()
    if 'name' not in task_data:
        return jsonify({'message': 'Bad request. Ensure "name" is included in the JSON payload'}), 404

    task = TaskModel.query.get(task_id)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404

    existing_task = TaskModel.query.filter_by(name=task_data['name']).first()

    if existing_task:
        return {'message': 'Task with this name already exists'}, 404

    task.name = task_data['name']
    db.session.commit()

    return jsonify({'id': task.id, 'name': task.name})


if __name__ == '__main__':
    app.run(debug=True)
