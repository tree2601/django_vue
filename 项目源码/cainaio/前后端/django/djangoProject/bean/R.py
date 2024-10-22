from rest_framework.response import Response


def ok(msg=None,data=None):
    result = {
        'code': 200,
        'msg': msg,
        'data': data
    }
    return Response(result);

def fail(msg=None,data=None):
    result = {
        'code': 201,
        'msg': msg,
        'data': data
    }
    return Response(result);
