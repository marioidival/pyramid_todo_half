def includeme(config):

    config.add_route('index', '/')

    config.scan('todopyramid.views')
