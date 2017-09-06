from _1_split_artical_to_word_list.segment import text_to_segment_list
from text_reader import article_list
from utils.cache import cache

@cache(use_mem=True)
def gen_word_dict_tuple(path):
    '''
    生成词典元组
    :return:
    '''
    word_list = []
    for txt in article_list(path):
        word_list += text_to_segment_list(txt)
    word_dict_tuple = tuple(sorted(set(word_list)))
    return word_dict_tuple

