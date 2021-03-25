from sqlalchemy import Column, String, Integer
from src.adapters.company import CompanyAdapter
from src.models.base import Base
from src.utils.exceptions import Conflict


class Company(Base, CompanyAdapter):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    street = Column(String(200))
    city = Column(String(100))
    country = Column(String(100))

    @classmethod
    def get_companies(cls, context):
        results = context.query(cls).all()
        return cls.to_json(results)

    @classmethod
    def create_company(cls, context, body):
        company = Company()
        company.to_object(body)
        context.add(company)
        context.commit()

    @classmethod
    def put_company(cls, context, body, company_id):
        company = cls.get_company_dbEntity_by_id(context, company_id)
        if not company:
            raise Conflict(404, status="The user you are trying to update does not exist")
        company.to_object(body)
        context.commit()

    @classmethod
    def patch_company(cls, context, body, company_id):
        company = cls.get_company_dbEntity_by_id(context, company_id)
        if not company:
            raise Conflict(404, status="The user you are trying to update does not exist")
        company.to_object(body)
        context.commit()

    @classmethod
    def get_company_dbEntity_by_id(cls, context, company_id):
        return context.query(cls).filter_by(id=company_id).first()

    @classmethod
    def get_company_by_id(cls, context, company_id):
        company = cls.get_company_dbEntity_by_id(context, company_id)
        if not company:
            raise Conflict(404, status="The company you are trying to get does not exist")
        return cls.to_json([company])

    @classmethod
    def hard_delete_company(cls, context, company_id):
        company = cls.get_company_dbEntity_by_id(context, company_id)
        if not company:
            raise Conflict(404, status="The company you are trying to delete does not exist")
        context.delete(company)
        context.commit()
