# -*- coding: utf-8 -*-


from app.config import lang_aviable

def lang(l):
    if l in lang_aviable:
        return getattr(t,l)
    else:
        return getattr(t, 'en')

class t():
    hu = {'hello':'online filmek és sorozatok birodalma'}
    en = {'hello':'empire of online films and series'}
