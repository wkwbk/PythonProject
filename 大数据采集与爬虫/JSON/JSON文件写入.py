import json

dict_content = {"people": [{"name": "Simon", "age": "22"}, {"name": "Tom", "age": "24"}, {"name": "Jack", "age": "26"}]}
with open('json文件.json', 'w') as f:
    json.dump(dict_content, f)
