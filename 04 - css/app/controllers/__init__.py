class Controller(object):
    from app.config import web, render, db
    from app.helpers import get_lang
    from app.models import simple_query

class ControllerException(Exception):
    pass
