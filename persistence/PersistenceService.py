from abc import ABCMeta, abstractmethod

class PersistenceService(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self
                 , connection
                 ):
        self.connection = connection

    @abstractmethod
    def fetchFishingLocation(self, location=None):
        pass
    @abstractmethod
    def writeFishingLocation(self, data):
        pass

    @abstractmethod
    def fetchFishingOptionsByMonth(self, month=None):
        pass
    @abstractmethod
    def writeFishingOption(self, data):
        pass

    @abstractmethod
    def fetchFishProfile(self):
        pass
    @abstractmethod
    def writeFishProfile(self, data):
        pass

    @abstractmethod
    def fetchFishingReportIds(self, startDate, endDate, source, location, limit):
        pass
    @abstractmethod
    def fetchFishingReport(self, id):
        pass
    @abstractmethod
    def fetchMostRecentReportDate(self, source):
        pass


    @abstractmethod
    def writeFishingReport(self):
        pass