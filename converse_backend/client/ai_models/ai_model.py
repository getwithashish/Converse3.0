from abc import ABC, abstractmethod


class AIModel(ABC):

    @abstractmethod
    def chat(chat_history):
        pass

    @abstractmethod
    def get_chat_history():
        pass
