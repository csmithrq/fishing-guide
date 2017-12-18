from abc import ABCMeta, abstractmethod

# Report service provides the necessary methods to find reports and determine whether those reports should be persisted to the database.
# Needs to: find existing reports for a given feed, check for new reports in that feed and persist them if found.
class ReportService(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self
                 , persistenceService
                 ):
        self.self=self
        self.persistenceService = persistenceService

    @abstractmethod
    def findReportDates(self):

        pass
    def processReport(self):
        pass