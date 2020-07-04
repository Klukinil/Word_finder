import json
import xml.etree.ElementTree as ET

def file_opener(file_name):

    if '.json' in file_name:
        with open(file_name, encoding='utf-8') as f:
            json_data = json.load(f)
        items_list = json_data["rss"]["channel"]["items"]
        news_list = [item['description'].split() for item in items_list]
        return news_list

    elif '.xml' in file_name:
        parser = ET.XMLParser(encoding="utf-8")
        tree = ET.parse(file_name, parser)
        root = tree.getroot()
        items_list = root.findall("channel/item/description")
        news_list = [description.text.split() for description in items_list]
        return news_list


def words_finder(word_length, top):

    words = news[0]
    for i in range(1, len(news)):
        words += news[i]
    long_words = [word.lower() for word in words if len(word) >= word_length]
    long_words.sort()

    words_count = dict()
    for long_word in long_words:
        words_count[long_word] = long_words.count(long_word)
    value_count = [value for value in words_count.values()]
    value_count.sort(reverse=True)
    top_value = value_count[0:top]

    top_word = dict()
    for key,value in words_count.items():
        if value in top_value:
          top_word[key] = value

    print(top_word)

news = file_opener("newsafr.xml")
words_finder(6, 10)
news = file_opener("newsafr.json")
words_finder(6, 10)