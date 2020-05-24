import requests

base_url="http://httpbin.org"

r=requests.get(base_url+'/get')
print(r.status_code)

r=requests.post(base_url+'/post')
print(r.status_code)

r=requests.put(base_url+'/put')
print(r.status_code)

r=requests.delete(base_url+'/delete')
print(r.status_code)