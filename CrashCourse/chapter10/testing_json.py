import json 

data = '[{"ID":101,"Name":"John","Role":"Member"},' \
       '{"ID":102,"Name":"Kenny","Role":"Editor"}]'
res = json.loads(data)

json_str = json.dumps(res, indent=2)

print(json_str)