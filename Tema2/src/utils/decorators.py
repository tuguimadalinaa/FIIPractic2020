import json
import logging
import functools
from flask import Response
from database_management import get_database_session

logger = logging.getLogger(__name__)


def session(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        context = get_database_session()
        kwargs["context"] = context
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(e)
            raise e
        finally:
            context.close()

    return wrapper


def http_handling(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(e)
            if hasattr(e, 'status'):
                return Response(status=e.args[0], response=json.dumps({"error": e.status}))
            else:
                return Response(status= 500, response=json.dumps({"error": e.args[0]}))
    return wrapper
