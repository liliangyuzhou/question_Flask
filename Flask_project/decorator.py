#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : decorator.py
# @Author: LILIANG
# @Date  : 2019/10/24
# @Desc  :  test
from flask import session,redirect,url_for
from functools import wraps
#登陆限制的装饰器
def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs)
        else:
            return  redirect(url_for("login"))

    return  wrapper