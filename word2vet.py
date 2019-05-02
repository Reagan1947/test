# -*- coding:utf-8 -*-
"""
这部分代码用于训练生成词向量的模型
"""
import logging
from gensim.models import word2vec


def get_vec_model(out_file_path, model_name):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # 以每一行为一个句子读取txt文件
    sentences = word2vec.LineSentence(out_file_path)
    model = word2vec.Word2Vec(sentences, hs=1, min_count=1, window=3, size=100)
    model_total_name = 'OutModel/' + model_name + '.model'
    model.save(model_total_name)
