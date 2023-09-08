from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu",code=302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных, меню (см.ниже)
        </header>

           <h2>Меню</h2>

            <a href="http://127.0.0.1:5000/lab1">Первая лабораторная</a>

        <footer>
            &copy; Крышева В.Д.,ФБИ-12, 3 курс, 2023
        </footer>
         </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title>Крышева Виктория Дмитриевна, Лабораторная 1</title>
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

        <footer>
            &copy; Крышева В.Д.,ФБИ-12, 3 курс, 2023
        </footer>
         </body>
</html>
"""