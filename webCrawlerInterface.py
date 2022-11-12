from abc import ABC, abstractmethod

class webCrawlerInterface(ABC):

    @abstractmethod
    def formatHtml(self, links):
        pass

    @abstractmethod
    def getlAllLinks(self, full_file_name) :
        pass

    @abstractmethod
    def formatSubDomains(self,links):
        pass

    @abstractmethod
    def filterLinks(self,links):
        pass

    @abstractmethod
    def searchTitles(self,term, titles):
        pass

    @abstractmethod
    def selectWebSites(self,indexpages):
        pass

    @abstractmethod
    def storeLinks(self,websites):
        pass

