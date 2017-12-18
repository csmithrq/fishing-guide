from feeds.ReportFeed import ReportFeed
from model.FishingReport import FishingReport
from lxml import html, etree
from bs4 import BeautifulSoup
from datetime import datetime
import logging
import re

class FeedGrabber:

    regexDateMatch = re.compile('(January|February|March|April|May|June|July|August|September|October|November|December).+\d{2},.+\d{4}')
    dateFormat = '%B %d, %Y'

    def __init__(self
                 , conf
                 ):
        pass

    ## Input: takes in whatever is needed to get to the html of a fishing report page.
    ## Output: returns html
    def getHtmlFeed(self, url, reportSource):
        try:
            reportFeed = ReportFeed(url, reportSource)
            ## should add code to verify that an html page is produced.
            return reportFeed
        except Exception as error:
            logging.error(error)
            raise

    ## Input: takes in an html page which contains fishing reports.
    ## Output: returns a list of fishing report objects.
    def getReportsFromHtmlFeed(self, reportFeed):
        reports = []
        try:
            reportSource = reportFeed.reportSource
            if reportSource == 'Lake Chabot Recreation':
                articleNodes = reportFeed.tree.xpath("//article")
                for node in articleNodes:
                    reportDate = datetime.strptime(next(iter(node.xpath('./header/div/div/div[1]/a'))).get("title"), self.dateFormat)
                    reportContent = ""
                    for rawHtml in node.xpath('./div[1]/p'):
                        reportContent += (etree.tostring(rawHtml)).decode("utf8")
                    fishingReport = FishingReport('Lake Chabot', reportSource, reportDate, reportContent, '')
                    reports.append(fishingReport)
                ## do some shit for lake chabot
            if reportSource == 'Delta 1':
                ## do some shit for delta 1
                pass

            if "USA Fishing" in reportSource:
                # find date from USA fishing report.
                soup = BeautifulSoup(reportFeed.page.text, "lxml")
                lines = soup.find_all(text=True)
                for line in lines:
                    matchedDates = re.search(self.regexDateMatch, line)
                    if matchedDates is not None:
                        reportDate = matchedDates[0]
                    else:
                        reportDate = None

                textNodes = reportFeed.tree.xpath('//p[@class="MsoNormal" or @class="aolmail_gmail-MsoNormal"]')
                reportContent = ""
                for textNode in textNodes:
                    reportContent += (etree.tostring(textNode)).decode("utf8")

                location = reportSource.replace("USA Fishing: ", "")
                fishingReport = FishingReport(location, reportSource, reportDate, reportContent, "")
                reports.append(fishingReport)
            return reports
        except Exception as error:
            logging.error(error)
            raise

    def getReport(self):
        pass