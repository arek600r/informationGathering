import urllib.request
import urllib.parse
import re

url = 'http://znutakardamonu.pl'
values = {'s':'basics',
          'submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)