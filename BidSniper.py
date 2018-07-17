import http.cookiejar
import urllib

url = "https://www.ebay.com/signin"
username = "allansattriv@gmail.com"
password ="assass1"

class BidSniper(object):
	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.cj = http.cookiejar.CookieJar()
		self.opener = urllib.request.build_opener(
			urllib.request.HTTPRedirectHandler(),
			urllib.request.HTTPHandler(debuglevel=0),
			urllib.request.HTTPSHandler(debuglevel=0),
			urllib.request.HTTPCookieProcessor(self.cj))
		self.opener.addheaders = [
			('User-agent',('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'))]
		""" obtain cookies """
		print("Obtaining Cookies...\n")
		self.login()
		print("Logging In...\n")
		""" login to ebay """
		response = self.login()
		print("Login Complete \n")
		print(response.getcode())
		print(response.info())
	"""
	Fills CookieJar/Login
	"""
	def login(self):
		login_data = urllib.parse.urlencode({
			'email' : self.username,
			'pass' : self.password,}).encode("utf-8")
		response = self.opener.open(url,data=login_data)
		return response
sniper = BidSniper(username,password)
