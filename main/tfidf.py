import math

from main.segment import text_to_segment_list
from main.text_reader import get_all_articles
from utils.cache import cache


@cache(use_mem=True,use_file=True)
def calc_idf(target_word, path):
    '''
    计算idf值
    :param target_word: 目标词
    :return:
    '''
    article_count = 0
    target_article_count = 0
    for txt in get_all_articles(path=path):
        article_count += 1
        segm_list = text_to_segment_list(txt)
        if target_word in segm_list:
            target_article_count += 1

    if target_article_count == 0:
        target_article_count += 1

    return math.log(article_count / target_article_count)


def calc_tf(text, target_word):
    '''
    计算词频
    :param text:
    :param target_word:
    :return:
    '''
    segm_list = text_to_segment_list(text)
    word_count = len(segm_list)
    t_word_count = segm_list.count(target_word)
    return t_word_count / word_count


# @cache(use_mem=True)
def calc_tfidf(text, target_word, path):
    '''
    计算TF-IDF
    :param text:
    :param target_word:
    :return:
    '''
    tf = calc_tf(text, target_word)
    idf = calc_idf(target_word, path=path)
    return tf * idf


def calc_all_word_tfidf(text,path):
    '''
    计算文本的所有的词的TF-IDF 并且按照TF-IDF从大到小的顺序排序
    :param text:
    :return:
    '''
    segm_set = set(text_to_segment_list(text))
    word_tfidf_list = []
    for segm in segm_set:
        tfidf = calc_tfidf(text, segm,path=path)
        word_tfidf_list.append((segm, tfidf))
    return sorted(word_tfidf_list, key=lambda item: item[1], reverse=True)

