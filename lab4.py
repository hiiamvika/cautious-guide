from flask import Blueprint,redirect, url_for, render_template, request
lab4 = Blueprint('lab4',__name__)

@lab4.route("/lab4")
def lab():
    return render_template('lab4.html')


@lab4.route("/lab4/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'vika' and password == '123':
        return render_template('success4.html', username = username)
    else:
        error = 'Неверные логин и/или пароль'
    if username == '':
        error = 'Введите логин'
    if password == '':
        error = 'Введите пароль'
    return render_template('login.html', error=error, username = username, password = password)


@lab4.route("/lab4/success4")
def success4():
    username = request.args.get('username')
    return render_template('success4.html', username = username)
