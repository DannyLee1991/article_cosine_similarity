import os

# 当前项目目录
project_dir = os.path.dirname(os.path.realpath(__file__))

# 设置缓存目录
CACHE_PATH = project_dir + os.path.sep + "_cache"

# 设置文本目录
ARTICLE_PATH = project_dir + os.path.sep + "_data/article"

# 设置停用词文本目录
STOPWORDS_FILE_PATH = project_dir + os.path.sep + "_data/stopwords/stop_words_eng.txt"

# 是否抽取停用词
IS_EXTRA_STOP_WORD = True
