import xml.etree.ElementTree as ET
from collections import Counter
import os
from pprint import pprint

file_path = os.path.join(os.getcwd(), 'newsafr.xml')



def get_top_10(conditional_file_path):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file_path, parser)
    root = tree.getroot()
    descriptions = root.findall("channel/item")
    for i in descriptions:
        pprint(i.find("description").text)
# get_top_10(file_path)



def split_and_filter_words(conditional_file_path, min_integer):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file_path, parser)
    root = tree.getroot()
    descriptions = root.findall("channel/item")
    lst = []
    lst_2 = []
    for i in descriptions:
        i.find("description").text
        lst.append(i.find("description").text)

    for i in lst:
        for word in i.split():
            if len(word) >= min_integer:
                lst_2.append(word)
    pprint(lst_2)
# split_and_filter_words(file_path, 12)



def split_and_filter_words(conditional_file_path, min_integer, top_integer):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file_path, parser)
    root = tree.getroot()
    descriptions = root.findall("channel/item")
    lst = []
    lst_2 = []
    for i in descriptions:
        i.find("description").text  # а так мы получим текст
        lst.append(i.find("description").text)

    for i in lst:
        for word in i.split():
            if len(word) >= min_integer:
                lst_2.append(word)
    dct_with_amount = (dict(Counter(lst_2)))
    sort_dct_with_amount = sorted(dct_with_amount.items(), key=lambda x: x[1], reverse=True)
    lst_more_six = ([i for i in sort_dct_with_amount if i[1] >= min_integer])
    top_10_list = lst_more_six[:top_integer]
    for i in enumerate(top_10_list, 1):
        print(f"На {i[0]} месте находится слово '{i[1][0]}', оно встречается {i[1][1]} раз(а).")
split_and_filter_words(file_path, 6, 10)
