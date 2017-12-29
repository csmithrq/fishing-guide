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
    regexFishMatch = re.compile('(catfish|rainbow|trout|bass|stripers|largemounth|smallmouth|sturgeon|halibut|rockfish|snapper|cod|bluegill|shad|steelhead|steelies)', re.IGNORECASE)

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


            rgxSep = re.compile("([ ]*\\|){1,}")
            rgx = re.compile("Caught Fish?")
            if "USA Fishing" in reportSource:
                soup = BeautifulSoup(reportFeed.page.text, "lxml")
                for script in soup(["script", "style"]):
                    script.extract()
                text = soup.get_text('|')
                chunks = (line.strip() for line in text.splitlines())
                ## This line takes the chunks (characters or lines), joins them together, replaces the repeated | characters with a single line break and replaces repeated line breaks.
                reportContent = re.sub(rgxSep, "<br>", ' '.join(chunk for chunk in chunks if chunk))

                ## only get non-advertisement info as the report content.
                try:
                    reportContent = reportContent.split("Caught Fish?")[0]
                except IndexError:
                    reportContent = reportContent
                except Exception as error:
                    logging.log(error)
                    raise

                # Get the date from the report content. All USA fishing dates have the format MONTH day #, year #.
                try:
                    matchedDates = re.search(self.regexDateMatch, reportContent)
                    reportDate = datetime.strptime(matchedDates.group(), '%B %d, %Y')
                except Exception as error:
                    logging.log(error)
                    raise

                # Get reported fish from the report content.
                try:
                    matchedFish = re.search(self.regexFishMatch, reportContent)
                except Exception as error:
                    logging.log(error)


                # find date from USA fishing report.
                soup = BeautifulSoup(reportFeed.page.text, "lxml")
                lines = soup.find_all(text=True)
                reportDate = None
                for line in lines:
                    matchedDates = re.search(self.regexDateMatch, line)
                    if matchedDates is not None:
                        reportDate = datetime.strptime(matchedDates.group(), '%B %d, %Y')
                ##textNodes = reportFeed.tree.xpath('//p[@class="MsoNormal" or @class="aolmail_gmail-MsoNormal"]')
                textNodes = reportFeed.tree.xpath('//p')
                reportContent = ""
                hyperlinkTag = re.compile(r'<a.*?>')
                for textNode in textNodes:
                    reportContent += hyperlinkTag.sub('', (etree.tostring(textNode)).decode("utf8"))
                location = reportSource.replace("USA Fishing: ", "")
                fishingReport = FishingReport(location, reportSource, reportDate, reportContent, "")
                reports.append(fishingReport)

            return reports
        except Exception as error:
            logging.error(error)
            raise

    def getReport(self):
        pass