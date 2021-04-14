from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

PORT = 8000


def application(env, start_response):
    setup_testing_defaults(env)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'DAS WORK!!']


with make_server('', PORT, application) as httpd:
    print(f'Start server at {PORT}...')
    httpd.serve_forever()

