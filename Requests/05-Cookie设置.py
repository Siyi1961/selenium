import requests

base_url="http://httpbin.org"
cookie={'user':'wang'}
# header={'User-Agent':'Mozilla/5.0'}

# r=requests.get(base_url+'/cookies',cookies=cookie)
#查看状态码
# print(r.status_code)
#查看url
# print(r.url)
#返回文本信息
# print(r.text)
# print(r.json)

'''
会话控制，session对象存储特定用户会话属性及配置信息
'''
s=requests.Session()
#设置cookie
r=s.get(base_url+'/cookies/set/wang/123')
print(r.text)

#获取cookie
r=s.get(base_url+'/cookies')
print(r.text)