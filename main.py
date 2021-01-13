from flask import Flask, jsonify, request

app = Flask(__name__, static_folder='src')


@app.route('/api/call', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        return jsonify({"request": "post"})
    else:
        return jsonify({"request": "get"})


@app.route('/', defaults={'path': 'index'})
@app.route('/<path:path>')
def catch_pages(path):
    path = f'{path}.html'
    return app.send_static_file(path)
