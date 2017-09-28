import os
from utils.cache import cache
from config import ARTICLE_PATH

@cache(use_mem=True, use_file=True)
def gen_article_name_list():
    '''
    生成文章名称列表
    :return:
    '''
    listdir = os.listdir(ARTICLE_PATH)
    result = []
    for dir in listdir:
        # 剔除隐藏文件
        if not dir.startswith('.'):
            result.append(dir)
    return result

@cache(use_mem=True,use_file=True)
def get_article_name_by_index(index):
    '''
    根据索引查询文章名
    :param index:
    :return:
    '''
    return gen_article_name_list()[index]

def article_list():
    '''
    得到文章列表
    :return: 文本字符串
    '''
    article_list = gen_article_name_list()
    for file in article_list:
        fp = ARTICLE_PATH + '/' + file
        try:
            with open(fp, 'r', encoding='utf-8') as txt_file:
                yield txt_file.read()
        except UnicodeDecodeError:
            try:
                with open(fp, 'r', encoding='gbk') as txt_file:
                    yield txt_file.read()
            except UnicodeDecodeError:
                os.remove(fp)
                print("remove : [%s]" % fp)

@cache(use_mem=True,use_file=True)
def get_all_articles():
    '''
    获取所有文章列表
    :return:
    '''
    return [i for i in article_list()]

@cache(use_mem=True, use_file=True)
def get_article(file_name):
    '''
    根据文件名获取文章
    :param file_name:
    :return:
    '''
    fp = ARTICLE_PATH + '/' + file_name
    try:
        with open(fp, 'r', encoding='utf-8') as txt_file:
            return txt_file.read()
    except UnicodeDecodeError:
        with open(fp, 'r', encoding='gbk') as txt_file:
            return txt_file.read()
