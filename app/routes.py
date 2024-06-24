from flask import request, Blueprint, make_response
import authentication
import controller

routes_config = Blueprint('route-config', __name__, template_folder="templates")

@routes_config.route('/token', methods=['GET']) # route to get a auth token
def token():
    try:
        data = request.get_json()
        response = make_response(controller.register_user(data['username'], data['email'], data['password']), 200)
    except Exception as e:
        response = make_response({e}, 400)
    return response


@routes_config.route('/getData', methods=['GET']) # route to get application data
@authentication.token_required
def getData():
    try:
        data = request.get_json()
        response = make_response(controller.getData(), 200)
    except Exception as e:
        response = make_response({e}, 400)
    return response
