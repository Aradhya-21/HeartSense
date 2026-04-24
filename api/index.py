from vercel_python import create_wsgi_app
from app import app  # Import your Flask app

# Create the serverless function
api = create_wsgi_app(app)
