from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [ { "label": "Scratch my back", "done": False } ]

@app.route('/todos', methods=['GET'])
def hello_world():
    text = jsonify(todos)
    return text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    return jsonify(todos)

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)