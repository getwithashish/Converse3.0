import jsonpickle

from exceptions import ChatNotFoundException
from models.models import delete_objects
from models.normal_chat_history import NormalChatHistory


class NormalAiChatter:

    def __init__(self, model=None) -> None:
        self.model = model

    def chat(self, prompt, chat_id, user_id):
        chat_history = []
        if chat_id:
            normal_chat_history = (
                NormalChatHistory.query.filter_by(user_id=user_id)
                .filter_by(id=chat_id)
                .first()
            )
            if not normal_chat_history:
                raise ChatNotFoundException()
            chat_history = jsonpickle.decode(normal_chat_history.chat_history)
        else:
            normal_chat_history = NormalChatHistory(
                chat_history=chat_history, user_id=user_id
            )
            normal_chat_history.save()
            chat_id = normal_chat_history.id

        ai_response = self.model.chat(prompt, chat_history)
        self.save_chat_history(normal_chat_history)

        return ai_response, chat_id

    def get_chat_history_list(self, user_id):
        chat_history_list = NormalChatHistory.query.filter_by(user_id=user_id).all()
        chat_list = [
            {"chat_id": chat.id, "chat_name": chat.started_at}
            for chat in chat_history_list
        ]

        return chat_list

    def get_chat_history(self, user_id, chat_id):
        normal_chat_history = (
            NormalChatHistory.query.filter_by(user_id=user_id)
            .filter_by(id=chat_id)
            .first()
        )

        if normal_chat_history:
            chat_history = jsonpickle.decode(normal_chat_history.chat_history)
            chat_history_data = {
                "chat_id": chat_id,
                "chat_history": [
                    {"text": chat.parts[0].text, "role": chat.role}
                    for chat in chat_history
                ],
            }
            return chat_history_data

        return []

    def save_chat_history(self, normal_chat_history):
        chat_history = self.model.get_chat_history()
        chat_history_json_string = jsonpickle.encode(chat_history)
        normal_chat_history.chat_history = chat_history_json_string
        normal_chat_history.save()

        return True

    def delete_chat_history(self, user_id, chat_id):
        if chat_id:
            normal_chat_history = (
                NormalChatHistory.query.filter_by(user_id=user_id)
                .filter_by(id=chat_id)
                .all()
            )
        else:
            normal_chat_history = NormalChatHistory.query.filter_by(
                user_id=user_id
            ).all()

        delete_objects(normal_chat_history)

        return True
