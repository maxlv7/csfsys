from app import create_app
from  gevent.pywsgi import WSGIServer

app = create_app()

if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()