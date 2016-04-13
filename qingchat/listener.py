import processer, utils
from wsgiref.simple_server import make_server


def receive(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    len = int(environ.get('CONTENT_LENGTH', 0))
    data = str(environ['wsgi.input'].read(len), encoding='utf-8')
    utils.append_file(data)
    processer.process()
    body = 'Hello'
    return [body.encode('utf-8')]


def start_server():
    httpd = make_server('', 8000, receive)
    print('Serving HTTP on port 8000...')
    httpd.serve_forever()
