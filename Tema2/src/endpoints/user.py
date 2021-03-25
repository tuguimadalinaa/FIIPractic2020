import json
from flask import request, Blueprint, Response
from src.models.user import User
from src.utils.decorators import session, http_handling

user_bp = Blueprint('users', __name__, url_prefix='/users')


@user_bp.route('', methods=['GET'])
@http_handling
@session
def get_users(context):
    users = User.get_users(context)
    return Response(status=200, response=json.dumps(users))


@user_bp.route('', methods=['POST'])
@http_handling
@session
def post_user(context):  # register
    body = request.json
    User.create_user(context, body)
    return Response(status=201, response="Resource created")


@user_bp.route('/<int:user_id>', methods=['PUT'])
@http_handling
@session
def put_user(context, user_id):
    body = request.json
    User.update_user(context, body, user_id)
    return Response(status=200, response="Resource updated")


@user_bp.route('/<int:user_id>', methods=['DELETE'])
@http_handling
@session
def delete_user(context, user_id):
    User.deactivate_user(context, user_id)
    return Response(status=200, response="Resource deleted")
