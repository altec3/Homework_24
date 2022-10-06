from project.setup.app import create_app
from project.setup.app.config import config

app = create_app(config)
