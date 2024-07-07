import datetime
import functools
from flask import request
from Model.User import User
import controller


def admin_token_required(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            if validate_admin_token(token):
                pass
            else:
                raise Exception
        except Exception as e:
            return {
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        return f(*args, **kwargs)

    return decorated


def token_required(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            if validate_user_token(token):
                pass
            else:
                raise Exception
        except Exception as e:
            return {
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        return f(*args, **kwargs)

    return decorated


def validate_user_token(token: str):
    token_bits = controller.decrypt_token(token).split("_")
    if (token_bits[0].split(":")[1].strip() == "guest@key.user" and datetime.datetime.fromtimestamp(
            float(token_bits[1])) + datetime.timedelta(minutes=5) >= datetime.datetime.fromtimestamp(
            datetime.datetime.now().timestamp())) or token_bits[0].split(":")[1].strip() == "admin@key.user":
        return True
    else:
        return False


def validate_admin_token(token: str):
    admin_user = "admin@key.user_1720113899.479933_KeyInc"
    admin_token = controller.encrypt_user(admin_user).split(":")[1].strip()
    if token == admin_token:
        return True
    else:
        return False
