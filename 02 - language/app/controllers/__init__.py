class Controller(object):
    from app.config import web, render
    from app.helpers import get_lang

class ControllerException(Exception):
    pass
