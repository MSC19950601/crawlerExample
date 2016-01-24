from bs4 import BeautifulSoup
import re
import urlparse
class UrlPaser(object):
    def getNewUrls(self,newUrl,soup):
        newUrls = set()
        links = soup.find_all('a', href = re.compile(r"[a-zA-z]+://[^s]*"))
        for link in links:
            getNewUrl = link['href']
            getNewFullUrl = urlparse.urljoin(newUrl,getNewUrl)
            newUrls.add(getNewFullUrl)

        return newUrls

    def getNewData(self,newUrl, soup):
        resData = {}

        resData['url'] = newUrl

        titleNode = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        resData['title'] = titleNode.get_text()

        summaryNode = soup.find('div', class_="lemma-summary")
        resData['summary'] = summaryNode.get_text()

        return resData


    def parse(self, newUrl, urlCont):
        if newUrl is None or urlCont is None:
            return

        soup = BeautifulSoup(urlCont, 'html.parser', from_encoding = 'gbk')
        newUrls = self.getNewUrls(newUrl, soup)
        newData = self.getNewData(newUrl, soup)
        return newUrls,newData