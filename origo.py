import codecs
import urllib.error

#from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
from urllib.request import urlopen

from webCrawlerInterface import webCrawlerInterface


class origo(webCrawlerInterface):
    def __init__(self,index):
        self.index = index

    def formatHtml(self,link):
        url = link

        try:
            page = urlopen(url)
        except (urllib.error.HTTPError,urllib.error.URLError,ValueError):
            return ""
        htmlBytes = page.read()
        try:
            html = htmlBytes.decode("utf-8")
        except UnicodeDecodeError:
            html = htmlBytes.decode("iso-8859-2")

        htmlSoup = BeautifulSoup(html, "html.parser")

        return htmlSoup

    def getlAllLinks(self,mainSite):
        links = []
        for link in mainSite.find_all('a'):
            links.append(link.get('href'))
        return links

    def formatSubDomains(self,links):
        formatedSubdomains = []
        for link in links:
            formated = self.formatHtml(self, link)
            formatedSubdomains.append(formated)
        return formatedSubdomains


    def filterLinks(self,links):
        filteredLinks = []
        for link in links:
            if link != "javascript:;":
                filteredLinks.append(link)
        return filteredLinks

    def searchTitles(self,term,titles):
        for title in titles:
            if title.contains(term):
                print(title)

    def selectWebSites(self,indexpages):
        formatedIndices = []
        for indexpage in indexpages:
            index = self.formatHtml(self, indexpage)
            formatedIndices.append(index)
        return formatedIndices

    def storeLinks(self,websites):
        websiteLinks = {}
        for website in websites:
            websiteTitle = website.find("title")
            websiteLinks[websiteTitle.string] = self.getlAllLinks(self, website)
        return websiteLinks