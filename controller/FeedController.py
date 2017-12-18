from persistence.MongoPersistence import MongoPersistence
from conf.ApplicationConfig import ApplicationConfig
from feeds.FeedGrabber import FeedGrabber
from datetime import datetime
from pymongo import MongoClient


print("Beginning execution...")

connection = MongoClient('localhost', 27017)
mongo = MongoPersistence(connection)
feedConf = ApplicationConfig().conf["reportFeedUrls"]
for source in feedConf:
    print("Attempting to load reports from source " + source + ', ' + feedConf.get(source))
    url = feedConf.get(source)
    conf = ""
    feedGrabber = FeedGrabber(conf)
    reportFeed = feedGrabber.getHtmlFeed(url, source)
    fishingReports = feedGrabber.getReportsFromHtmlFeed(reportFeed)

    try:
        lastReportDate = mongo.fetchMostRecentReportDate(source)
    except IndexError as error:
        lastReportDate = datetime.strptime("2000/01/01", "%Y/%M/%d")

    for fishingReport in fishingReports:
        if fishingReport.reportDate > lastReportDate:
            print("Wrote fishing report for date " + str(fishingReport.reportDate))
            mongo.writeFishingReport(fishingReport)
        else:
            print("Report date of " + str(fishingReport.reportDate) + " is an old report compared to the last report of " + str(lastReportDate))