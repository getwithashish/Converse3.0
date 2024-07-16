import google.generativeai as genai
from google.generativeai.types.generation_types import StopCandidateException
import logging

from client.ai_models.ai_model import AIModel
from client.ai_models.gemini.config import GEMINI_MODEL_NAME, GOOGLE_API_KEY
from exceptions import SafetyException


logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)

logger = logging.getLogger(__name__)


class GeminiAIModel(AIModel):

    def __init__(self, model_name=GEMINI_MODEL_NAME) -> None:
        genai.configure(api_key=GOOGLE_API_KEY, transport="rest")
        self.model = genai.GenerativeModel(model_name)

    def chat(self, prompt, chat_history):
        try:
            self.chat = self.model.start_chat(history=chat_history)
            response = self.chat.send_message(prompt)
            content_parts = response.candidates[0].content.parts[0]
            return content_parts.text
        except StopCandidateException as sce:
            logger.error(sce)
            raise SafetyException()

    def get_chat_history(self):
        if self.chat:
            return self.chat.history
        return []
