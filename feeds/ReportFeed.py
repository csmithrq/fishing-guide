from lxml import html, etree
import logging
import requests

class ReportFeed:

    def __init__(self
                 , url
                 , reportSource
                 ):
        try:
            self.url = url
            self.page = requests.get(url)
            self.text = str(self.page.content)
            self.tree = html.fromstring(self.page.content)
            self.reportSource = reportSource
        except Exception as error:
            logging.error(error)
            raise