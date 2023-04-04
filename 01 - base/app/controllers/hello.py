# -*- coding: utf-8 -*-
from app.controllers import Controller

class world(Controller):
    def GET(self):
        return self.render.hello()
