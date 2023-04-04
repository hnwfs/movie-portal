#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

from app.config import debug
from app.config import routes

App = web.application(routes.urls, globals())

if __name__ == "__main__":
    App.run()
else:
    application = App.wsgifunc()
