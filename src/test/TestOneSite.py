from src.main import main as m

# Tests a single site if all the required functionality works with it as intended
index = "https://magyarnemzet.hu"
formatedFile = m.formatHtml(index)
links = m.getlAllLinks(formatedFile)
print(links)
term = "Orbán"
websitelinks = m.buildLinkDictionary(formatedFile)
websitelinks = m.filterLinks(websitelinks,index)
titlesWithTerm = m.getTitlesWithTerm("Orbán",websitelinks)
print(titlesWithTerm)