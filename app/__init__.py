from flask import Flask
from .config import config_options
from flask_bootstrap import Bootstrap

#intializing Flask Extensions
bootstrap = Bootstrap()

def create_app(config_name)

#initializing application
app = Flask(__name__)

   #creating the app configurations
    app.config.from_object(config_options[config_name])

    # initializing flask extensions
    bootstrap.init_app(app)

    # registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    return app