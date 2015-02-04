from couchpotato.core.helpers.encoding import tryUrlencode
from couchpotato.core.helpers.variable import getIdentifier
from couchpotato.core.logger import CPLog
from couchpotato.core.media._base.providers.nzb.newznab import Base
from couchpotato.core.media.movie.providers.base import MovieProvider

log = CPLog(__name__)

autoload = 'Newznab'


class Newznab(MovieProvider, Base):

    cat_ids = {
        'en' : [
            ([2020], ['cam', 'ts', 'tc', 'r5', 'scr']),
            ([2030], ['dvdr', 'dvdrip']),
            ([2040], ['720p', '1080p', 'brrip']),
            ([2050], ['brrip']),
            ([2060], ['3d']),
        ],
        'de' : [
            ([2010], ['cam', 'ts', 'tc', 'r5', 'scr', 'dvdr', 'dvdrip', '720p', '1080p', 'brrip', '3d']),
        ],
    }
    cat_backup_id = {'en' : 2000, 'de' : 2000}


    def buildUrl(self, media, host):

        query = tryUrlencode({
            't': 'movie',
            'imdbid': getIdentifier(media).replace('tt', ''),
            'apikey': host['api_key'],
            'extended': 1
        })

        if len(host.get('custom_tag', '')) > 0:
            query = '%s&%s' % (query, host.get('custom_tag'))

        return query
