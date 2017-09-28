import os
from utils.cache import cache
from main.segment import text_to_segment_list


@cache(use_mem=True, use_file=True)
def get_stop_word_list(txt_file_path):
    '''
    获取停用词set
    :param txt_file_path:
    :return:
    '''
    stopwords = []
    with open(txt_file_path, 'r', encoding='utf-8') as txt:
        for line in txt.readlines():
            stopwords.append(text_to_segment_list(line)[0])
    return stopwords