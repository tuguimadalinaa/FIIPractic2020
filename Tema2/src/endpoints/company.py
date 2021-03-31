import json

from flask import request, Blueprint, Response

from src.models.user_company import UserCompany
from src.utils.decorators import session, http_handling, is_authorized, is_admin, action_log
from src.models.company import Company

company_bp = Blueprint('companies', __name__, url_prefix='/companies')


@company_bp.route('', methods=['GET'])
@http_handling
@session
@is_authorized
def get_companies(context, user):
    companies = Company.get_companies(context)
    return Response(status=200, response=json.dumps(companies), content_type='application/json')


@company_bp.route('/<int:company_id>', methods=['GET'])
@http_handling
@session
@is_authorized
def get_company_by_id(context, company_id, user):
    response = Company.get_company_by_id(context, company_id)
    return Response(status=200, response=json.dumps(response), content_type='application/json')


@company_bp.route('', methods=['POST'])
@http_handling
@session
@is_authorized
@is_admin
@action_log(action="POST COMPANY")
def post_company(context, user):
    body = request.json
    Company.create_company(context, body)
    return Response(status=201, response=json.dumps({"message": "Resource created"}), content_type='application/json')


@company_bp.route('/<int:company_id>', methods=["PUT"])
@http_handling
@session
@is_authorized
@is_admin
@action_log(action="PUT COMPANY")
def put_company(context, company_id, user):
    body = request.json
    Company.put_company(context, body, company_id)
    return Response(status=200, response=json.dumps({"message": "Resource updated with put"}),
                    content_type='application/json')


@company_bp.route('/<int:company_id>', methods=["PATCH"])
@http_handling
@session
@is_authorized
@is_admin
@action_log(action="PATCH COMPANY")
def patch_company(context, company_id, user):
    body = request.json
    Company.patch_company(context, body, company_id)
    return Response(status=200, response=json.dumps({"message": "Resource updated with patch"}),
                    content_type='application/json')


@company_bp.route('/<int:company_id>', methods=['DELETE'])
@http_handling
@session
@is_authorized
@is_admin
@action_log(action="DELETE COMPANY")
def delete_company(context, company_id, user):
    Company.hard_delete_company(context, company_id)
    return Response(status=200, response=json.dumps({"message": "Resource deleted"}), content_type='application/json')


@company_bp.route('/<int:company_id>/assign', methods=['PATCH'])
@http_handling
@session
@is_authorized
@is_admin
@action_log(action="ASSIGN COMPANY")
def company_assign(context, company_id, user):
    UserCompany.assign_to_company(context, company_id, request.json)
    return Response(status=200, response=json.dumps({"message": "Company assigned to user"}),
                    content_type='application/json')


@company_bp.route('/<int:company_id>/users', methods=['GET'])
@http_handling
@session
@is_authorized
def get_companies_with_users(context, company_id, user):
    companies = UserCompany.get_company_users(context, company_id)
    return Response(status=200, response=json.dumps(companies), content_type='application/json')
