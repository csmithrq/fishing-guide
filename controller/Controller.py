from model import *
from persistence.PersistenceService import PersistenceService
from persistence.MongoPersistence import MongoPersistence
from pymongo import MongoClient
from model.FishingLocation import FishingLocation
from feeds.ReportFeed import ReportFeed
from model.FishingReport import FishingReport
from feeds.FeedGrabber import FeedGrabber
from datetime import datetime

from bs4 import BeautifulSoup
from lxml import html, etree
import json
import pprint
import re


print("Beginning execution...")

connection = MongoClient('localhost', 27017)
mongo = MongoPersistence(connection)

str = "December 20, 2016"
regexDateMatch = re.compile('(January|February|March|April|May|June|July|August|September|October|November|December).+\d{2},.+\d{4}')

dt = datetime.strptime(str, '%B %d, %Y')
print(type(dt))
print(dt)

dt2 = re.search(regexDateMatch,str)
print(type(dt2.group()))
print(dt2.group())

test = mongo.fetchFishingReportIds(5)
print(test)
for id in test:
    print(mongo.fetchFishingReport(id))
#
#conf=""
#feedGrabber = FeedGrabber(conf)
#regexDateMatch = re.compile('(January|February|March|April|May|June|July|August|September|October|November|December).+\d{2},.+\d{4}')
#
#testStr = "December 08, 2017"
#if re.search(regexDateMatch, testStr) is not None:
#    print("found")
#
#
#url = "http://www.usafishing.com/delta.html"
#pageHtml = feedGrabber.getHtmlFeed(#url, "USA Fishing: Delta")
#report = feedGrabber.getReportsFromHtmlFeed(pageHtml)
#print(type(report[0]))
#print(report[0].reportContent)
#
#url = "http://www.usafishing.com/bodega.html"
#pageHtml = feedGrabber.getHtmlFeed(url, "USA Fishing: Bodega")
#report = feedGrabber.getReportsFromHtmlFeed(pageHtml)
#print(type(report[0]))
#print(report[0].reportContent)
#
#url = "http://www.usafishing.com/SFBay.html"
#pageHtml = feedGrabber.getHtmlFeed(url, "USA Fishing: SF Bay")
#report = feedGrabber.getReportsFromHtmlFeed(pageHtml)
#print(type(report[0]))
#print(report[0].reportContent)



#url = "http://www.usafishing.com/delta.html"
#conf = ""
#feedGrabber = FeedGrabber(conf)
#pageHtml = feedGrabber.getHtmlFeed(url, "USA Fishing: Delta")
#print(type(pageHtml.page.text))
#print(type(pageHtml.tree))
#print(type(pageHtml.page))
###textTree = html.tree.xpath('//*[@id="AOLMsgPart_3_bd061f8e-4a07-409c-9ccb-ea739b4aa968"]/div/div/div')
#soup = BeautifulSoup(pageHtml.page.text, "lxml")
#test = pageHtml.tree.xpath('//p[@class="MsoNormal" or @class="aolmail_gmail-MsoNormal"]')
#for line in test:#
#    lineFixed = etree.tostring(line).decode("utf8")
#    print(lineFixed)

#data = soup.findAll(text=True)
#print(list(data))
#print(soup.prettify())//*[@id="table3"]/tbody/tr[2]

#conf = ""
#feedGrabber = FeedGrabber(conf)
#htmlFeed = feedGrabber.getHtmlFeed('http://www.lakechabotrecreation.com/fishing/fishing-conditions/', 'Lake Chabot Recreation')
#reports = feedGrabber.getReportsFromHtmlFeed(htmlFeed)
#print(type(reports))
#for report in reports:
#    print(type(report))
##    print("---------------newreport-----------------")
#    print(report.__str__())


#reportFeed = ReportFeed('http://www.lakechabotrecreation.com/fishing/fishing-conditions/', 'Lake Chabot Recreation')
#test = reportFeed.tree.xpath("//article")
#for node in test:
#    date = node.xpath('//header/div/div/div[1]/a')
#    firstDate = next(iter(date))
#    #print(firstDate.get("title"))
#    #print(type(node))
#    #print(node)
#
#    #print(html.tostring(node))
#    reportContent = node.xpath('//div[1]/p')
#    for report in reportContent:
#        #print(html.tostring(report))
#        print(html.tostring(report))#
#

#connection = MongoClient('localhost', 27017)
#
#
#connection['dev'].drop_collection('fishProfiles')
#connection['dev'].drop_collection('fishingLocations')
#connection['dev'].drop_collection('fishingOptions')
#with open("C:\\Users\\csmith\\Documents\\Repositories\\fish\\fishProfiles.json") as txt:
#    fishProfiles = json.load(txt)
#with open("C:\\Users\\csmith\\Documents\\Repositories\\fish\\fishingLocations.json") as txt:
#    fishin#gLocations = json.load(txt)
#with open("C:\\Users\\csmith\\Documents\\Repositories\\fish\\fishingOptions.json") as txt:
#    fishingOptions = json.load(txt)
#mongo = MongoPersistence(connection)
#mongo.writeFishProfile(fishProfiles)
#mongo.writeFishingLocation(fishingLocations)
#mongo.writeFishingOption(fishingOptions)
#
#
#options1 = mongo.fetchFishingOptionsByMonth(5)
#
#chabot = mongo.fetchFishingLocation("chabot")
#print(type(chabot))
#print("happened")
#for entry in chabot:
#    print(entry.location)
