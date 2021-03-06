from main.calc_vect_angle import calc_vct_angle_cos
from main.data_reader.article_reader import get_article_name_by_index, get_all_articles
from main.word_tfidf_vect import gen_text_tfidf_vct
from utils.cache import cache


@cache(print_log=False)
def calc_all_article_cos():
    '''
    计算所有的文章的相对向量夹角cos
    :return: (文章1索引,文章2索引,相对cos)
    '''
    all_article = get_all_articles()

    result_list = []
    for index, atc_txt_1 in enumerate(all_article):
        print("总体进度 %d/%d" % (index, len(all_article)))

        vct_1 = gen_text_tfidf_vct(atc_txt_1)

        id_1 = all_article.index(atc_txt_1)
        atc_name_1 = get_article_name_by_index(id_1)

        for sub_index, atc_txt_2 in enumerate(all_article):
            print("总体进度 %d/%d  子进度 %d/%d" % (index, len(all_article), sub_index, len(all_article)))
            if atc_txt_1 == atc_txt_2:
                continue
            else:

                vct_2 = gen_text_tfidf_vct(atc_txt_2)

                cos = calc_vct_angle_cos(vct_1, vct_2)

                id_2 = all_article.index(atc_txt_2)
                atc_name_2 = get_article_name_by_index(id_2)

                result_list.append((atc_name_1, atc_name_2, cos))

    return result_list


all_art_cos_tp = calc_all_article_cos()

print('--------')
print("总排序 --> ")
# 获取文章相似度排名前20条记录
print(sorted(all_art_cos_tp, key=lambda item: item[2], reverse=True)[:20])
