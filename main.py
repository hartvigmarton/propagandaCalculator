import codecs
import urllib.error

#from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
from urllib.request import urlopen

def formatHtml(link):
    url = link

    try:
        page = urlopen(url)
    except (urllib.error.HTTPError,urllib.error.URLError):
        return ""
    htmlBytes = page.read()
    try:
        html = htmlBytes.decode("utf-8")
    except UnicodeDecodeError:
        html = htmlBytes.decode("iso-8859-2")

    htmlSoup = BeautifulSoup(html, "html.parser")

    return htmlSoup

def getlAllLinks(mainSite):
    links = []
    for link in mainSite.find_all('a'):
        links.append(link.get('href'))
    return links

def formatSubDomains(links):
    formatedSubdomains = []
    for link in links:
        formated = formatHtml(link)
        formatedSubdomains.append(formated)
    return formatedSubdomains


def filterLinks(links):
    filteredLinks = []
    for link in links:
        if link != "javascript:;":
            filteredLinks.append(link)
    return filteredLinks

def searchTitles(term,titles):
    for title in titles:
        if title.contains(term):
            print(title)

if __name__ == "__main__":
    term = "Gyurcsány"
    origoMain = formatHtml("https://www.origo.hu/index.html")
    #print(origoMain)
    #title = origoMain.find("title")
    #print(title.string)
    origoLinks = getlAllLinks(origoMain)
    origoFilteredLinks = filterLinks(origoLinks)
    origoSubDomains = formatSubDomains(origoFilteredLinks)
    gyurcsanyCnt = 0
    pageTitles = []
    for subdomain in origoSubDomains:
        title = subdomain.find("title")
        if not pageTitles.__contains__(title):
            pageTitles.append(title)

    for title in pageTitles:
        if str(title).__contains__(term):
            gyurcsanyCnt += 1
    print(gyurcsanyCnt)
"""
origoUrl = "https://www.origo.hu/index.html"
origoPage = urlopen(origoUrl)
htmlBytes = origoPage.read()
html = htmlBytes.decode("utf-8")
origoLinks = []
htmlSoup = BeautifulSoup(html,"html.parser")

for link in htmlSoup.find_all('a'):
    origoLinks.append(link.get('href'))





htmlFile = codecs.open("ORIGO.html", "r", "utf-8")
soup = BeautifulSoup(htmlFile, 'html.parser')
stringSoup = str(soup)
token2 = word_tokenize(stringSoup)

fletoCnt = 0
for gyurcsany in token2:
    if gyurcsany.__contains__("Orbán"):
        fletoCnt += 1
        print(gyurcsany)

print(fletoCnt)
"""
