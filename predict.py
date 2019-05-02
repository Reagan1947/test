# -*- coding:utf-8 -*-
"""
这部分用于对题目进行分类
"""

import readWord
import countVec
from sklearn.externals import joblib
from gensim.models import word2vec
from sklearn import preprocessing

# classifyWords.sep_words('problemDataSet/BigDataProblem.txt')
# 分词结果转换为向量
infile_test = readWord.loadDatadet('sep_words_result/testOut.txt')
# print(infile_test)
combine_model = word2vec.Word2Vec.load("OutModel/CombineOutModel.model")
# 得到向量文本
resultFeature_test = countVec.get_feature(infile_test, combine_model)
# print(resultFeature_test)
X_scaled = preprocessing.scale(resultFeature_test)
clf = joblib.load('ProblemClassify.m')
# 进行预测
predict = clf.predict(X_scaled)
print(predict)

