# -*- coding:utf-8 -*-
"""
这部分代码用于加载分词结果
"""

def loadDatadet(infile):
    f = open(infile, 'r', encoding='UTF-8')
    sourceInLine = f.readlines()
    dataset = []
    for line in sourceInLine:
        temp1 = line.strip('\n')
        # temp2=temp1.split()
        if temp1 != '':
            dataset.append(temp1)
    return dataset
