# -*- coding: utf-8 -*

from wsgiref.simple_server import make_server
import os

def application(environ, start_response):

    str_info = environ['PATH_INFO'][1:]

    if str_info.endswith('.html'):
        start_response('200 OK', [('Content-Type', 'text/html')])
        if not os.path.exists(str_info):
            start_response("404 not Found")
            return
        file_object = open(str_info, "r")
        try:
            all_the_text = file_object.read()
        finally:
            file_object.close()
            start_response(all_the_text)
    else:
        start_response('200 OK', [('Content-Type', 'text/html')])
        return '<h1>Hello, %s!</h1>' % (str_info or 'chp')

    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, %s!</h1>' % (str_info or 'chp')

# 创建服务器
httpd = make_server('', 8888, application)
print "Serving HTTP on port 8888..."
# 监听
httpd.serve_forever()
