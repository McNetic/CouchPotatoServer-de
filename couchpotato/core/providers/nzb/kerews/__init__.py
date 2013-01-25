from .main import Kerews

def start():
    return Kerews()

config = [{
    'name': 'kerews',
    'label': 'Kere.ws',
    'groups': [
        {
            'tab': 'searcher',
            'subtab': 'nzb_providers',
            'name': 'kere.ws',
            'description': 'Free provider. See  <a href="http://kere.ws/" target="_blank">Kere.ws</a>',
            'wizard': True,
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                },
                {
                    'name': 'api_key',
                    'default': ',,,',
                    'label': 'Api Key',
                    'description': 'Can be found on your profile page'
                },
            ],
        },
    ],
}]
