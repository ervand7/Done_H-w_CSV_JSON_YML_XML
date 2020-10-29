import json
from collections import Counter
import os

file_path = os.path.join(os.getcwd(), 'newsafr.json')



def split_and_filter_words(conditional_file_path, min_word_len):
    with open(file_path) as f:
        json_data = json.load(f)
    descriptions = json_data["rss"]["channel"]["items"]
    lst = []
    lst_of_words = []
    for i in descriptions:
        lst.append(f'{i["description"]}')
    for i in lst:
        for word in i.split():
            if len(word) >= min_word_len:
                lst_of_words.append(word)
    return lst_of_words




def show_top_10(conditional_file_path, min_word_len, top_integer):
    a = split_and_filter_words(file_path, min_word_len)

    dct_with_amount = (dict(Counter(a)))
    sort_dct_with_amount = sorted(dct_with_amount.items(), key=lambda x: x[1], reverse=True)
    lst_words_len_more_6 = ([i for i in sort_dct_with_amount if i[1] >= min_word_len])
    top_10_list = lst_words_len_more_6[:top_integer]
    for i in enumerate(top_10_list, 1):
        print(f"На {i[0]} месте находится слово '{i[1][0]}', оно встречается {i[1][1]} раз(а).")




show_top_10(file_path, 6, 10)