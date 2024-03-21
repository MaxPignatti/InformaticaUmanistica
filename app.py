from flask import Flask, send_from_directory, jsonify, request
from llama2 import Llama2
import os

app = Flask(__name__, static_folder='/frontend/build', static_url_path='')
llama = Llama2()

# Serve the index.html file for the root URL
@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

# Serve static files from the build directory
@app.route('/<path:path>')
def static_proxy(path):
    file_name = path.split('/')[-1]
    directory_name = os.path.join(app.static_folder, '/'.join(path.split('/')[:-1]))
    return send_from_directory(directory_name, file_name)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"HELLO!"})

# Route for handling API requests via POST
@app.route('/api/sendText', methods=['POST'])
def handle_post():
    # Get the data from the POST request
    data = request.json

    # Extract the text from the request
    text = data.get('text')

    # Pass the text to Llama2 for processing
    response = llama.process(text)

    # Return the response obtained from Llama2
    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(debug=True)
