# -*- coding: utf-8 -*-

def simple_query(self):
    if self.get_lang()['l'] == 'hu':
        return self.db.query('select id, tmdb, m_title from movie order by id desc')
    else:
        return self.db.query('select id, tmdb, e_title as m_title from movie order by id desc')
