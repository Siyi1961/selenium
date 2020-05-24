import requests

base_url="http://httpbin.org"
cookie={'user':'wang'}
r=requests.get(base_url+'/cookies', cookies=cookie,timeout=0.01)
print(r.status_code)
print(r.text)