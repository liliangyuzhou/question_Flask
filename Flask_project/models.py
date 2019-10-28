#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : models.py
# @Author: LILIANG
# @Date  : 2019/10/22
# @Desc  :  test


from exts import db
from datetime import datetime

class User(db.Model):
    __tablename__="user"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    telephone=db.Column(db.String(11),nullable=False)
    username=db.Column(db.String(50),nullable=False)
    password=db.Column(db.String(100),nullable=False)


class Question(db.Model):
    __tablename__='question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title=db.Column(db.String(100),nullable=False)
    content=db.Column(db.Text,nullable=False)
    #now（） 获取的是服务器第一次运行的时间，以后无论创建多少个question，时间都与第一次一模一样
    #now就是每次创建一个模型的时候，都要取当前的时间
    create_time=db.Column(db.DateTime,default=datetime.now)

    #该字段使用外键关联user表的用户id
    author_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    author=db.relationship('User',backref=db.backref('questions'))



class Answer(db.Model):
    __tablename__='answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content=db.Column(db.Text,nullable=False)
    create_time=db.Column(db.DateTime,default=datetime.now)
    question_id=db.Column(db.Integer,db.ForeignKey('question.id'))
    author_id=db.Column(db.Integer,db.ForeignKey('user.id'))

    question=db.relationship('Question',backref=db.backref('answers',order_by=id.desc()))
    author=db.relationship('User',backref=db.backref('answers'))
