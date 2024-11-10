# controllers/user_controller.py

from models.user_model import UserModel
from utils.security import hash_password

class UserController:
    def __init__(self):
        self.user_model = UserModel()

    def add_user(self, username, password, role):
        return self.user_model.create_user(username, password, role)

    def get_user(self, username):
        return self.user_model.get_user_by_username(username)

    def update_last_login(self, user_id):
        self.user_model.update_last_login(user_id)

    def close(self):
        self.user_model.close()
