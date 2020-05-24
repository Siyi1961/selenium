import requests

base_url="http://httpbin.org"
param_data={'user':'wang','password':'123'}

r=requests.get(base_url+'/get',params=param_data)
#查看状态码
print(r.status_code)
#查看url
print(r.url)
#返回文本信息
print(r.text)