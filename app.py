from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/lab2")
def lab2():
    return render_template('lab2.html')

@app.route("/lab2/random")
def random():
    return render_template('random.html')

@app.route("/lab2/example")
def example():
    name = 'Крышева В.Д.'
    lab2 = 'Лабораторная работа 2'
    group = 'ФБИ-12'
    course = '3 курс'
    fruits= [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'манадарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]
    books = [
        {'author': 'Алексей Иванов', 'name': '«Бронепароходы»', 'genre': 'Исторический роман', 'pages': '700 стр.'},
        {'author': 'Элизабет Вуртцель', 'name': '«Нация прозака»', 'genre': 'Современные зарубежные романы', 'pages': '470 стр.'},
        {'author': 'Ма Боюн', 'name': '«Зоопарк на краю света»', 'genre': 'Исторический роман', 'pages': '300 стр.'},
        {'author': 'Павел Пепперштейн', 'name': '«Бархатная кибитка»', 'genre': 'Проза', 'pages': '640 стр.'},
        {'author': 'Элизабет Страут', 'name': '«О, Уильям!»', 'genre': 'Современная проза', 'pages': '288 стр.'},
        {'author': 'Стиг Дагерман', 'name': '«Немецкая осень»', 'genre': 'Современная проза', 'pages': '256 стр.'},
        {'author': 'Селеста Инг', 'name': '«Наши пропавшие сердца»', 'genre': ' Роман', 'pages': '352 стр.'},
        {'author': 'Ханья Янагихара', 'name': '«До самого рая»', 'genre': 'Современный роман', 'pages': '576 стр.'},
        {'author': 'Одри Мэги', 'name': '«Колония»', 'genre': 'Исторический роман', 'pages': '300 стр.'},
        {'author': 'Оливия Мэннинг', 'name': '«Величайшее благо»', 'genre': 'Современная классика', 'pages': '350 стр.'},
    ]
    return render_template('example.html', name=name, lab2=lab2, group=group,course=course, fruits=fruits, books=books)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu",code=302)

@app.route("/menu")
def menu():
    return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных, меню (см.ниже)
        </header>

           <h2>Меню</h2>

            <a href="/lab1">Первая лабораторная</a><br>
            <a href="/lab2">Вторая лабораторная</a><br>

        <footer>
            &copy; Крышева В.Д.,ФБИ-12, 3 курс, 2023
        </footer>
         </body>
</html>
'''
@app.route("/lab1/tree")
def tree():
    return '''
<!doctype html>
<html>
    <head>
        <title>Крышева Виктория Дмитриевна, Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='tree.jpg') + '''">

         <footer>
            &copy; Крышева В.Д.,ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
    '''

@app.route("/lab1/student")
def student():
    return '''
<!doctype html>
<html>
    <head>
        <title>Крышева Виктория Дмитриевна, Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
         <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>&#9734;Крышева Виктория Дмитриевна&#9734;</h1>
        <img src="''' + url_for('static', filename='NSTU.jpg') + '''">

        <footer>
            &copy; Крышева В.Д.,ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
    '''

@app.route("/lab1/python")
def puthon():
    return '''
<!doctype html>
<html>
    <head>
        <title>Крышева Виктория Дмитриевна, Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
         <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>Puthon</h1>
        
        <p>Язык программирования Python 3 — это мощный инструмент для создания программ самого разнообразного 
        назначения, доступный даже для новичков. С его помощью можно решать 
        задачи различных типов.
        </p>

        <p>Язык Python обладает некоторыми примечательными особенностями, которые обуславливают его широкое 
        распространение. 
        Поэтому прежде чем изучать python, следует рассказать о его достоинствах и недостатках.
        </p>

        <img src="''' + url_for('static', filename='Python.jpg') + '''">

        <footer>
            &copy; Крышева В.Д.,ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
    '''

@app.route("/lab1/scream")
def scream():
    return '''
<!doctype html>
<html>
    <head>
        <title>Крышева Виктория Дмитриевна, Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
         <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>Крик - Эдвард Мунк. 1893. Картон, масло, темпера, пастель. 91х73,5</h1>
        
        <p>Образец экспрессионизма, картина "Крик", как и многочисленные ее варианты, до сих пор является одним из самых загадочных шедевров мировой живописи.
        </p>

        <p>Многие критики полагают, что сюжет картины - плод больной фантазии психически нездорового человека. Кто-то видит в работе предчувствие экологической катастрофы, кто-то решает вопрос о том, какая именно мумия вдохновила автора на эту работу.
        </p>

        <img src="''' + url_for('static', filename='scream.jpg') + '''">

        <footer>
            &copy; Крышева В.Д.,ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
    '''

@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title>Крышева Виктория Дмитриевна, Лабораторная 1</title>
        <link rel="stylesheet" href="""+ url_for('static', filename='lab1.css') + """>

    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

         <p>Flask — фреймворк для создания веб-приложений на языке<br>
            программирования Python, использующий набор инструментов<br>
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так<br>
            называемых микрофреймворков — минималистичных каркасов<br>
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</p>

             <a href="http://127.0.0.1:5000/menu">Меню</a>

             <h2>Реализованные роуты</h2>
             <a href="http://127.0.0.1:5000/lab1/tree">Дуб</a><br>
             <a href="http://127.0.0.1:5000/lab1/student">Студент</a><br>
             <a href="http://127.0.0.1:5000/lab1/python">Python</a><br>
             <a href="http://127.0.0.1:5000/lab1/scream">Картина "Крик"</a><br>

        <footer>
            &copy; Крышева В.Д.,ФБИ-12, 3 курс, 2023
        </footer>
     </body>
</html>
"""