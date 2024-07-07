from flask import Flask
from routes import routes_config
import unittest

app = Flask(__name__)
app.register_blueprint(routes_config)
app.register_blueprint(unittest.tstRoutes_config)

if __name__ == '__main__':
    app.run(port=8000)


