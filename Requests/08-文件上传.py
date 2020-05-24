import requests

base_url="http://httpbin.org"
file={'file':open('timeg.png','rb')}
r=requests.get(base_url+'/image/png', files=file)
print(r.status_code)
# print(r.text)

