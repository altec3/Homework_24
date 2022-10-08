import os


class Config:

    BASE_DIR = os.getcwd()
    DATA_DIR = os.path.join(BASE_DIR, "data")
    COMMANDS = ('filter', 'map', 'unique', 'sort', 'limit', 'regex')

    @staticmethod
    def init_app(app):
        pass


config = Config()
