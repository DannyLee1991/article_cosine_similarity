from text_reader import gen_article_name_list, get_all_articles, get_article
from _1_split_artical_to_word_list.segment import text_to_segment_list
from _2_gen_word_vect.gen_word_vect import gen_word_dict_tuple
from _3_calc_tfidf.tfidf import calc_tfidf, calc_all_word_tfidf
from _4_calc_word_tfidf_vect.word_tfidf_vect import gen_text_tfidf_vct
from _5_calc_vct_angle.calc_vect_angle import calc_vct_angle_cos
from config import ARTICLE_PATH
from utils.log import line, block

# 1.输出全部的文件名
line("1.输出全部文件名列表")
for article_name in gen_article_name_list(ARTICLE_PATH):
    print(article_name)
block(' ')

# 2.获取前两篇文章内容
line("2.获取前两篇文章内容")
for article in get_all_articles(ARTICLE_PATH)[:2]:
    line("我是分割线")
    print(article)
block(' ')

# 3.根据指定文件名，获取文章内容
line("3.获取 文件名为 10 的文章内容")
article_10 = get_article("10", ARTICLE_PATH)
print(article_10)
block(' ')

# 4.将文本变为小写后的分词结果（顺序和文本中原始的顺序一致，不去重）
line("4.将文本变为小写后的分词结果（顺序和文本中原始的顺序一致，不去重）")
txt = get_all_articles(ARTICLE_PATH)[0]
seg_list = text_to_segment_list(txt)
print(seg_list)
block(' ')

# 5.根据指定目录下的文本，生成总词典元祖（去重且顺序不变）
line("5.根据指定目录下的文本，生成总词典元祖（去重且顺序不变）")
word_dict_tuple = gen_word_dict_tuple(ARTICLE_PATH)
print(word_dict_tuple)
block(' ')

# 6.计算'father'这个词，在第一篇文章中的TF-IDF值
line("6.计算'father'这个词，在第一篇文章中的TF-IDF值")
txt = get_all_articles(ARTICLE_PATH)[0]
father_tfidf = calc_tfidf(txt, 'father', ARTICLE_PATH)
print(father_tfidf)
block(' ')

# 7.计算第一篇文章中的所有词的TF-IDF
line("7.计算第一篇文章中的所有词的TF-IDF")
txt = get_all_articles(ARTICLE_PATH)[0]
all_tfidf = calc_all_word_tfidf(txt, ARTICLE_PATH)
print(all_tfidf)
block(' ')

# 8.计算指定文章的TF-IDF词向量
line("8.计算指定文章的TF-IDF词向量")
txt = get_all_articles(ARTICLE_PATH)[0]
tfidf_vct = gen_text_tfidf_vct(txt, ARTICLE_PATH)
print(tfidf_vct)
block(' ')


# 9.计算第一篇和第二篇文章的向量夹角余弦值
line("9.计算第一篇和第二篇文章的向量夹角余弦值")
txt_0 = get_all_articles(ARTICLE_PATH)[0]
txt_1 = get_all_articles(ARTICLE_PATH)[1]
tfidf_vct_0 = gen_text_tfidf_vct(txt_0, ARTICLE_PATH)
tfidf_vct_1 = gen_text_tfidf_vct(txt_1, ARTICLE_PATH)
cos = calc_vct_angle_cos(tfidf_vct_0, tfidf_vct_1)
print(cos)
block(' ')