from flask import Flask

from server.setup.api import api
from server.views import query_ns


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    app.app_context().push()

    config_obj.init_app(app)
    api.init_app(app)
    api.add_namespace(query_ns)

    return app
