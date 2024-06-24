from flask import Flask
from routes import routes_config
from tst.unittest import tstRoutes_config

app = Flask(__name__)
app.register_blueprint(routes_config)
app.register_blueprint(tstRoutes_config)

if __name__ == '__main__':
    app.run(port=8000)


