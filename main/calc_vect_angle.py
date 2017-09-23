# 计算向量夹角
import numpy as np
from utils.cache import cache

@cache(use_mem=True,use_file=True)
def calc_vct_angle_cos(vct_1, vct_2):
    '''
    向量夹角cos计算
    :param vct_1:
    :param vct_2:
    :return:
    '''
    dot = np.dot(vct_1, vct_2)
    Lx = np.sqrt(np.dot(vct_1, vct_1))
    Ly = np.sqrt(np.dot(vct_2, vct_2))
    return dot / (Lx * Ly)
