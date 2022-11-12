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

def getTitlesWithTerm(term,websiteLinks):
    links = {}
    for key in websiteLinks:
        titlesWithTerm = []
        for link in websiteLinks[key]:
            formatedPage = formatHtml(link)
            pageTitle = formatedPage.find("title")
            #print(term, pageTitle.string)
            if term in pageTitle.string:
                titlesWithTerm.append(pageTitle.string)
        links[key] = titlesWithTerm
            #print(link)
    return links

def printTitlesWithTerm(term,websiteLinks):
    for key in websiteLinks:
        for link in websiteLinks[key]:
            formatedPage = formatHtml(link)
            pageTitle = formatedPage.find("title")
            if term in pageTitle.string:
                print(key, pageTitle.string)


def getNrTermsPerPage(titlesWithTerm):
    nrTermPerPage = {}
    for key in titlesWithTerm:
        nrTerm = 0
        for title in titlesWithTerm[key]:
            nrTerm += 1
        nrTermPerPage[key] = nrTerm
    return nrTermPerPage

if __name__ == "__main__":
    websiteList = ["https://www.origo.hu","https://444.hu"]
    websites = selectWebSites(websiteList)
    term = "Orbán"
    websiteLinks = storeLinks(websites)
    websiteLinks = filterLinks(websiteLinks,websiteList)
    titlesWithTerm = getTitlesWithTerm(term,websiteLinks)
    nrTermPerPage = getNrTermsPerPage(titlesWithTerm)

    #print(titlesWithTerm)
    #print(nrTermPerPage)

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

