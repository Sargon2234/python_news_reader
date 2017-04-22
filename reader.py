import feedparser
from time import strftime
from Database import Database
import json


class NewsReader:
    def __init__(self, service):
        self.data = Database('localhost', 27017)
        self.connection = self.data.buildConnection('news_services')
        self.service = service

    def finalFlow(self):
        lookingUrl = self.getServiceUrl(self.service)
        preparsedData = self.parseRss(lookingUrl)
        parsedData = self.parseEntries(preparsedData)
        return self.insertData(parsedData)

    def getServiceUrl(self, service):
        with open('./rssUrls.json') as file:
            text = file.read()
            decoded = json.loads(text)
            return decoded[service]

    def parseRss(self, url):
        return feedparser.parse(url)

    def parseEntries(self, entry):
        finalArray = []
        for theme in entry['entries']:
            try:
                neededData = {
                    'title': theme['title'],
                    'info': theme['summary'],
                    'full_info': theme['links'][0]['href'],
                    'date': strftime("%Y-%m-%d %H:%M:%S", theme['published_parsed']),
                    'image': self.getImage(theme),
                    'service': self.service
                }
                finalArray.append(neededData)
            except (ValueError, KeyError, RuntimeError, TypeError, NameError) as e:
                print('Error with', e)
        return finalArray

    def getImage(self, data):
        if (self.service == 'bbc'):
            return data['media_thumbnail'][0]['url']
        else:
            try:
                return data['media_content'][0]['url']
            except KeyError:
                return None

    def insertData(self, data):
        self.data.insertBulk('news', data)


a = NewsReader('ny_times')
a.finalFlow()
