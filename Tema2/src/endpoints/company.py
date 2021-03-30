import json

from flask import request, Blueprint, Response

from src.models.user_company import UserCompany
from src.utils.decorators import session, http_handling, is_authorized
from src.models.company import Company

company_bp = Blueprint('company', __name__, url_prefix='/company')


@company_bp.route('', methods=['GET'])
@http_handling
@session
@is_authorized
def get_companies(context):
    companies = Company.get_companies(context)
    return Response(status=200, response=json.dumps(companies))


@company_bp.route('/<int:company_id>', methods=['GET'])
@http_handling
@session
@is_authorized
def get_company_by_id(context, company_id):
    response = Company.get_company_by_id(context, company_id)
    return Response(status=200, response=json.dumps(response))


@company_bp.route('', methods=['POST'])
@http_handling
@session
@is_authorized
def post_company(context, user):
    body = request.json
    Company.create_company(context, body)
    return Response(status=201, response="Resource created")


@company_bp.route('/<int:company_id>', methods=["PUT"])
@http_handling
@session
@is_authorized
def put_company(context, company_id, user):
    body = request.json
    Company.put_company(context, body, company_id)
    return Response(status=200, response="Resource updated with put")


@company_bp.route('/<int:company_id>', methods=["PATCH"])
@http_handling
@session
@is_authorized
def patch_company(context, company_id, user):
    body = request.json
    Company.patch_company(context, body, company_id)
    return Response(status=200, response="Resource updated with patch")


@company_bp.route('/<int:company_id>', methods=['DELETE'])
@http_handling
@session
@is_authorized
def delete_company(context, company_id, user):
    Company.hard_delete_company(context, company_id)
    return Response(status=200, response="Resource deleted")


@company_bp.route('/<int:company_id>/assign', methods=['PATCH'])
@http_handling
@session
@is_authorized
def company_assign(context, company_id, user):
    UserCompany.assign_to_company(context, company_id, request.json)
    return Response(status=200, response="Company assigned to user")


@company_bp.route('/<int:company_id>/users', methods=['GET'])
@http_handling
@session
@is_authorized
def get_companies_with_users(context, company_id, user):
    companies = UserCompany.get_company_users(context, company_id)
    return Response(status=200, response=json.dumps(companies))
