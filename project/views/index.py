from flask_restx import Namespace, Resource
from flask import jsonify

from project.container import index_service
from project.setup.api.parsers import input_query

api = Namespace('/')


@api.route("/perform_query")
class QueriesResource(Resource):

    @api.expect(input_query)
    def post(self):
        payload = input_query.parse_args()
        response = index_service.get_result(payload=payload)

        if response:
            return jsonify(response)
        return None, 400
