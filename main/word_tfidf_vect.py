import numpy as np
from main.gen_word_vect import gen_word_dict_list
from main.segment import text_to_segment_list
from main.data_reader.stopword_reader import get_stop_word_list

from main.tfidf import calc_tfidf
from utils.cache import cache


@cache(use_mem=True, use_file=False)
def get_dict_index(word):
    '''
    根据单词 取得在字典中的索引
    :param word:
    :return:
    '''
    return gen_word_dict_list().index(word)


@cache(use_mem=True, use_file=True, print_log=False)
def gen_text_tfidf_vct(text):
    '''
    生成文本的TF-IDF向量
    :param text:
    :return:
    '''
    word_dict = gen_word_dict_list()
    vect = np.zeros(len(word_dict))
    segms = set(text_to_segment_list(text))

    # 剔除停用词
    segms -= set(get_stop_word_list())

    for index, segm in enumerate(sorted(segms)):
        tfidf = calc_tfidf(text, segm)
        vect[get_dict_index(segm)] = tfidf
        # print("[TF-IDF向量生成] %d/%d %s => %s" % (index, len(segms), segm, tfidf))
    return vect
