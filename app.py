import json
from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/todos.json', methods=['GET', 'POST'])
def todo():
    todos = []

    if request.method == 'POST':
	todos = (request.get_json())

    return Response(json.dumps(todos), mimetype='application/json')

app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))
if __name__ == '__main__':
    app.run(port=3000, debug=True)
