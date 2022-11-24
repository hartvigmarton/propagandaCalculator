import codecs
import urllib.error
import streamlit as st
#from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd


#get all the subdomains of a website
def getlAllLinks(mainSite,websiteURL):
    links = []

    for link in mainSite.find_all('a'):
        if str(link.get('href')).startswith("/"):
            title = mainSite.find("title")
            links.append(websiteURL + link.get('href'))
        elif link.get('href') is not None:
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
            

#builds a dictionary with the name of the website as key and a list of links to the subdomains as value
def buildLinkDictionary(formatedWebsites,websiteURLs):
    websiteLinks = {}
    urlIndex = 0
    for website in formatedWebsites:
        websiteTitle = website.find("title")
        try:
            websiteLinks[websiteTitle.string] = getlAllLinks(website,websiteURLs[urlIndex])
        except AttributeError:
            pass
        urlIndex += 1
    return websiteLinks

def formatHtml(link):
    url = link

    try:
        page = Request(
            url=url,
            headers={'User-Agent': 'Mozilla/5.0'})
    except (urllib.error.HTTPError,urllib.error.URLError,ValueError):
        return ""
    htmlBytes = urlopen(page).read()
    try:
        html = htmlBytes.decode("utf-8")
    except UnicodeDecodeError:
        html = htmlBytes.decode("iso-8859-2")

    htmlSoup = BeautifulSoup(html, "html.parser")

    return htmlSoup
def formatWebSites(indexpages):
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
            try:
                if term in pageTitle.string:
                    titlesWithTerm.append(pageTitle.string)
            except (AttributeError,TypeError):
                pass
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

#TODO Magyar Nemzet linkek fixálása, oldalon konfigurálható kulcsszó keresés
if __name__ == "__main__":

    websiteList = ["https://www.origo.hu","https://444.hu","https://telex.hu","https://888.hu"]
    #websiteList = ["https://www.origo.hu","https://444.hu","https://telex.hu/","https://magyarnemzet.hu/","https://888.hu/"]
    websites = formatWebSites(websiteList)
    term = "Orbán"
    terms = "Orbán","Gyurcsány"
    websiteLinks = buildLinkDictionary(websites,websiteList)
    websiteLinks = filterLinks(websiteLinks,websiteList)
    titlesWithTerm = getTitlesWithTerm(term,websiteLinks)
    nrTermPerPage = getNrTermsPerPage(titlesWithTerm)


    st.title("Propaganda Kalkulátor")
    st.markdown("Üdvözlünk a Propaganda kalkulátoron! Ezen az oldalon lemérjük, hogy egyes hírportálok mennyiszer hoznak le bizonyos kifejezéseket. Illusztrációnak\n"
                "jelenleg az \"Orbán\" kifejezés előfordulásait számoltuk meg az Origon és a 444-en")

    selectTerm = st.sidebar.selectbox('Válassz kifejezést',
                                                  terms,
                                                  index=terms.index('Orbán'))
    titlesWithTerm
    nrTermPerPage
    #titlesWithTerm = getTitlesWithTerm(selectTerm, websiteLinks)
    #titlesWithTerm
    #df = pd.DataFrame(nrTermPerPage)
    #df = pd.DataFrame({
     #   'first column': [1, 2, 3, 4],
      #  'second column': [10, 20, 30, 40]
    #})

    #df

    #print(titlesWithTerm)
    #print(nrTermPerPage)


