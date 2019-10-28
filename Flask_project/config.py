#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : config.py
# @Author: LILIANG
# @Date  : 2019/10/22
# @Desc  :  test
import os
DEBUG = True
SECRET_KEY=os.urandom(24)

# dialect+driver://username:password@host:port/database
DIALECT='mysql'
DRIVER='mysqldb'
# DRIVER='pymysql'
# DRIVER='mysqlclient'
USERNAME='root'
PASSWORD='root'
HOST='127.0.0.1'
PORT=3306
DATABASE='Flask_project'
SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,
                                                                USERNAME,PASSWORD,
                                                                HOST,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS=False