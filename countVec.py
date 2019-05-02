# -*- coding:utf-8 -*-
"""
这部分代码用于将分词结果转换为词向量的形式
"""
import readWord
from gensim.models import word2vec
import sys
import numpy as np
from sklearn import svm
from sklearn.externals import joblib

sys.setrecursionlimit(1000000)
# model_1 = word2vec.Word2Vec.load("out_c++.model")
# model_2 = word2vec.Word2Vec.load("text8.model")
# infile_1 = readWord.loadDatadet('C++Problem.txt')
# infile_2 = readWord.loadDatadet('out.txt')


def get_feature(lis, model):
    total = []
    for i in lis:
        vec = []
        # lens = len(i.split())
        for j in range(len(i.split())):
            # print(len(i.split()))
            # print(j)
            temp = model[i.split()[j]]
            vec.append(temp)
        # print(np.shape(vec))
        a = np.sum(vec, axis=0)
        # print(np.shape(a))
        # a = a/lens
        total.append(a)
        # print(np.shape(total))
    return total


# def total_vec(model_name,)
# resultFeature_1 = get_feature(infile_1, model_1)
# # print(np.shape(resultFeature_1))
# c = np.ones(206,)
# # java 题目 0表示java
# resultFeature_2 = get_feature(infile_2, model_2)
# java = np.zeros(208,)
# X = resultFeature_1 + resultFeature_2
# Y = np.hstack((c, java))
# clf = svm.SVC()
# clf.fit(X, Y)
# print(clf.score(X, Y))
# print(clf.support_vectors_)
# joblib.dump(clf, "my_model.m")
