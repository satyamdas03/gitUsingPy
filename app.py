from flask import Flask, request, jsonify
import version_control

app = Flask(__name__)

@app.route('/init', methods=['POST'])
def init_repo():
    data = request.get_json()
    repo_name = data.get('repo_name')
    version_control.init(repo_name)
    return jsonify({"message": f"Repository {repo_name} initialized."})

@app.route('/add', methods=['POST'])
def add_files():
    data = request.get_json()
    paths = data.get('paths')
    version_control.add(paths)
    return jsonify({"message": "Files added to index."})

@app.route('/commit', methods=['POST'])
def commit_changes():
    data = request.get_json()
    message = data.get('message')
    author = data.get('author')
    sha1 = version_control.commit(message, author)
    return jsonify({"message": "Commit successful.", "sha1": sha1})

# Add other routes for status, diff, push, etc.

if __name__ == '__main__':
    app.run(debug=True)
