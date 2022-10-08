from server.setup.app import create_app
from server.setup.app.config import config

app = create_app(config)
