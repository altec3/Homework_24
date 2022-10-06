import os


class Config:

    BASE_DIR = os.getcwd()
    DATA_DIR = os.path.join(BASE_DIR, "data")

    @staticmethod
    def init_app(app):
        pass


config = Config()
