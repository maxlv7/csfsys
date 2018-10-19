def trueReturn(data, msg):
    return {
        "status": 200,
        "data": data,
        "msg": msg
    }


def falseReturn(data, msg):
    return {
        "status": -1,
        "data": data,
        "msg": msg
    }