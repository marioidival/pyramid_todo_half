def includeme(config):
    '''This method provide an way for you add routes separately, but if you
    want, can add all in __init__.py

    config.scan talks for includeme, verify __file__ for get route_names
    index, new, edit, delete
    '''

    config.add_route('index', '/')
    config.add_route('new', '/new')
    config.add_route('edit', '/edit/{todo_id}')
    config.add_route('delete', '/delete/{todo_id}')

    config.scan('todopyramid.views')
