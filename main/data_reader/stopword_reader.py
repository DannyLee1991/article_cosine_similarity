from utils.cache import cache
from main.segment import text_to_segment_list
from config import STOPWORDS_FILE_PATH


@cache(use_mem=True, use_file=True)
def get_stop_word_list():
    '''
    获取停用词set
    :param txt_file_path:
    :return:
    '''
    stopwords = []
    with open(STOPWORDS_FILE_PATH, 'r', encoding='utf-8') as txt:
        for line in txt.readlines():
            stopwords.append(text_to_segment_list(line)[0])
    return stopwords