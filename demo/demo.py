from main.calc_vect_angle import calc_vct_angle_cos
from main.data_reader.article_reader import gen_article_name_list, get_all_articles, get_article
from main.gen_word_vect import gen_word_dict_list
from main.segment import text_to_segment_list
from main.tfidf import calc_tfidf, calc_all_word_tfidf
from main.word_tfidf_vect import gen_text_tfidf_vct
from utils.log import line, block

line("输出全部文件名列表")
for article_name in gen_article_name_list():
    print(article_name)
block(' ')

line("获取前两篇文章内容")
for article in get_all_articles()[:2]:
    line("我是分割线")
    print(article)
block(' ')

line("获取 文件名为 10 的文章内容")
article_10 = get_article("10")
print(article_10)
block(' ')

line("将文本变为小写后的分词结果（顺序和文本中原始的顺序一致，不去重）")
txt = get_all_articles()[0]
seg_list = text_to_segment_list(txt)
print(seg_list)
block(' ')

line("根据指定目录下的文本，生成总词典list（去重且顺序不变）")
word_dict_list = gen_word_dict_list()
print(word_dict_list)
print("字典长度 %d " % len(word_dict_list))
block(' ')

line("根据指定目录下的文本，生成去停用词后的词典list")
extra_stopwords_word_dict_list = gen_word_dict_list(extra_stopwords=True)
print(extra_stopwords_word_dict_list)
print("去停用词后字典长度 %d " % len(extra_stopwords_word_dict_list))
block(' ')

line("计算'father'这个词，在第一篇文章中的TF-IDF值")
txt = get_all_articles()[0]
father_tfidf = calc_tfidf(txt, 'father')
print(father_tfidf)
block(' ')

line("计算第一篇文章中的所有词的TF-IDF")
txt = get_all_articles()[0]
all_tfidf = calc_all_word_tfidf(txt)
print(all_tfidf)
block(' ')

line("计算指定文章的TF-IDF词向量")
txt = get_all_articles()[0]
tfidf_vct = gen_text_tfidf_vct(txt, extra_stopwords=True)
print(tfidf_vct)
block(' ')

line("计算第一篇和第二篇文章的向量夹角余弦值")
txt_0 = get_all_articles()[0]
txt_1 = get_all_articles()[1]
tfidf_vct_0 = gen_text_tfidf_vct(txt_0, extra_stopwords=True)
tfidf_vct_1 = gen_text_tfidf_vct(txt_1, extra_stopwords=True)
cos = calc_vct_angle_cos(tfidf_vct_0, tfidf_vct_1)
print(cos)
block(' ')
