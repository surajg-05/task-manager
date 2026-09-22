from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = [
    {"id": 1, "title": "Learn AWS", "completed": False},
    {"id": 2, "title": "Build CI/CD pipeline", "completed": False}
]


@app.get("/api/tasks")
def get_tasks():
    return jsonify(tasks)


@app.post("/api/tasks")
def add_task():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "completed": False
    }

    tasks.append(task)

    return jsonify(task), 201


@app.delete("/api/tasks/<int:task_id>")
def delete_task(task_id):
    global tasks

    tasks = [task for task in tasks if task["id"] != task_id]

    return jsonify({"message": "Task deleted"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)