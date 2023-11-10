from flask import Blueprint,redirect, url_for, render_template, request, make_response
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

@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge(): 
    msg = ''
    if request.method =='GET':
        return render_template('fridge.html', msg=msg)
    
    temperature = request.form.get('temperature')

    if temperature == '':
        msg ='Не задана температура'
    else:
        temperature = int(temperature)
        if temperature < -12:
            msg ='Не удалось установить температуру — слишком низкое значение'
        elif temperature > -1:
            msg = 'Не удалось установить температуру — слишком высокое значение'
        elif (temperature >= -12) and (temperature <= -9):
            msg = f'Установлена температура: {temperature}°С ❄️❄️❄️'
        elif (temperature >= -8) and (temperature <= -5):
            msg = f'Установлена температура: {temperature}°С ❄️❄️'
        elif (temperature >= -4) and (temperature <= -1):
            msg = f'Установлена температура: {temperature}°С ❄️'
    return render_template('fridge.html', temperature=temperature, msg=msg)


@lab4.route("/lab4/zerno", methods = ['GET', 'POST'])
def zerno():
    if request.method == 'GET':
        return render_template('zerno.html')
    price = 0
    msg = ''
    msg2 = ''
    zerno = request.form.get('zerno')
    weight = request.form.get('weight')

    if weight == '':
            msg = 'Не задан нужный вес'
            return render_template('zerno.html',msg=msg)
    
    weight = int(weight)

    if zerno == 'barley':
            price = 12000 * weight
    elif zerno == 'oats':
            price = 8500 * weight
    elif zerno == 'wheat':
            price = 8700 * weight
    else: 
        zerno == 'rye'
        price = 14000 * weight

    if weight <= 0:
            msg = 'Неверное значение'
            return render_template('zerno.html',msg=msg)
    elif weight > 500:
            msg = 'Нужного объема зерна нет в наличии'
            return render_template('zerno.html',msg=msg)
    elif weight > 50:
            price= price - (price * 10 / 100)
            msg2 = 'Применится скидка 10% за большой объем'
    return render_template('zernoOK.html', price=price, zerno=zerno, weight=weight, msg=msg, msg2 = msg2)


@lab4.route("/lab4/zernoOK")
def zernoOK():
    return render_template('zernoOK.html')


@lab4.route("/lab4/cookies", methods=['GET', 'POST'])
def cookies():
    if request.method =='GET':
        return render_template('cookies.html')
    
    color = request.form.get('color')
    b_color = request.form.get('background-color') 
    f_size = request.form.get('font-size')
    msg = ''

    if color == b_color:
        msg = 'цвет текста не должен совпадать с цветом фона'
        return render_template('cookies.html', msg = msg)
    elif color != b_color:
        color = color

    if f_size == '':
        msg = 'Задайте размер текста'
        return render_template('cookies.html', msg = msg)
    
    if 5<= int(f_size) <= 30:
        f_size = str(f_size) + 'px'
    else:
        msg = 'Размер текста должен быть от 5px до 30px'
        return render_template('cookies.html', msg = msg)
    
    headers = {
         'Set-Cookie': 'color=' + color + f_size + b_color + '; path=/',
         'Set-Cookie': 'font-size=' + f_size + '; path=/',
         'Set-Cookie': 'background-color=' + b_color + '; path=/',
         'Location': '/lab4/cookies'
    }
    return '', 303, headers









