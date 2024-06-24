import functools
from flask import request

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
            ##TO_DO Determine if user is admin
        except Exception as e:
             return {
                 "message": "Invalid Authentication token!",
                 "data": None,
                 "error": "Unauthorized"
             }, 401
        return f(*args, **kwargs)
    return decorated