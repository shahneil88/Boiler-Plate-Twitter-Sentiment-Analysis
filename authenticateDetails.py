import oauth2 as oauth
import urllib2 as urllib


class authenticate:
	def __init__(self):
		self.access_token_key = ""
		self.access_token_secret = ""
		self.consumer_key = ""
		self.consumer_secret = ""
		self.oauth_token    = oauth.Token(key=self.access_token_key, secret=self.access_token_secret)
		self.oauth_consumer = oauth.Consumer(key=self.consumer_key, secret=self.consumer_secret)

		self.signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

		self.http_method = "GET"

		self.http_handler  = urllib.HTTPHandler(debuglevel=0)
		self.https_handler = urllib.HTTPSHandler(debuglevel=0)



	def twitterreq(self,url, method, parameters):

  		req = oauth.Request.from_consumer_and_token(self.oauth_consumer,
                                             token=self.oauth_token,
                                             http_method=self.http_method,
                                             http_url=url,
                                             parameters=parameters)

 		req.sign_request(self.signature_method_hmac_sha1, self.oauth_consumer, self.oauth_token)
  		headers = req.to_header()

		if self.http_method == "POST":
			encoded_post_data = req.to_postdata()
		else:
			encoded_post_data = None
			url = req.to_url()

		opener = urllib.OpenerDirector()
		opener.add_handler(self.http_handler)
		opener.add_handler(self.https_handler)
		response = opener.open(url, encoded_post_data)

		return response

if __name__ == '__main__':
  auth = authenticate()
