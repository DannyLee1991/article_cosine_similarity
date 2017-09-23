import os
from utils.cache import cache


@cache(use_mem=True, use_file=True)
def gen_article_name_list(path):
    '''
    生成文章名称列表
    :param path:
    :return:
    '''
    listdir = os.listdir(path)
    result = []
    for dir in listdir:
        # 剔除隐藏文件
        if not dir.startswith('.'):
            result.append(dir)
    return result

@cache(use_mem=True,use_file=True)
def get_article_name_by_index(index, path):
    '''
    根据索引查询文章名
    :param index:
    :param path:
    :return:
    '''
    return gen_article_name_list(path)[index]

def article_list(path):
    '''
    得到文章列表
    :param path:
    :return: 文本字符串
    '''
    article_list = gen_article_name_list(path)
    for file in article_list:
        fp = path + '/' + file
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
def get_all_articles(path):
    '''
    获取所有文章列表
    :param path:
    :return:
    '''
    return [i for i in article_list(path=path)]

@cache(use_mem=True, use_file=True)
def get_article(file_name, path):
    '''
    根据文件名获取文章
    :param file_name:
    :param path:
    :return:
    '''
    fp = path + '/' + file_name
    try:
        with open(fp, 'r', encoding='utf-8') as txt_file:
            return txt_file.read()
    except UnicodeDecodeError:
        with open(fp, 'r', encoding='gbk') as txt_file:
            return txt_file.read()
