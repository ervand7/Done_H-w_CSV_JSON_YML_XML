import json
from collections import Counter
import os

file_path = os.path.join(os.getcwd(), 'newsafr.json')


def split_and_filter_words(min_word_len=6):
    with open(file_path) as f:
        json_data = json.load(f)
    description = json_data["rss"]["channel"]["items"]
    list_of_all_descriptions = []
    for i in description:
        list_of_all_descriptions.append(f'{i["description"]}')
    list_with_words_which_more_min_len = []
    for i in list_of_all_descriptions:
        for word in i.split():
            if len(word) >= min_word_len:
                list_with_words_which_more_min_len.append(word)
    return list_with_words_which_more_min_len


def show_top(top_limit=10):
    dict_words_and_its_letters_count = dict(Counter(split_and_filter_words()))
    sorted_dict_words_and_its_letters_count = sorted(dict_words_and_its_letters_count.items(), key=lambda x: x[1],
                                                     reverse=True)
    top_10_list = sorted_dict_words_and_its_letters_count[:top_limit]
    for i in enumerate(top_10_list, 1):
        print(f"На {i[0]} месте находится слово '{i[1][0]}', оно встречается {i[1][1]} раз(а).")


if __name__ == '__main__':
    split_and_filter_words()
    show_top()
