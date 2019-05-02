# -*- coding:utf-8 -*-
"""
这部分用于对原始数据进行分词处理
"""

import jieba


# 创建停用词列表
def stopwords_list():
    stopwords = [line.strip() for line in open('stopList/StopList.txt', encoding='UTF-8').readlines()]
    return stopwords


# 对句子进行中文分词
def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    print("//*正在分词*//")
    sentence_depart = jieba.cut(sentence.strip())
    # 创建一个停用词列表
    stopwords = stopwords_list()
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


def sep_words(file_path):
    # 给出文档路径
    inputs = open(file_path, 'r', encoding='UTF-8')
    total_name = file_path.split("/")[-1]
    ex_name = total_name.split(".")[0]
    out_name = 'sep_words_result/'+ex_name + 'Out.txt'
    outputs = open(out_name, 'w', encoding='UTF-8')
    # 将输出结果写入ou.txt中
    for line in inputs:
        line_seg = seg_depart(line)
        outputs.write(line_seg + '\n')
    outputs.close()
    inputs.close()
    print("//*删除停用词和分词结束*//")
