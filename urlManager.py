class UrlManager(object):
    def __init__(self):
        self.newUrls = set()
        self.oldUrls = set()

    def addNewUrl(self, urlMsc):
         if urlMsc is None:
             return
         if urlMsc not in self.newUrls and urlMsc not in self.oldUrls:
            self.newUrls.add(urlMsc)

    def hasNewUrl(self):
        return len(self.newUrls) != 0

    def getNewUrl(self):
        newUrl = self.newUrls.pop()
        self.oldUrls.add(newUrl)
        return newUrl

    def addNewUrls(self, UrlMscS):
        if UrlMscS is None or len(UrlMscS) == 0:
            return
        for url in UrlMscS:
            self.addNewUrl(url)
