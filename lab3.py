from flask import Blueprint,redirect, url_for, render_template, request
lab3 = Blueprint('lab3',__name__)


@lab3.route("/lab3")
def lab():
    return render_template('lab3.html')


@lab3.route("/lab3/form")
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors = errors)


@lab3.route("/lab3/order")
def order():
    return render_template('order.html')


@lab3.route("/lab3/pay")
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink =='black-tea':
        price = 80
    else:
        price = 70
    
    if request.args.get('milk') == 'on':
        price +=30
    if request.args.get('sugar') == 'on':
        price +=10
    return render_template('pay.html', price=price)


@lab3.route("/lab3/success")
def success():
    return render_template('success.html')


@lab3.route('/lab3/ticket')
def ticket():
    errors = {}
    name = request.args.get('name')
    age = request.args.get('age')
    from_where = request.args.get('from_where')
    where = request.args.get('where')
    date = request.args.get('date')
    if name == '':
        errors['name'] = 'Введите данные'
    if age == '':
        errors['age'] = 'Введите данные'
    if from_where == '':
        errors['from_where'] = 'Введите данные'
    if where == '':
        errors['where'] = 'Введите данные'
    if date == '':
        errors['date'] = 'Введите данные'

    return render_template('ticket.html', name=name, age=age, from_where=from_where, where=where, date=date, errors=errors)





