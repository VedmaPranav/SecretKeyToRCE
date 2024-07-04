import datetime


class User:
    def __init__(self, username: str, issue: datetime):
        self.username = username
        self.issue = issue

    # @staticmethod
    # def encrypt_token(self, user_token):
