class CompanyAdapter:
    @staticmethod
    def to_json_from_list(total, results):
        return {
            "total": total,
            "items": [
                CompanyAdapter.to_json_from_entity(company)
                for company in results
            ]
        }

    @staticmethod
    def to_json_from_entity(company):
        return {
            "id": company.id,
            "name": company.name,
            "street": company.street,
            "city": company.city,
            "country": company.country
        }

    def to_object(self, body):
        for key, value in body.items():
            if hasattr(self, key):
                setattr(self, key, value)
