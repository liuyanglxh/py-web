# coding=utf-8
from flask import Blueprint, request
from src.web.flask_demo.common.business_exception import BusinessException

recommend = Blueprint('recommend', __name__)


@recommend.route("/get-recommend")
def get_recommend():
    return "推荐", 200


@recommend.route(rule="/add-recommend", methods=['PUT'])
def add_recommend():
    name, age = request.args.get('name'), request.args.get('age')
    return '添加成功!', 200


@recommend.route(rule='/test-error')
def test_error():
    a, b = request.args.get('a'), request.args.get('b')
    if b == 0:
        raise BusinessException('除数不能为0', status_code=410)
    a, b = int(a), int(b)
    raise a / b
