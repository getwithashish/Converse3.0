from flask import request
from flask_jwt_extended import get_jwt, jwt_required

from client.ai_models.gemini.gemini_ai_model import GeminiAIModel
from messages import INVALID_PROMPT
from service.normal_chatter import NormalChatter
from utils.chat_response import ChatResponse


@jwt_required()
def NormalAiChat():
    prompt = request.json.get("prompt", None)
    chat_id = request.json.get("chat_id", None)
    user_id = get_jwt().get("user_id", None)

    if prompt:
        gemini_ai_model = GeminiAIModel()
        normal_chatter = NormalChatter(gemini_ai_model)
        ai_response, chat_id = normal_chatter.chat(prompt, chat_id, user_id)
        status = 200
    else:
        ai_response = INVALID_PROMPT
        status = 400

    return ChatResponse(ai_response, chat_id, status).format_response()
