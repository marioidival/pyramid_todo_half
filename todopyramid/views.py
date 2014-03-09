from pyramid.i18n import TranslationStringFactory
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from bson import ObjectId

_ = TranslationStringFactory('todopyramid')

@view_config(route_name='index', renderer='todopyramid:templates/index.jinja2')
def index(request):
    '''Return all TodoList'''
    db = request.db
    todo_lists = list(db.todolist.find())

    return {'todolist': todo_lists}


@view_config(route_name='new', renderer='todopyramid:templates/new.jinja2')
def new(request):

    db = request.db
    todo = {}

    if request.POST:
        form = dict(request.params.items())
        db.todolist.insert(form)
        return HTTPFound('/')
        
    return {'todo': todo}


@view_config(route_name='edit', renderer='todopyramid:templates/new.jinja2')
def edit(request):
    ''' request.matchdict get params passed by routes
    edit/{todo_id}
    '''
    db = request.db
    todo_id = request.matchdict.get('todo_id')

    if request.POST:
        form = dict(request.params.items())
        db.todolist.update({'_id': ObjectId(todo_id)},
                {'$set': form}, upsert=True)
        return HTTPFound('/')

    if todo_id:
        todo = db.todolist.find_one({'_id': ObjectId(todo_id)})
        return {'todo': todo}


@view_config(route_name='delete', renderer='json')
def delete(request):
    ''' request.matchdict get params passed by routes
    delete/{todo_id}
    '''
    db = request.db
    todo_id = request.matchdict.get('todo_id')

    db.todolist.remove({'_id': ObjectId(todo_id)})
    return HTTPFound('/')
