from .main import OMDBAPI

def start():
    return OMDBAPI()

config = [{
    'name': 'omdbapi',
    'order': 10,
    'groups': [
        {
            'tab': 'databases',
            'name': 'omdb',
            'label': 'Open Media Database',
            'description': 'Used for all calls to OMDB.',
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
            ],
        },
    ],
}]
