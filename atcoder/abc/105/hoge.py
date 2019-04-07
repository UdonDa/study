import urllib.request
_input = '眠い'


url = 'http://challenge-server.code-check.io/api/hash?q={}'.format(_input)
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as res:
    body = res.read()
