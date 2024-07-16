from flask import request
from flask_jwt_extended import get_jwt, jwt_required

from client.ai_models.gemini.gemini_ai_model import GeminiAIModel
from utils.common_response import CommonResponse
from messages import (
    CHAT_HISTORY_LIST_RETRIEVED,
    CHAT_HISTORY_RETRIEVED,
    CHAT_HISTORY_UNAVAILABLE,
    INVALID_PROMPT,
)
from converse_backend.service.normal_ai_chatter import NormalAiChatter
from utils.chat_response import ChatResponse


@jwt_required()
def NormalAiChat():
    prompt = request.json.get("prompt", None)
    chat_id = request.json.get("chat_id", None)
    user_id = get_jwt().get("user_id", None)

    if prompt:
        gemini_ai_model = GeminiAIModel()
        normal_chatter = NormalAiChatter(gemini_ai_model)
        ai_response, chat_id = normal_chatter.chat(prompt, chat_id, user_id)
        status = 200
    else:
        ai_response = INVALID_PROMPT
        status = 400

    return ChatResponse(ai_response, chat_id, status).format_response()


@jwt_required()
def NormalAiChatHistoryList():
    user_id = get_jwt().get("user_id", None)

    normal_chatter = NormalAiChatter()
    chat_list = normal_chatter.get_chat_history_list(user_id)
    status = 200

    return CommonResponse(CHAT_HISTORY_LIST_RETRIEVED, status, chat_list)


@jwt_required()
def NormalAiChatHistory():
    user_id = get_jwt().get("user_id", None)
    chat_id = request.args.get("chat_id", None)

    normal_chatter = NormalAiChatter()
    chat_history = normal_chatter.get_chat_history(user_id, chat_id)
    if chat_history:
        status = 200
        return CommonResponse(CHAT_HISTORY_RETRIEVED, status, chat_history)

    status = 404
    return CommonResponse(CHAT_HISTORY_UNAVAILABLE, status, None)


@jwt_required()
def deleteNormalAiChatHistory():
    user_id = get_jwt().get("user_id", None)
    chat_id = request.args.get("chat_id", None)

    normal_chatter = NormalAiChatter()
    normal_chatter.delete_chat_history(user_id, chat_id)

    status = 204
    return "", status
