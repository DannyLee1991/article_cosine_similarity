import re
from utils.cache import cache

@cache(use_mem=True,use_file=True)
def text_to_segment_list(text):
    '''
    分词 将文本转换成单词list
    :param text:
    :return:
    '''
    return re.split('[^a-z]+', text.lower()) if text else []
