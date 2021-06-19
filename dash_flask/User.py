from flask_login import UserMixin


# user models
class User(UserMixin):
    def is_authenticated(self):
        return True

    def is_actice(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return "1"