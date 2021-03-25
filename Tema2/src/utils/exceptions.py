
class Conflict(Exception):

    def __init__(self, *args, **kwargs):
        self.status = kwargs["status"]
        print(self.status)
        del kwargs["status"]
        super().__init__(*args, **kwargs)

    def to_dict(self):
        response = dict()
        response['error'] = self.status
        return response


class InvalidBody(Exception):
    def __init__(self, *args, **kwargs):
        self.status = kwargs["status"]
        del kwargs["status"]
        super().__init__(*args, **kwargs)
