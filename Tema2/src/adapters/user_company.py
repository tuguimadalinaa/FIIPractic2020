class UserCompanyAdapter:
    @staticmethod
    def to_json_from_list(results):
        return [
            {
                "company_id": user_company.company_id,
                "user_id" : user_company.user_id

            }
            for user_company in results
        ]
