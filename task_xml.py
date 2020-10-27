import xml.etree.ElementTree as ET
from collections import Counter
import os

file_path = os.path.join(os.getcwd(), '/Users/USER/Desktop/Open and reading file/py-homework-basic-files/3.1.formats.json.xml/newsafr.xml')

def get_top_10(conditional_file_path):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file_path, parser)
    root = tree.getroot()

    descriptions = root.findall("channel/item")
    lst = []
    lst_2 = []
    for i in descriptions:
      i.find("description").text # а так мы получим текст
      lst.append(i.find("description").text)

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

get_top_10(file_path)
