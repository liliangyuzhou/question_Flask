#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: LILIANG
# @Date  : 2019/10/22
# @Desc  :  test
from  flask import Flask,render_template,request,redirect,url_for,session
import config
from models import User,Question,Answer
from exts import db
from decorator import login_required
from sqlalchemy import or_

app=Flask(__name__)
app.config.from_object(config)
db.init_app(app)



@app.route("/")
def index():
    context={
        'questions':Question.query.order_by(Question.create_time.desc()).all()
    }
    return render_template('index.html',**context)

@app.route('/login/',methods=["GET","POST"])
def login():
    if request.method=='GET':
        return render_template("login.html")
    else:
        telephone=request.form.get('telephone')
        password=request.form.get('password')
        user=User.query.filter(User.telephone==telephone,User.password==password).first()
        if user:
            session['user_id']=user.id
            #如果想在31天都不需要登录
            # session.permanent=True
            return redirect(url_for('index'))
        else:
            return "手机号码或者密码错误，请确认后再登录"

@app.route('/detail/<question_id>')
def detail(question_id):
    question_model=Question.query.filter(Question.id==question_id).first()

    print(question_model.author)
#这里是传参数打html页面的写法
    return render_template('detail.html',question_model=question_model)

@app.route('/logout/')
def logout():
    # session.pop('user_id')
    # del session['user_id']
    session.clear()
    return  redirect(url_for('login'))

@app.route('/register/',methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        telephone=request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #手机号码验证，如果已经被注册就不能再次注册
        user=User.query.filter(User.telephone==telephone).first()
        if user:
            return  u"该手机号码已被注册，请更换手机号码！"
        else:
        #password1要与password2相等
            if password1!=password2:
                return u"两次密码不相等，请核对后填写"
            else:
                user=User(telephone=telephone,username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                # 如果注册成功，就让页面跳转到登录的页面
                return redirect(url_for('login'))
@login_required
@app.route('/question/',methods=["GET","POST"])
def question():
    if request.method=="GET":
        return render_template("question.html")
    else:
        title=request.form.get('title')
        content=request.form.get('content')
        question=Question(title=title,content=content)
        user_id=session.get('user_id')
        user=User.query.filter(User.id==user_id).first()
        question.author_id=user.id
        db.session.add(question)
        db.session.commit()
        return redirect(url_for("index"))

@app.route("/add_answer/",methods=['POST'])
@login_required
def add_answer():
    content=request.form.get('answer-content')
    question_id=request.form.get('question_id')
    answer=Answer(content=content)
    user_id=session.get('user_id')

    user=User.query.filter(User.id==user_id).first()
    answer.author =user
    question=Question.query.filter(Question.id==question_id).first()
    answer.question=question
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('detail',question_id=question_id))


@app.route('/search/')
def search():
    q=request.args.get("q")
    #title,content,只要包含一个，使用或
    # questions=Question.query.filter(or_(Question.title.contains(q),Question.content.contains(q))).order_by(Question.create_time.desc())


    # title,content,两个都要包含，使用且，什么修饰函数都不要用。
    questions = Question.query.filter(Question.title.contains(q), Question.content.contains(q)).order_by(Question.create_time.desc())
    return render_template('index.html',questions=questions)


@app.context_processor
def my_context_processor():
    user_id=session.get('user_id')
    if user_id:
        user=User.query.filter(User.id==user_id).first()
        if user:
            return {"user":user}
    else:
        #被这个装饰器修饰的钩子函数，必须要返回一个字典，即使为空也要返回
        return {}
if __name__=='__main__':
    app.run()