from datetime import datetime
from flask import json
from werkzeug.wrappers import Response


class DateTimeEncoder(json.JSONEncoder):
    # default 解析json dumps 无法解析的类型
    def default(self, obj):
        if isinstance(obj, datetime):
            return ''.join([obj.isoformat(), 'Z'])
        elif isinstance(obj, bytes):
            return obj.decode('utf-8')

        return json.JSONEncoder.default(self, obj)


class ApiResult(object):

    def __init__(self, value, status=200):
        self.value = value
        self.status = status

    def to_response(self):
        return Response(json.dumps(self.value, cls=DateTimeEncoder),
                        status=self.status,
                        mimetype='application/json')
