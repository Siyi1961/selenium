import json

data={'id':1,'name':'wang','password':'6688'}

print("data的类型是：",type(data))
print(data['id'])

json_str=json.dumps(data)
print("json_str的类型是：",type(json_str))
print(json_str)

#json是一个整体的字符串，不能查找其中的键的值
