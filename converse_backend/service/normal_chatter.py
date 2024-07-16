import jsonpickle

from models.normal_chat_history import NormalChatHistory


class NormalChatter:

    def __init__(self, model) -> None:
        self.model = model

    def chat(self, prompt, chat_id, user_id):
        chat_history = []
        if chat_id:
            normal_chat_history = (
                NormalChatHistory.query.filter_by(user_id=user_id)
                .filter_by(id=chat_id)
                .first()
            )
            chat_history = jsonpickle.decode(normal_chat_history.chat_history)
        else:
            normal_chat_history = NormalChatHistory(
                chat_history=chat_history, user_id=user_id
            )
            normal_chat_history.save()
            chat_id = normal_chat_history.id

        print("Reached Here: ", self.model.chat)

        ai_response = self.model.chat(prompt, chat_history)
        print("Reached Here 2")

        self.save_chat_history(normal_chat_history)

        return ai_response, chat_id

    def save_chat_history(self, normal_chat_history):
        chat_history = self.model.get_chat_history()
        chat_history_json_string = jsonpickle.encode(chat_history)
        normal_chat_history.chat_history = chat_history_json_string
        normal_chat_history.save()
        return True
