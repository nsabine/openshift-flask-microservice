import os
import logging
import socket
from flask import Flask, jsonify

HOST_NAME = os.environ.get('HOSTNAME', 'unknown')
BUILD_NAME = os.environ.get('OPENSHIFT_BUILD_NAME', 'unknown')
PROJECT = os.environ.get('OPENSHIFT_BUILD_NAMESPACE', 'unknown')

log = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/config')
def config():
    return jsonify({
        'host_name': HOST_NAME,
        'build_name': BUILD_NAME,
        'project': PROJECT,
        'host': socket.gethostname()
    })


@app.route("/")
def hello():
    return "Hello from %s" % HOST_NAME

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
