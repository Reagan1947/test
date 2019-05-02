# Classify the C++ , Java, and Bigdata_Problem

> This is a little Demo for Using SVM to classify the txt-problem

> This project basically based on a  web page: <https://blog.csdn.net/lily960427/article/details/78168877>

## About the txt-problem

  The txt-problem basically look like below

```
假定 x 一个 逻辑 量 x     x 值 ____   true 1 
设 enum   Printstatus { ready , busy , error }     cout busy   输出 
设 enum   Printstatus { ready 2 , busy , error }   cout busy 输出 
常数 4.205 6.7 E 9 分别 具有 4 _____ ____ 2 位 有效数字 
枚举 类型 中 每个 枚举 值 一个 ____ 枚举 常量 _____ 值 一个 整数 ____ 
常数 100 3.62 数据类型 分别 ____   int   _____   double   
x 5 ,   y 10 ,   计算 y ++ x 表达式 后 x y 值 分别 6 __ 60   
假定 x ch 分别 int 型 char 型 sizeof x sizeof ch 值 分别 __ 4 __ 
假定 x 10 表达式 x 10 20 30 值 __   20   __ 
表达式 sqrt 81 pow 6 , 3 值 分别 9   216 
含 随机 函数 表达式 rand 20 值 0 __   19   __ 区间 
switch 语句 中 每个 语句 标号 含 关键字 case 后面 表达式 常量 
if 语句 中 每个 else 关键字 前面 层次 最 接近 ____   if   ____ 关键字 相配 
语句 标号 使用 C++ 保留字 case defaule 只能 用于   switch   语句 定义 体中 
```

  We have three kinds of txt-Problem, you would able to see in the `problemDataset `dir.Cause I don't have enough time to get the Dataset of the txt-problem. So that it's only a little demo, and don't have good performance of classify.

  However if you are interested in it, you are able to change the txt-problem and make your program.

## Package used

The most important package is:

* word2vec
* jieba
* sklearn

## The end

If you have any problem about the program, contact with me in github

## SVM

SVM used in the programm

```python
clf = svm.SVC(kernel='rbf', cache_size=500)
```

## Label

* C++        get tag '1'
* Bigdata  get tag '2'
* Java         get tag '3'

  