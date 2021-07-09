import sys
from urllib import urlencode
from urllib2 import urlopen

username = "ÄãµÄÑ§ºÅ"
upass = "ÄãµÄÃÜÂë"
LOGIN = "http://172.16.254.37/0.htm"
LOGOUT = "http://172.16.254.37/F.htm"

def post(url, data=None):
 if data:
  data = urlencode(data)
 response = urlopen(url, data)
 return response.read()


def login():
 data={}
 data["DDDDD"] = username
 data["upass"] = upass
# data["R1"] = 0
 data["save_me"] =1
# data["v6ip"] = ""
 data["0MKKey"] =123
 post(LOGIN, data)
 pass


def logout():
 post(LOGOUT)

def main(argv):
 if argv[0] in ('login','in','i'):
  login()
 elif argv[0] in ('logout','out','o'):
  logout()
  pass
 pass

if __name__ == '__main__':
 main(sys.argv[0:]);


login()
#logout()