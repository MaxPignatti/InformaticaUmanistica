
from flask import Flask, send_from_directory, jsonify, request
import os
app = Flask(__name__, static_folder='/frontend/build', static_url_path='')

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

@app.route('/api/sendText',methods=['POST'])
def hello():
    data = request.json
    text = data.get('text')
    #Usiamo il modello
    return "YES" #Risposta dal modello (o creiamo la playlist e ritorniamo un success)

if __name__ == '__main__':
    app.run()