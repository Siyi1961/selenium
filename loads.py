import json

json_str='{"id":1,"name":"wang","password":"6688"}'

print(type(json_str))

data=json.loads(json_str)
print(type(data))

print(data['name'])