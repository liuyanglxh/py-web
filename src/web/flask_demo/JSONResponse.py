# 重写response对象
from flask import jsonify
from werkzeug.wrappers import Response


class JSONResponse(Response):
    default_mimetype = "application/json"

    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, dict):
            response = jsonify(response)
        return super(JSONResponse, cls).force_type(response, environ)
