import codecs
import urllib.error
import streamlit
#from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
from urllib.request import urlopen




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


def filterLinks(websiteLinks,websiteList):
    websiteIndex = 0
    for key in websiteLinks:
        filteredLinks = set()
        for link in websiteLinks[key]:
            if websiteList[websiteIndex] in link:
                filteredLinks.add(link)
        websiteIndex += 1
        websiteLinks[key] = filteredLinks
    return websiteLinks


def searchTitles(term,titles):
    for title in titles:
        if title.contains(term):
            print(title)
            


def storeLinks(websites):
    websiteLinks = {}
    for website in websites:
        websiteTitle = website.find("title")
        websiteLinks[websiteTitle.string] = getlAllLinks(website)
    return websiteLinks

def formatHtml(link):
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
def selectWebSites(indexpages):
    formatedIndices = []
    for indexpage in indexpages:
        index = formatHtml(indexpage)
        formatedIndices.append(index)
    return formatedIndices


if __name__ == "__main__":
    websiteList = ["https://www.origo.hu","https://444.hu"]
    websites = selectWebSites(websiteList)
    term = "Gyurcsány"
    websiteLinks = storeLinks(websites)
    websiteLinks = filterLinks(websiteLinks,websiteList)
    print(websiteLinks)

    """"
    for key in websiteLinks:
        #print("the key is " + key)
        #print(websiteLinks[key])
        filteredLinks = set()
        for link in websiteLinks[key]:
            if websiteList[websiteIndex] in link:
                #print ("https://www." + key.lower() + ".hu",link)
                filteredLinks.add(link)
        websiteIndex += 1
        websiteLinks[key] = filteredLinks
        print("filtered links for" + key + ": ")
        for link in websiteLinks[key]:
            print(link)

    #websiteContent = {}
   
    for key in websiteLinks:
        for link in websiteLinks[key]:
            if  "origo" not in link:
                print(link)



    for key in websiteContent:
        print(key)
        print(websiteContent[key])
"""

