from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from models.models import db
from utils.decouple_config_util import DecoupleConfigUtil
from controllers.register import register
from controllers.login import login
from controllers.normal_ai_chat import NormalAiChat


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
app.route("/chat_with_ai", methods=["POST"])(NormalAiChat)

if __name__ == "__main__":
    app.run(debug=True, host=config("HOST"), port=config("PORT"))
