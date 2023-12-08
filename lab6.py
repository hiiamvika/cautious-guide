from flask import Blueprint,redirect, url_for, render_template, request, session
from Db import db
from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user,logout_user

lab6 = Blueprint("lab6",__name__)

@lab6.route("/lab6/check")
def main():
    my_users = users.query.all()
    print(my_users)
    return "result in console!"


@lab6.route("/lab6/checkarticles")
def all_articles():
    all_articles = articles.query.all()
    print(all_articles)
    return "result in console!"


@lab6.route("/lab6")
def main():
    try:
        username = (users.query.filter_by(id=current_user.id).first()).username
        return render_template("lab6.html", username = username)
    except:
         return render_template("lab6.html", username = "Аноним")


@lab6.route("/lab6/register", methods=['GET', 'POST'])
def registerPage():
    errors = []

    if request.method =='GET':
        return render_template("register.html", errors = errors)
    
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    if not (username_form or password_form):
        errors.append("Пожалуйста, заполните все поля")
        print(errors)
        return render_template("register.html", errors=errors)

    isUserExist = users.query.filter_by(username=username_form).first()

    if isUserExist is not None:
        errors.append("Пользователь с таким именем уже существует")
        return render_template("register.html", errors=errors)
    
    hashedPswd = generate_password_hash(password_form, method='pbkdf2')
    newUser = users(username=username_form, password=hashedPswd)

    db.session.add(newUser)
    db.session.commit()
    return redirect("/lab6/login")


@lab6.route("/lab6/login", methods=['GET', 'POST'])
def login():
    errors = ''
    if request.method =='GET':
        return render_template("login.html")
    
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    isUserExist = users.query.filter_by(username=username_form).first()

    my_user = users.query.filter_by(username=username_form).first()
    
    if username_form is None and password_form is None:
        errors = 'Заполните все поля!'
        return render_template("login.html", errors=errors)
    else:
        if my_user is not None:
            if check_password_hash(my_user.password, password_form):
                login_user(my_user, remember=False)
                return redirect("/lab6")
            else:
                errors = 'Неверный пароль!'
                return render_template("login.html", errors=errors)
        else:
            errors = 'Пользователя с таким именем не существует!'
            return render_template("login.html", errors=errors)
    
        return render_template("login.html")


@lab6.route("/lab6/articles_all")
@login_required
def articles_list():
    my_articles = articles.query.filter_by(user_id=current_user.id).all()
    return render_template("articleAll.html", articles = my_articles)


@lab6.route("/lab6/logout")
@login_required
def logout():
    logout_user()
    return render_template('lab6.html')


@lab6.route("/lab6/new_article", methods=['GET', 'POST'])
@login_required
def createArticle():
    errors = ''
    if request.method == "GET":
        return render_template("new_article.html")
    else:
        userID = current_user.id
        text_article = request.form.get("text_article")
        title = request.form.get("title_article")

        if text_article == '' or title == '':
                errors = 'Заполните все поля!'
                return render_template("new_article.html", errors=errors)
        
        newArticle = articles(user_id = userID, title = title, article_text = text_article)

        db.session.add(newArticle)
        db.session.commit()

    return render_template("new_article.html")


@lab6.route("/lab6/articles/<int:article_id>")
@login_required
def getArticle(article_id):
    #достать из токена
    username = (users.query.filter_by(id=current_user.id).first()).username
    myArticle = articles.query.filter_by(id=article_id).first()
    
    title = myArticle.title
    text = myArticle.article_text
    
    return render_template ("articleN.html", title = title, article_text = text, username = username)
            







