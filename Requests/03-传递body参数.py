import requests

base_url="http://httpbin.org"
form_data={'user':'wang','password':'123'}

r=requests.post(base_url+'/post',data=form_data)
#查看状态码
print(r.status_code)
#查看url
print(r.url)
#返回文本信息
print(r.text)
print(r.json)