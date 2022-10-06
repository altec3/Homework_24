from flask_restx.reqparse import RequestParser

from project.setup.app.config import config

input_query: RequestParser = RequestParser()
input_query.add_argument(name='file_name', type=str, location='json', required=True, nullable=False)
input_query.add_argument(
    name='cmd1',
    choices=config.COMMANDS,
    location='json',
    required=True,
    nullable=False
)
input_query.add_argument(
    name='cmd2',
    choices=config.COMMANDS,
    location='json',
    required=True,
    nullable=False
)
input_query.add_argument(name='value1', type=str, location='json', required=True, nullable=False)
input_query.add_argument(name='value2', type=str, location='json', required=True, nullable=False)
