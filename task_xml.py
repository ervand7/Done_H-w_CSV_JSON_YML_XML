import xml.etree.ElementTree as ET
from collections import Counter
import os

file_path = os.path.join(os.getcwd(), 'newsafr.xml')
user_input = int(input('Enter min. count of letters: '))


def split_and_filter_words(min_word_len=user_input):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file_path, parser)
    root = tree.getroot()
    descriptions = root.findall("channel/item")
    list_of_all_descriptions = []
    for i in descriptions:
        list_of_all_descriptions.append(i.find("description").text)
    list_with_words_which_more_min_len = []
    for i in list_of_all_descriptions:
        for word in i.split():
            if len(word) >= min_word_len:
                list_with_words_which_more_min_len.append(word)
    return list_with_words_which_more_min_len


def show_top_10(top_limit=10):
    dict_words_and_its_letters_count = dict(Counter(split_and_filter_words()))
    sorted_dict_words_and_its_letters_count = sorted(dict_words_and_its_letters_count.items(), key=lambda x: x[1],
                                                     reverse=True)
    top_10_list = sorted_dict_words_and_its_letters_count[:top_limit]
    for i in enumerate(top_10_list, 1):
        print(f"На {i[0]} месте находится слово '{i[1][0]}', оно встречается {i[1][1]} раз(а).")


if __name__ == '__main__':
    show_top_10()