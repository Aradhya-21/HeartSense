import sys
import os

# Add root folder to sys.path so we can import back
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from back.app import app

class StripApiPrefixMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '')
        if path.startswith('/api'):
            # Strip the /api prefix for the Flask app routes
            environ['PATH_INFO'] = path[4:] or '/'
        return self.app(environ, start_response)

# Wrap the WSGI app with the middleware
app.wsgi_app = StripApiPrefixMiddleware(app.wsgi_app)

# Expose the app object for Vercel's serverless function builder
if __name__ == '__main__':
    app.run()
