import datetime
import functools
from flask import request
from Model.User import User

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
            decrypt_token()
            validate_admin()
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
            if validate_token(token):
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

def validate_token(token:str):
    token_bits = token.split("|")
    if token_bits[0] == "guest@key.user" and datetime.time((float)token_bits[1])