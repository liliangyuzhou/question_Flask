#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : manage.py
# @Author: LILIANG
# @Date  : 2019/10/22
# @Desc  :  test
"""
1.python manage.py db init

Creating directory D:\Flask_project\migrations\versions ...  done
Generating D:\Flask_project\migrations\alembic.ini ...  done
Generating D:\Flask_project\migrations\env.py ...  done
Generating D:\Flask_project\migrations\README ...  done
Generating D:\Flask_project\migrations\script.py.mako ...  done
Please edit configuration/connection/logging settings in 'D:\\Flask_project\\migrations\\alembic.ini' before proceeding.

(venv) D:\Flask_project>python manage.py migrate

2.python manage.py db migrate

INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'user'
Generating D:\Flask_project\migrations\versions\dfcc030abccd_.py ...  done

(venv) D:\Flask_project>python manage.py db upgrade
3.执行python manage.py db upgrade后，正式将user表映射到数据库中
  done

(venv) D:\Flask_project>python manage.py db upgrade
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> dfcc030abccd, empty message

(venv) D:\Flask_project>




"""
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from zlktqa import app
from exts import db
from models import User,Question,Answer
manager=Manager(app)

#使用migrate绑定app和db
migrate=Migrate(app,db)

#添加迁移脚本的命令到manager中
manager.add_command('db',MigrateCommand)
if __name__=="__main__":
    manager.run()