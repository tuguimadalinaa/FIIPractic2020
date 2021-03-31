from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint

from src.adapters.user_company import UserCompanyAdapter
from src.models.base import Base
from src.models.company import Company
from src.models.user import User
from src.utils.validators import validate_company_assigned
from src.utils.exceptions import Conflict, HTTPException


class UserCompany(Base, UserCompanyAdapter):
    __tablename__ = 'user_company'
    __table_args__ = (PrimaryKeyConstraint('user_id', 'company_id'),)

    user_id = Column(Integer, ForeignKey("user.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    company_id = Column(Integer, ForeignKey("company.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)

    @classmethod
    def get_company_by_id(cls, context, company_id):
        return context.query(cls).filter_by(id=company_id).first()

    @classmethod
    def add_user_company_entry(cls, context, company_id, user_id):
        uc = UserCompany()
        uc.user_id = user_id
        uc.company_id = company_id
        context.add(uc)
        context.commit()

    @classmethod
    def assign_to_company(cls, context, company_id, body):
        body['company'] = company_id
        validate_company_assigned(body)
        user = User.get_user_by_id(context, body['user_id'])

        if not user:
            raise HTTPException("User or company does not exist", status=404)

        Company.get_company_by_id(context, company_id)

        users_at_same_company = cls.get_company_users(context, company_id)
        if len(users_at_same_company) > 0:
            if body['user_id'] in [user['user_id'] for user in users_at_same_company]:
                raise Conflict("User and company already added", status=400)

        cls.add_user_company_entry(context, company_id, body['user_id'])
        context.commit()

    @classmethod
    def get_company_users(cls, context, company_id):
        results = context.query(cls).filter_by(company_id=company_id).all()
        return cls.to_json(results)
