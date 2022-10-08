from flask_restx import Api

api = Api(
    title="Homework 23",
    description="Developer: Aleksey Lesnikov",
    doc="/docs",
    validate=True,
)
