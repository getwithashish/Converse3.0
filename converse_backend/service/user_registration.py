from models.user import User
from messages import (
    PASSWORD_REQUIRED,
    USER_REGISTRATION_SUCCESSFUL,
    USERNAME_EXISTS,
    USERNAME_REQUIRED,
)


class UserRegistration:

    def register(self, username, password):
        if not username:
            message = USERNAME_REQUIRED
            status = 400
        elif not password:
            message = PASSWORD_REQUIRED
            status = 400
        elif User.query.filter_by(username=username).first():
            message = USERNAME_EXISTS
            status = 400
        else:
            new_user = User(username=username)
            new_user.set_password(password)
            new_user.save()
            message = USER_REGISTRATION_SUCCESSFUL
            status = 201

        return message, status
