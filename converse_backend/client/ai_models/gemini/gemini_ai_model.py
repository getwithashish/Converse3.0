import google.generativeai as genai

from client.ai_models.ai_model import AIModel
from client.ai_models.gemini.config import GEMINI_MODEL_NAME, GOOGLE_API_KEY


class GeminiAIModel(AIModel):

    def __init__(self, model_name=GEMINI_MODEL_NAME) -> None:
        genai.configure(api_key=GOOGLE_API_KEY, transport="rest")
        self.model = genai.GenerativeModel(model_name)

    def chat(self, prompt, chat_history):
        self.chat = self.model.start_chat(history=chat_history)
        response = self.chat.send_message(prompt)
        content_parts = response.candidates[0].content.parts[0]
        return content_parts.text

    def get_chat_history(self):
        if self.chat:
            return self.chat.history
        return []
