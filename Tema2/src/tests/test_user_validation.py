from src.utils.validators import validate_email


class TestUserValidation:

    def test_user_email_validation_succes(self):
        email = "madalina.tugui@gmail.com"
        valid = True
        try:
            validate_email(email)
        except Exception:
            valid = False
        assert valid

    def test_user_email_validation_failed(self):
        email = "madalina.tuguigmail.com"
        valid = True
        try:
            validate_email(email)
        except Exception:
            valid = False
        assert not valid

