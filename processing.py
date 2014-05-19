import fetchAndStore
import sys
import traceback
import nltk
import re
import json
class process:
	def __init__(self):
		self.config = json.load(open('StopWords.json'))
		self.stopwords =  list(set(self.config["stopwords"]))

	def cleanToken(self,each):
		each = re.sub(r'\w+:\/\/.*','',each)
		each = re.sub(r'[#@].*','',each)
		each = re.sub(r'rt','',each)
		each = re.sub(r'[\?\.-]*','',each)
		return each

	def removeNumber(self,each):
		try:
			float(each)
			return False
		except ValueError:
			return True

	def removeStopWords(self,each):
		if each not in self.stopwords:
			return True
		else:
			return False

	def toLowerCase(self,each):
		return each.lower()

	def main(self):
		fetchInstance = fetchAndStore.sentimentAnalysis()
		tweets = fetchInstance.fetchDB()
		for each in tweets:
			try:
				value = each['text']
				#token = nltk.word_tokenize(value)
				token = value.split()
				token = map(self.toLowerCase,token)
				token = map(self.cleanToken,token)
				token = filter(bool,token)
				token = filter(self.removeNumber,token)
				token = filter(self.removeStopWords,token)
				print token
			except NameError:
				print "Exception Raised"



if __name__ == '__main__':
	p = process()
	p.main()