import pymongo
import json
import urllib2 as urllib
import authenticateDetails
import nltk

class sentimentAnalysis:
	def __init__(self):
		## tweets is the Database name
		self.conn=pymongo.MongoClient()["tweets"]
		
		## posts is the collection name
		self.posts = self.conn.posts
		self.tweet = {}

	def fetchSamples(self,keyword):
		url = "https://stream.twitter.com/1/statuses/filter.json?track="+keyword
		print url
		parameters = []
		authenticateInstance = authenticateDetails.authenticate()
		response = authenticateInstance.twitterreq(url, "GET", parameters)

		## Insert into MongoDB Database
		for line in response:
			val = json.loads(line.strip())
			self.posts.insert(val)

	#Fetch from MongoDB
	def fetchDB(self):
		tweetText = self.posts.find({},{'text':1, '_id':0})
		return tweetText


if __name__ == '__main__':
	keywordName = 'ipl'
	sentiment = sentimentAnalysis()
	sentiment.fetchSamples(keywordName)

