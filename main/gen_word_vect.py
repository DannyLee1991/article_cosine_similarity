from main.data_reader.article_reader import article_list
from main.segment import text_to_segment_list
from main.data_reader.stopword_reader import get_stop_word_list
from utils.cache import cache
from config import ARTICLE_PATH, STOPWORDS_FILE_PATH


@cache(use_mem=True)
def gen_word_dict_list(extra_stopwords=False):
    if extra_stopwords:
        stopwords_list = get_stop_word_list(STOPWORDS_FILE_PATH)
        return gen_extra_stopwords_word_dict_list(stopwords_list)
    else:
        return origin_word_dict_list()


def origin_word_dict_list():
    '''
    生成词典list
    :return:
    '''
    word_list = []
    for txt in article_list(ARTICLE_PATH):
        word_list += text_to_segment_list(txt)
    return sorted(set(word_list))


@cache(use_mem=True)
def gen_extra_stopwords_word_dict_list(stopwords_list):
    '''
    生成去停用词之后的词典
    :param stopwords_list:
    :return:
    '''
    word_dict_list = origin_word_dict_list()
    return sorted(set(word_dict_list) - set(stopwords_list))
