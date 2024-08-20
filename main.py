from flask import Flask
from flask_cors import CORS
from routes.routes import register_routes
from utils.function_global import get_local_ip

application = Flask(__name__)
CORS(application)

register_routes(application)

if __name__ == '__main__':
    HOST_CONNECT = get_local_ip()
    PORT_CONNECT = 5000
    application.run(host=HOST_CONNECT, port=PORT_CONNECT, debug=True)
