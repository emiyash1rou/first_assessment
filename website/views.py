#Where the homepage is, gui
 
from flask import Blueprint, render_template,request,flash,redirect,url_for
from flask_login import login_required, current_user
from .models import ToDoList
from . import db
views = Blueprint("views",__name__)
 
@views.route("/")
@views.route("/home")
@login_required
def home():
    todolists=ToDoList.query.all()
 
    return render_template("home.html",user=current_user)
 
@views.route("/create-post",methods=['GET','POST'])
@login_required
def create_post():
    if request.method=='POST':
        description=request.form.get('description')
        description=description.replace("\r\n","")
        title=request.form.get('title')
        if not description:
            flash('ToDoList cannot be empty',category='error')
        else:
            todolist=ToDoList(title=title,description=description,author=current_user.id)
            db.session.add(todolist)
            db.session.commit()
           
            flash('ToDoList created',category='success')
            return redirect(url_for('auth.login'))
 
    return render_template("create_post.html",user=current_user)