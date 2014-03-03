def includeme(config):

    config.add_route('index', '/')
    config.add_route('new', '/new')
    config.add_route('edit', '/edit/{todo_id}')
    config.add_route('delete', '/delete/{todo_id}')

    config.scan('todopyramid.views')
