import output
import urlDownload
import urlManager
import urlParser


class SpiderMain(object):
    def __init__(self):
        self.urls = urlManager.UrlManager()
        self.downloader = urlDownload.UrlDownload()
        self.parser = urlParser.UrlPaser()
        self.output = output.Output()


    def craw(self, rootUrl):
        count = 1
        self.urls.addNewUrl(rootUrl)
        while self.urls.hasNewUrl():
            try:
                newUrl = self.urls.getNewUrl()
                print 'craw %d : %s' % (count, newUrl)
                urlCont = self.downloader.download(newUrl)
                newUrls, newData = self.parser.parse(newUrl, urlCont)
                self.urls.addNewUrls(newUrls)
                self.output.collectData(newData)
                if count == 1000:
                    break
                count = count + 1
            except:
                print 'craw fialed!'

        self.output.outputUrl()

if __name__ == '__main__':
    rootUrl = "http://baike.baidu.com/view/2655336.htm"
    objSpider = SpiderMain()
    objSpider.craw(rootUrl)