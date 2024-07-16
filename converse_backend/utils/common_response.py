from flask import jsonify


class CommonResponse:

    def __init__(self, message, status) -> None:
        self.message = message
        self.status = status

    def format_response(self):
        return (
            jsonify({"message": self.message}),
            self.status,
        )
