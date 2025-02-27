from flask import Flask

app = Flask(__name__)

# Configuration de base de l'application
app.config['JSON_SORT_KEYS'] = False

from routes import *

if __name__ == '__main__':
    app.run(debug=True)