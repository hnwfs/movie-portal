import web, os, sys

app_path     = os.path.dirname(os.path.realpath(sys.argv[0]))
views_path   = app_path + '/app/views'
lang_aviable = ['hu', 'en']

render       = web.template.render(views_path, globals=globals(), base='base')

debug        = web.config.debug = False
