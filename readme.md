News Reader
==============
Upload latest news to database.
##Configurations:<br>
Python v.**3.6.1**,
pip **9.0.1**
```
# install pymongo, feedparser
python3 -m pip install pymongo
python3 -m pip install feedparser

# for localhost you should start mongo with typing in console
mongod
# this will start default localhost connection for mongo at 27017 port
# Don't use default port on production!
# Add unique index to collection for title and date
# Access mongo shell. Type in console:
mongo
> use news_services
> db.news.createIndex({title:1, date: 1}, {unique: true})
```
Then you can just add urls for rss in rssUrls.json file
and run reader.py with your service.
<br><br>
##Example
```
python3 reader.py
```
Which will load latest news to mongo collection 'news_services'.
<br><br>
To test:
```
# In mongo shell
db.news.find().limit(1).pretty()
# which will return something like this:
{
	"_id" : ObjectId("58fbd1496cd33601b2810286"),
	"title" : "Trump Reaches Beyond West Wing for Counsel",
	"info" : "",
	"full_info" : "https://www.nytimes.com/2017/04/22/us/politics/donald-trump-white-house.html?partner=rss&emc=rss",
	"date" : "2017-04-22 19:35:47",
	"image" : "https://static01.nyt.com/images/2017/04/23/us/23trumptalk3-sub-master/23trumptalk3-sub-master-moth-v2.jpg",
	"service" : "ny_times"
}
```