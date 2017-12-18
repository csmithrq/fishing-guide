class ApplicationConfig:

        def __init__(self
                     ):
            self.self = self
            self.conf =  {
                "mongo": {
                    "host": "localhost"
                    , "user": ""
                    , "password": ""
                    , "db": "dev"
                    , "port": "27017"
                },
                "reportFeedUrls": {
                    "Lake Chabot Recreation": "http://www.lakechabotrecreation.com/fishing/fishing-conditions/"
                    #, "USA Fishing: SF Bay": "http://www.usafishing.com/SFBay.html"
                    #, "USA Fishing: Delta": "http://www.usafishing.com/delta.html"
                    #, "USA Fishing: Lakes": "http://www.usafishing.com/lakefish.html"
                    #, "USA Fishing: Bodega Bay": "http://www.usafishing.com/bodega.html"
                    #, "USA Fishing: Russian River": "http://www.usafishing.com/russian.html"
                    #, "USA Fishing: Sacramento River": "http://www.usafishing.com/sac.html"
                    #, "USA Fishing: American River": "http://www.usafishing.com/american.html"
                }
            }
