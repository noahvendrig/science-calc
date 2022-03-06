import json

f = open('periodic-table.json', encoding='utf-8')
data = json.load(f)
f.close()

print(data)
