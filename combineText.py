# coding=utf-8
import os
# 获取目标文件夹的路径


def combine_file(pack_name):
    filedir = os.getcwd() + pack_name
    # 获取当前文件夹中的文件名称列表
    filenames=os.listdir(filedir)
    # 打开当前目录下的result.txt文件，如果没有则创建
    f = open('sep_words_result/combine.txt', 'w', encoding='UTF-8')
    # 先遍历文件名
    for filename in filenames:
        filepath = filedir+'/'+filename
        # 遍历单个文件，读取行数
        for line in open(filepath, encoding='UTF-8'):
            f.writelines(line)
            # f.write('\n')
    # 关闭文件
    f.close()