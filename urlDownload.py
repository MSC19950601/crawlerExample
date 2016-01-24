import urllib2


class UrlDownload(object):
    def download(self, newUrl):
        if newUrl is None:
            return None

        response = urllib2.urlopen(newUrl)

        if response.getcode() != 200:
            return None

        return response.read()

