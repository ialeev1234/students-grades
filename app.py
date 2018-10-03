import os

from bottle import run

import api_routes, routes

if os.environ.get('APP_LOCATION') == 'heroku':
    host, port = '0.0.0.0', int(os.environ.get('PORT', 5000))
else:
    host, port = '127.0.0.1', 8080

url = f"http://{host}:{port}"

if __name__ == '__main__':
    run(host=host, port=port)
