from feeds.ReportService import ReportService

class ReportServiceImpl(ReportService):

    def __init__(self
                 , persistenceService
                 ):
        self.self = self
        self.persistenceService = persistenceService

    def checkReport(self):
        self.persistenceService.fet
        pass

    def processReport(self):
        pass