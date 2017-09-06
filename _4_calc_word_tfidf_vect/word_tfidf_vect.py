import numpy as np
from _2_gen_word_vect.gen_word_vect import gen_word_dict_tuple
from _3_calc_tfidf.tfidf import calc_tfidf

from _1_split_artical_to_word_list.segment import text_to_segment_list
from utils.cache import cache


@cache(use_mem=True, use_file=False)
def get_dict_index(word, path):
    '''
    根据单词 取得在字典中的索引
    :param word:
    :param path: 文本路径
    :return:
    '''
    return gen_word_dict_tuple(path).index(word)


@cache(use_mem=True, use_file=True, print_log=False)
def gen_text_tfidf_vct(text, path):
    '''
    生成文本的TF-IDF向量
    :param text:
    :return:
    '''
    vect = np.zeros(len(gen_word_dict_tuple(path)))
    segms = sorted(set(text_to_segment_list(text)))
    for index, segm in enumerate(segms):
        tfidf = calc_tfidf(text, segm, path=path)
        vect[get_dict_index(segm, path=path)] = tfidf
        # print("[TF-IDF向量生成] %d/%d %s => %s" % (index, len(segms), segm, tfidf))
    return vect
