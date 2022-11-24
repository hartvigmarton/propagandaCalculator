from src.main.main import buildLinkDictionary,filterLinks,getTitlesWithTerm,formatWebSites

#Tests all websites with the functionalities
websiteList = ["https://www.origo.hu", "https://444.hu", "https://telex.hu", "https://888.hu","https://magyarnemzet.hu"]
websites = formatWebSites(websiteList)
term = "Orbán"
websiteLinks = buildLinkDictionary(websites,websiteList)
#print(websiteLinks)

#for key in websiteLinks:
   #print(key)
   #print(websiteLinks[key])
websiteLinks = filterLinks(websiteLinks,websiteList)
print(websiteLinks)
titlesWithTerm = getTitlesWithTerm(term,websiteLinks)
print(titlesWithTerm)
