from flask import json


class Result(object):
    success = True
    data = None
    code = 200

    def __init__(self, success, data, code):
        self.success = success
        self.data = data
        self.code = code


r = Result(True, "a", 200)
print json.dumps(r, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)
