from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from messages import CHAT_NOT_FOUND, CHAT_RESPONSE_NOT_SAFE
from exceptions import ChatNotFoundException, SafetyException
from models.models import db
from utils.decouple_config_util import DecoupleConfigUtil
from utils.common_response import CommonResponse
from controllers.register import register
from controllers.login import login
from controllers.normal_ai_chat import (
    NormalAiChat,
    NormalAiChatHistory,
    NormalAiChatHistoryList,
    deleteNormalAiChatHistory,
)


config = DecoupleConfigUtil.get_env_config()

app = Flask(__name__)
app.secret_key = config("APP_SECRET_KEY")

app.config["SQLALCHEMY_DATABASE_URI"] = config("DATABASE_URI")
app.config["JWT_SECRET_KEY"] = config("JWT_SECRET_KEY")

db.init_app(app)
jwt = JWTManager(app)

CORS(
    app,
    origins=config(
        "CORS_ORIGINS", cast=lambda v: [item.strip() for item in v.split(",")]
    ),
)

with app.app_context():
    db.create_all()


app.route("/register", methods=["POST"])(register)
app.route("/login", methods=["POST"])(login)
app.route("/normal_chat_with_ai", methods=["POST"])(NormalAiChat)
app.route("/normal_chat_history_list", methods=["GET"])(NormalAiChatHistoryList)
app.route("/normal_chat_history", methods=["GET"])(NormalAiChatHistory)
app.route("/normal_chat_history_list", methods=["DELETE"])(deleteNormalAiChatHistory)


@app.errorhandler(SafetyException)
def handle_safety_exception(error):
    status = 403
    return CommonResponse(CHAT_RESPONSE_NOT_SAFE, status, None).format_response()


@app.errorhandler(ChatNotFoundException)
def handle_chat_not_found_exception(error):
    status = 404
    return CommonResponse(CHAT_NOT_FOUND, status, None).format_response()


if __name__ == "__main__":
    app.run(debug=True, host=config("HOST"), port=config("PORT"))
