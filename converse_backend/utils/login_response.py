from flask import jsonify


class LoginResponse:

    def __init__(self, access_token, status) -> None:
        self.access_token = access_token
        self.status = status

    def format_response(self):
        return (
            jsonify({"access_token": self.access_token}),
            self.status,
        )
