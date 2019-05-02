import classifyWords
import word2vet
import readWord
from gensim.models import word2vec
import countVec
import numpy as np
import random
from sklearn import svm
from sklearn.externals import joblib
from sklearn import preprocessing
import combineText


# 分词所有的题目文本
classifyWords.sep_words('problemDataSet/BigDataProblem.txt')
classifyWords.sep_words('problemDataSet/C++Problem.txt')
classifyWords.sep_words('problemDataSet/JavaProblem.txt')

# 把所有分词题目文本合并
# combineText.combine_file('/sep_words_result')
# 将合并后的分词题目进行向量学习，得到产生向量的模型
word2vet.get_vec_model('sep_words_result/combine.txt', 'CombineOutModel')
# word2vet.get_vec_model('sep_words_result/BigDataProblemOut.txt', 'BigDataOutModel')
# word2vet.get_vec_model('sep_words_result/C++ProblemOut.txt', 'C++OutModel')
# word2vet.get_vec_model('sep_words_result/JavaProblemOut.txt', 'JavaOutModel')
# 加载向量模型
combine_model = word2vec.Word2Vec.load("OutModel/CombineOutModel.model")
#  model_cPlus = word2vec.Word2Vec.load("OutModel/C++OutModel.model")
#  model_BigData = word2vec.Word2Vec.load("OutModel/BigDataOutModel.model")
#  model_Java = word2vec.Word2Vec.load("OutModel/JavaOutModel.model")
# 加载需要转换为向量的，分词完成的文本
infile_cPlus = readWord.loadDatadet('sep_words_result/C++ProblemOut.txt')
infile_BigData = readWord.loadDatadet('sep_words_result/BigDataProblemOut.txt')
infile_Java = readWord.loadDatadet('sep_words_result/JavaProblemOut.txt')

# 使用向量模型将分词文本转换为向量
resultFeature_cPlus = countVec.get_feature(infile_cPlus, combine_model)
resultFeature_BigData = countVec.get_feature(infile_BigData, combine_model)
resultFeature_Java = countVec.get_feature(infile_Java, combine_model)

# 将C++文本标记为1；  大数据文本标记为2；  Java文本标记为3
label_cPlus = np.ones(np.shape(resultFeature_cPlus)[0])
label_BigData = np.ones(np.shape(resultFeature_BigData)[0]) * 2
label_Java = np.ones(np.shape(resultFeature_Java)[0]) * 3
# print(label_Java)

# 把所有的类型标记整合为一个数组
Y = np.hstack((label_cPlus, label_BigData, label_Java))
# print(Y)
# 把所有向量整合为一个数组
X = resultFeature_cPlus + resultFeature_BigData + resultFeature_Java
# print(np.shape(X))
# print(np.shape(Y))
# 把X和Y结合为一个数组
d = np.column_stack((Y, X))
# 随机打乱数组的顺序
random.shuffle(d)
# 创建一个SVC使用rbf内核，内存为500MB
clf = svm.SVC(kernel='rbf', cache_size=500)
# 提取特征的标签：即第一列
pre = d[:, 0]
# 删除第一列标签作为数据
dataset = np.delete(d, 0, axis=1)
# 进行归一化
X_scaled = preprocessing.scale(dataset)
# print(np.shape(dataset))
# print(pre.reshape(-1,1).astype('int'))
# 进行SVM机器学习
clf.fit(X_scaled,pre.reshape(-1,1).astype('int'))
print(clf.score(X, Y))
print(clf.support_vectors_)
n_Support_vector = clf.n_support_#支持向量个数
print("支持向量个数为： ", n_Support_vector)
# 保存得到的模型
joblib.dump(clf, "ProblemClassify.m")
