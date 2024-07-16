from flask import jsonify


class ChatResponse:

    def __init__(self, ai_response, chat_id, status) -> None:
        self.ai_response = ai_response
        self.chat_id = chat_id
        self.status = status

    def format_response(self):
        return (
            jsonify(
                {
                    "ai_response": self.ai_response,
                    "chat_id": self.chat_id,
                }
            ),
            self.status,
        )
