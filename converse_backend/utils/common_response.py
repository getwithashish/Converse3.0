from flask import jsonify


class CommonResponse:

    def __init__(self, message, status, data=None) -> None:
        self.message = message
        self.status = status
        self.data = data

    def format_response(self):
        return (
            jsonify({"message": self.message, "data": self.data}),
            self.status,
        )
