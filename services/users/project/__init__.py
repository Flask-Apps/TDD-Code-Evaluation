import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


# instantiate the app
app = Flask(__name__)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


# instantiate the db
# db = SQLAlchemy(app)
db = SQLAlchemy()

def create_app(script_info=None):
    
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extension
    db.init_app(app)

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # shell context for flask cli
    # this register the app and db to the shell
    # this will allow us to work with the application context
    # and database without having to import them directly into the
    # shell
    app.shell_context_processor({
        'app': app,
        'db': db
    })
    return app
