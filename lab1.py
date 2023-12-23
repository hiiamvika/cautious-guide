from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1',__name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu",code=302)


@lab1.route("/menu")
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
            <a href="/lab3">Третья лабораторная</a><br>
            <a href="/lab4">Четвертая лабораторная</a><br>
            <a href="/lab5">Пятая лабораторная</a><br>
            <a href="/lab6">Шестая лабораторная</a><br>
            <a href="/lab7/">Седьмая лабораторная</a><br>
            <a href="/lab8/">Восьмая лабораторная</a><br>


        <footer>
            &copy; Крышева В.Д.,ФБИ-12, 3 курс, 2023
        </footer>
         </body>
</html>
'''


@lab1.route("/lab1/tree")
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


@lab1.route("/lab1/student")
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


@lab1.route("/lab1/python")
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


@lab1.route("/lab1/scream")
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


@lab1.route("/lab1")
def lab():
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

             <a href="/menu">Меню</a>

             <h2>Реализованные роуты</h2>
             <a href="/lab1/tree">Дуб</a><br>
             <a href="/lab1/student">Студент</a><br>
             <a href="/lab1/python">Python</a><br>
             <a href="/lab1/scream">Картина "Крик"</a><br>

        <footer>
            &copy; Крышева В.Д.,ФБИ-12, 3 курс, 2023
        </footer>
     </body>
</html>
"""