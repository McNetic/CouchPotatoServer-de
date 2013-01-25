from couchpotato.core.helpers.encoding import tryUrlencode
from couchpotato.core.helpers.rss import RSS
from couchpotato.core.logger import CPLog
from couchpotato.core.providers.nzb.base import NZBProvider
from couchpotato.environment import Env
from dateutil.parser import parse
from urllib2 import HTTPError
import time
import traceback

log = CPLog(__name__)


class Kerews(NZBProvider, RSS):

    urls = {
        'download': 'http://kere.ws/api?t=get&id=%s',
        'detail': 'http://kere.ws/api?t=details&id=%s',
        'search': 'http://kere.ws/api?t=movie',
    }

    cat_ids = {
        'en' : [
            ([2000], ['brrip']),
            ([2010], ['dvdr']),
            ([2020], ['dvdrip']),
            ([2030], ['cam', 'ts', 'tc', 'r5', 'scr']),
            ([2040], ['720p', '1080p']),
        ],
        'de' : [
            ([1010], ['cam', 'ts', 'tc', 'r5', 'scr']),
            ([1020], ['dvdrip']),
            ([1030], ['dvdr']),
            ([1050], ['720p']),
            ([1060], ['1080p']),
            ([1070], ['brrip']),
        ]
    }
    cat_backup_id = {'en' : 2000, 'de' : 1070}

    limits_reached = False

    http_time_between_calls = 1 # Seconds

    def _search(self, movie, quality, results):

	cat_id_string = 'cat=%s' % ','.join(['%s' % x for x in self.getCatId(quality.get('identifier'))])
        arguments = tryUrlencode({
            'imdbid': movie['library']['identifier'].replace('tt', ''),
            'apikey': self.conf('api_key'),
            'extended': 1
        })

        url = '%s&%s&%s' % ((self.urls['search']), arguments, cat_id_string)
        nzbs = self.getRSSData(url, cache_timeout = 1800, headers = {'User-Agent': Env.getIdentifier()})

        for nzb in nzbs:

            date = None
            for item in nzb:
                if item.attrib.get('name') == 'usenetdate':
                    date = item.attrib.get('value')
                    break

            if not date:
                date = self.getTextElement(nzb, 'pubDate')

            nzb_id = self.getTextElement(nzb, 'guid').split('/')[-1:].pop()
            name = self.getTextElement(nzb, 'title')

            if not name:
                continue

            results.append({
                'id': nzb_id,
                'name': self.getTextElement(nzb, 'title'),
                'age': self.calculateAge(int(time.mktime(parse(date).timetuple()))),
                'size': int(self.getElement(nzb, 'enclosure').attrib['length']) / 1024 / 1024,
                'url': self.urls['download'] % tryUrlencode(nzb_id) + self.getApiExt(),
                'detail_url': self.urls['detail'] % tryUrlencode(nzb_id),
                'content': self.getTextElement(nzb, 'description'),
            })

    def getApiExt(self):
        return '&apikey=%s' % self.conf('api_key')

    def download(self, url = '', nzb_id = ''):

        # Try again in 3 hours
        if self.limits_reached > time.time() - 10800:
            return 'try_next'

        try:
            data = self.urlopen(url, show_error = False)
            self.limits_reached = False
            return data
        except HTTPError, e:
            if e.code == 503:
                response = e.read().lower()
                if 'maximum api' in response or 'download limit' in response:
                    if not self.limits_reached:
                        log.error('Limit reached for kere.ws')
                    self.limits_reached = time.time()
                    return 'try_next'

            log.error('Failed download from kere.ws: %s', (traceback.format_exc()))

        return 'try_next'
