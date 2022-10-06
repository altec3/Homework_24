from flask import Flask

from project.setup.api import api
from project.views import query_ns


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    app.app_context().push()

    config_obj.init_app(app)
    api.init_app(app)
    api.add_namespace(query_ns)

    return app
