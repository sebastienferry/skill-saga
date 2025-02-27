from flask import Flask
from routes import init_routes
from waitress import serve
import app

def create_app():
    app = Flask(__name__)
    
    # Initialize routes
    init_routes(app)
    
    return app

# For development and debug, we use the Flask development server through the app.py file
# For production, we use Waitress which is a production WSGI server.
# https://pypi.org/project/waitress/
if __name__ == "__main__":
    app = create_app()

    # Production WSGI server
    serve(app, host='0.0.0.0', port=8080)