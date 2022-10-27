import codecs
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
from urllib.request import urlopen

def formatHtml(link):
    url = link
    page = urlopen(url)
    htmlBytes = page.read()
    try:
        html = htmlBytes.decode("utf-8")
    except UnicodeDecodeError:
        pass
    try:
        htmlSoup = BeautifulSoup(html, "html.parser")
    except UnboundLocalError:
        pass
    return htmlSoup

def getlAllLinks(mainSite):
    links = []
    for link in mainSite.find_all('a'):
        links.append(link.get('href'))
    return links

def formatSubDomains(links):
    prettifiedSubdomains = []
    for link in links:
        prettifiedSite = formatHtml(link)
        prettifiedSubdomains.append(prettifiedSite)
    return prettifiedSubdomains

if __name__ == "__main__":
    origoMain = formatHtml("https://www.origo.hu/index.html")
    origoLinks = getlAllLinks(origoMain)
    origoSubDomains = formatSubDomains(origoLinks)
    for subdomain in origoSubDomains:
        print(subdomain.get_text())

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
