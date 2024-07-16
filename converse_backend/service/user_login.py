from flask_jwt_extended import create_access_token

from messages import INVALID_USERNAME_PASSWORD
from models.user import User


class UserLogin:

    def login(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            additional_claims = {"user_id": user.id}
            access_token = create_access_token(
                identity=username, additional_claims=additional_claims
            )
            return access_token, 200
        else:
            return INVALID_USERNAME_PASSWORD, 400
