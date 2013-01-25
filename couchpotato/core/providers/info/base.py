from couchpotato.core.providers.base import Provider


class MovieProvider(Provider):
    type = 'movie'

    def isSearchEnabled(self):
        return self.isEnabled() and self.conf('search_enabled')

    def isSearchDisabled(self):
        return not self.isSearchEnabled()

    def isInfoEnabled(self):
        return self.isEnabled() and self.conf('info_enabled')

    def isInfoDisabled(self):
        return not self.isInfoEnabled()

