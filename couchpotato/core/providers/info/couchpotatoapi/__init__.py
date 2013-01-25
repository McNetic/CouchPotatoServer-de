from .main import CouchPotatoApi

def start():
    return CouchPotatoApi()

config = [{
    'name': 'couchpotatoapi',
    'order': 10,
    'groups': [
        {
            'tab': 'databases',
            'name': 'couchpotatoapi',
            'label': 'CouchPotato API',
            'description': 'Used for all calls to CouchPotato API.',
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
