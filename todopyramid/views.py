from pyramid.i18n import TranslationStringFactory
from pyramid.view import view_config

_ = TranslationStringFactory('todopyramid')

@view_config(route_name='index', renderer='todopyramid:templates/index.jinja2')
def index(request):
    db = request.db
    return {'cursor': db}
