from .main import TheMovieDb

def start():
    return TheMovieDb()

config = [{
    'name': 'themoviedb',
    'order': 10,
    'groups': [
        {
            'tab': 'databases',
            'name': 'tmdb',
            'label': 'TheMovieDB',
            'description': 'Used for all calls to TheMovieDB.',
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': True,
                },
                {
                    'name': 'search_enabled',
                    'label': 'Enabled for movie search',
                    'type': 'bool',
                    'default': True,
                },
                {
                    'name': 'info_enabled',
                    'label': 'Enabled for movie info download',
                    'type': 'bool',
                    'default': True,
                },
                {
                    'name': 'api_key',
                    'advanced': True,
                    'default': '9b939aee0aaafc12a65bf448e4af9543',
                    'label': 'Api Key',
                },
            ],
        },
    ],
}]
