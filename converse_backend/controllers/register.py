from flask import request

from utils.common_response import CommonResponse
from service.user_registration import UserRegistration


def register():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user_registration = UserRegistration()
    message, status = user_registration.register(username, password)

    return CommonResponse(message, status).format_response()
