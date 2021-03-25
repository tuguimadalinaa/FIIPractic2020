import json

from flask import request, Blueprint, Response
from src.utils.decorators import session, http_handling
from src.models.company import Company

companies_bp = Blueprint('companies', __name__, url_prefix='/companies')


@companies_bp.route('', methods=['GET'])
@session
def get_companies(context):
    companies = Company.get_companies(context)
    return Response(status=200, response=json.dumps(companies))


@companies_bp.route('/<int:company_id>', methods=['GET'])
@session
def get_company_by_id(context, company_id):
    company = Company.get_company_by_id(context, company_id)
    return Response(status=200, response=json.dumps(company))


@companies_bp.route('', methods=['POST'])
@session
def post_company(context):
    body = request.json
    Company.create_company(context, body)
    return Response(status=201, response="Resource created")


@companies_bp.route('/<int:company_id>', methods=["PUT"])
@session
def put_company(context, company_id):
    body = request.json
    Company.put_company(context, body, company_id)
    return Response(status=200, response="Resource updated completely")


@companies_bp.route('/<int:company_id>', methods=["PATCH"])
@session
def patch_company(context, company_id):
    body = request.json
    Company.patch_company(context, body, company_id)
    return Response(status=200, response="Resource updated partial")


@companies_bp.route('/<int:company_id>', methods=['DELETE'])
@http_handling
@session
def delete_company(context, company_id):
    Company.hard_delete_company(context, company_id)
    return Response(status=200, response="Resource deleted")