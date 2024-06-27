import unittest
from wsgiref.simple_server import make_server
import io

def application(environ, start_response):
    # Simular comportamento da aplicação
    path = environ['PATH_INFO']
    headers = [('Content-Type', 'text/html')]

    if path == '/':
        start_response('200 OK', headers)
        return [b'<h1>Hello, World!</h1>']
    else:
        start_response('404 Not Found', headers)
        return [b'<h1>Not Found</h1>']

class TestApp(unittest.TestCase):

    def setUp(self):
        self.capture_buffer = io.StringIO()

    def test_application(self):
        environ = {'PATH_INFO': '/'}
        application(environ, self.capture_buffer.write)
        self.capture_buffer.seek(0)
        response_html = self.capture_buffer.read()
        self.assertEqual(response_html, '<h1>ola!</h1>')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
