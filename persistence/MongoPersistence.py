from persistence.PersistenceService import PersistenceService
from model.FishingLocation import FishingLocation
from model.FishProfile import FishProfile
from model.FishingOption import FishingOption
from model.FishingReport import FishingReport
from bson import json_util
from pymongo import MongoClient
import datetime
import re
import json
import pprint

class MongoPersistence(PersistenceService):

    def __init__(self
        , connection
                 ):
        self.connection = connection
        self.database = connection['dev']

    ## Methods for getting and writing data to fishing locations.
    def fetchFishingLocation(self, location=None):
        coll = self.database['fishingLocations']
        entries = []
        fishingLocations = []
        if (location==None):
            entries = list(coll.find())
        else:
            for entry in coll.find({"location": { '$regex' : re.compile(location, re.IGNORECASE)}}):
                entries.append(entry)
        for entry in entries:
            fishingLocation = FishingLocation(
                entry["location"]
                , entry["coordinates"]
                , entry["waterType"]
                , entry["locationType"]
                , entry["fish"]
            )
            fishingLocations.append(fishingLocation)
        return fishingLocations

    def writeFishingLocation(self, data):
        return self.write('fishingLocations', data)


    ## Methods for getting and writing data to fishing options.
    def fetchFishingOptionsByMonth(self, month=None):
        coll = self.database['fishingOptions']
        entries = []
        fishingOptions = []
        if month is None:
            entries = list(coll.find())
        elif int(month) <= 12:
            monthInt = int(month)
            print(monthInt)
            for entry in coll.find({ '$and': [ {"startMonth": {'$lte': monthInt }}, { "endMonth": {'$gte': monthInt}}]}):
                entries.append(entry)

        for entry in entries:
            fishingOption = FishingOption(
            entry["location"]
            , entry["fish"]
            , entry["trigger"]
            , entry["startMonth"]
            , entry["endMonth"]
            , entry["startDate"]
            , entry["endDate"]
            , entry["strategy"]
            )
            fishingOptions.append(fishingOption)

        return fishingOptions

    def writeFishingOption(self, data):
        return self.write('fishingOptions', data)


    ## Methods for getting and writing data to fish profiles.
    def fetchFishProfile(self, fish):
        coll = self.database['fishProfiles']
        entries = []
        fishProfiles = []
        for entry in coll.find({"fish": { '$regex' : re.compile(fish, re.IGNORECASE)}}):
                entries.append(entry)
        for entry in entries:

            fishProfile = FishProfile(
                entry["fish"]
                , entry["fishGroup"]
                , entry["feedingType"]
                , entry["feedingNotes"]
                , entry["sizeByAge"]
                , entry["legality"]
                , entry["additionalNotes"]
            )
            fishProfiles.append(fishProfile)
        return fishProfiles

    def writeFishProfile(self, data):
        return self.write('fishProfiles', data)
        pass


    def writeFishingReport(self, fishingReport):
        #jsonReport = json.loads(vars(fishingReport))
        jsonReport = json_util.loads(json.dumps(vars(fishingReport), default=json_util.default))
        return self.writeOne('fishingReports', jsonReport)

    def fetchFishingReportIds(self, startDate=None, endDate=None, source=None, location=None):
        queryCriteria = []
        if startDate is not None and endDate is not None:
            queryCriteria.append({"reportDate": {'$gte': startDate}})
            queryCriteria.append({"reportDate": {'$lte': endDate}})
        if source is not None:
            queryCriteria.append({"reportSource": {'$regex': re.compile(source, re.IGNORECASE)}})
        if location is not None:
            queryCriteria.append({"location": {'$regex': re.compile(location, re.IGNORECASE)}})
        coll = self.database['fishingReports']
        ids = []
        for reportJson in coll.find({'$and': queryCriteria}):
            ids.append(reportJson['_id'])
        return ids

    def fetchFishingReport(self, id):
        try:
            coll = self.database['fishingReports']
            reportJson = coll.find_one({"_id": {'$eq': id}})
            fishingReport = FishingReport(
                reportJson["location"]
                , reportJson["reportSource"]
                , reportJson["reportDate"]
                , reportJson["reportContent"]
                , reportJson["reportedFish"]
            )
            return fishingReport
        except Exception as error:
            print(error)
            raise

    def fetchMostRecentReportDate(self, source):
        coll = self.database['fishingReports']
        reportDate = coll.find().sort([('reportDate', -1)]).limit(1)[0]["reportDate"]
        return reportDate

    ## Helper utilities.
    def write(self, collection, data):
        coll = self.database[collection]
        result = coll.insert_many(data)
        return result.inserted_ids

    ## Helper utilities.
    def writeOne(self, collection, data):
        coll = self.database[collection]
        result = coll.insert_one(data)
        return result.inserted_id
