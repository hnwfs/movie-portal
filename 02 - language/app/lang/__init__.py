# -*- coding: utf-8 -*-


from app.config import lang_aviable

def lang(l):
    if l in lang_aviable:
        return getattr(t,l)
    else:
        return getattr(t, 'en')

class t():
    hu = {'hello':'Üdvözöllek a webpy-ben írt MVC keretrendszerből!'}
    en = {'hello':'Welcome to the MVC framework written using webpy!'}
