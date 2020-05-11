import json

path = 'D:/a/1/s/output.json'

with open(path,encoding='utf_16') as f:
    d = json.load(f)
print(bool(d['results']))
