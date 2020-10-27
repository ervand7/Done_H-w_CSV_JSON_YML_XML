import json
from collections import Counter
import os
from pprint import pprint

file_path = os.path.join(os.getcwd(), 'newsafr.json')



def reading_file_path(conditional_file_path):
    with open(file_path) as f:
        json_data = json.load(f)
    descriptions = json_data["rss"]["channel"]["items"]
    pprint(descriptions)
# reading_file_path(file_path)



def split_and_filter_words(conditional_file_path, min_integer):
    with open(file_path) as f:
        json_data = json.load(f)
    descriptions = json_data["rss"]["channel"]["items"]
    lst = []
    lst_2 = []
    for i in descriptions:
        lst.append(f'{i["description"]}')
    for i in lst:
        for word in i.split():
            if len(word) >= min_integer:
                lst_2.append(word)
    pprint(lst_2)
# split_and_filter_words(file_path, 17)



def split_and_filter_words(conditional_file_path, min_integer, top_integer):
    with open(file_path) as f:
        json_data = json.load(f)
    descriptions = json_data["rss"]["channel"]["items"]
    lst = []
    lst_2 = []
    for i in descriptions:
        lst.append(f'{i["description"]}')
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