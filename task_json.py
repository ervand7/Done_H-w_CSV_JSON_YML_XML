import json
from collections import Counter
import os

file_path = os.path.join(os.getcwd(), '/Users/USER/Desktop/Open and reading file/py-homework-basic-files/3.1.formats.json.xml/newsafr.json')
with open(file_path) as f:
    json_data = json.load(f)
descriptions = json_data["rss"]["channel"]["items"]

lst = []
lst_2 = []
for i in descriptions:
    lst.append(f'{i["description"]}')

for i in lst:
    for s in i.split():
        if len(s) >= 6:
            lst_2.append(s)

d_1 = (dict(Counter(lst_2)))
d_2 = sorted(d_1.items(), key=lambda x: x[1], reverse=True)
d_3 = ([i for i in d_2 if i[1] >= 6])
d_4 = d_3[:10]
for i in enumerate(d_4, 1):
    print(f"На {i[0]} месте находится слово '{i[1][0]}', оно встречается {i[1][1]} раз(а).")