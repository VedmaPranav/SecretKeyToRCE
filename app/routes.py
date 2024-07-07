from flask import request, Blueprint, make_response
import authentication
import controller

routes_config = Blueprint('route-config', __name__, template_folder="templates")


@routes_config.route('/token', methods=['GET'])  # route to get a auth token
def token():
    try:
        response = make_response(controller.get_user_token(), 200)
    except Exception as e:
        response = make_response({e}, 400)
    return response


@routes_config.route('/get_data', methods=['GET'])  # route to get application data
@authentication.token_required
def get_data():
    try:
        response = make_response(controller.get_data(), 200)
    except Exception as e:
        response = make_response({e}, 400)
    return response
