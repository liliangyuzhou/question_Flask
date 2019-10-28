#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : utils.py
# @Author: LILIANG
# @Date  : 2019/10/24
# @Desc  :  test

#学习装饰器函数的写法
from functools import wraps

def my_log(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("hello world!")
        func(*args,**kwargs)
    return wrapper

#run.__name__代表的是run这个函数的名称
@my_log
def run():
    print("123")
print(run.__name__)

@my_log
def run1(a=1,b=2):
    c=a+b
    print(c)


run()
run1()
#1.装饰器的使用是通过@符号放在函数的上面
#2.装饰器中定义的函数，要使用*args和**kwargs的组合，并且这个函数中执行原始函数的时候也要传入*args和**kwargs的组合
#3.需要使用functools.wraps在装饰器的函数上把传进来的这个函数进行一个包裹，这样就不会丢失原来函数的
#__name__属性