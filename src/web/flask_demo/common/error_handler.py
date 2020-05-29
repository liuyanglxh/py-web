# coding=utf-8


import json
from flask import Blueprint, Response

from src.web.flask_demo.common.business_exception import BusinessException

exception = Blueprint('exception', __name__)


@exception.app_errorhandler(404)
def error_404(error):
    res = {"status": 404, "message": "404错误,找不到对应router"}
    return Response(json.dumps(res), mimetype='application/json')


@exception.app_errorhandler(Exception)
def error_exception(error):
    """这个handler可以catch住所有的abort(500)和raise exeception."""
    print error
    res = {"message": "服务器在开小差，稍后再试", 'success': 'false'}
    # 输出到特定的地方
    return Response(json.dumps(res), mimetype='application/json')


@exception.app_errorhandler(BusinessException)
def error_business(error):
    res = {"message": "服务器在开小差，稍后再试", 'success': 'false'}
    return Response(json.dumps(res), mimetype='application/json')
