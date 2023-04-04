import web, os, sys

app_path     = os.path.dirname(os.path.realpath(sys.argv[0]))
views_path   = app_path + '/app/views'
lang_aviable = ['hu', 'en']
db           = web.database(dbn='sqlite', db='../static/sqlite/part-mozi-03.sqlite3')

render       = web.template.render(views_path, globals=globals(), base='base')

debug        = web.config.debug = False
