from pyramid.config import Configurator
from pyramid.events import NewRequest
from pyramid_jinja2 import renderer_factory
from todopyramid.models import get_root

import pymongo

connection = pymongo.MongoClient()

def connect(request):
    """Get name of database and return cursor Mongo
    """
    doc_name = request.registry.settings['mongodb.db_name']
    db = connection[doc_name]
    return db

def add_db_to_request(event):
    """Add "db" for each New Request in application
    db = request.db
    """
    event.request.set_property(connect, 'db', reify=True)

def main(global_config, **settings):
    """ This function returns a WSGI application.

    It is usually called by the PasteDeploy framework during
    ``paster serve``.
    """
    settings = dict(settings)
    settings.setdefault('jinja2.i18n.domain', 'todopyramid')

    config = Configurator(root_factory=get_root, settings=settings)
    #Set db to requests
    config.add_subscriber(add_db_to_request, NewRequest)
    config.add_translation_dirs('locale/')
    config.include('pyramid_jinja2')
    # change extension of jinja2
    #config.add_renderer('.html', renderer_factory)

    config.add_static_view('static', 'static')
    config.include('todopyramid.routes')

    return config.make_wsgi_app()
