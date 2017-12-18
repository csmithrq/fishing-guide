

class FishingReport:
    def __init__(self
                , location
                , reportSource
                , reportDate
                , reportContent
                , reportedFish
                 ):
        self.location=location
        self.reportSource=reportSource
        self.reportDate=reportDate
        self.reportContent=reportContent
        self.reportedFish=reportedFish


    def __str__(self):
        sb = []
        for key in self.__dict__:
            sb.append("{key}='{value}'".format(key=key, value=self.__dict__[key]))

        return ', '.join(sb)


    def __repr__(self):
        return self.__str__()