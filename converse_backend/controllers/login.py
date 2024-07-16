from flask import request

from utils.login_response import LoginResponse
from utils.common_response import CommonResponse
from service.user_login import UserLogin


def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user_login = UserLogin()
    response, status = user_login.login(username, password)
    if status != 200:
        return CommonResponse(response, status)
    else:
        return LoginResponse(response, status)
