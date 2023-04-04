# -*- coding: utf-8 -*-
from app.controllers import Controller

class world(Controller):
    def GET(self):
        db_res = self.db.query('select * from movie order by id desc')
        return self.render.hello(db_res, self.get_lang())
