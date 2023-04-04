from app.config import web
from app.lang   import lang

def get_lang(self):
    try:
        return lang(web.ctx.env['HTTP_ACCEPT_LANGUAGE'][:2])
    except:
        return lang('en')

