from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
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

        <h1>веб-сервер на Flask</h1>

        <footer>
            &copy; Крышева В.Д.,ФБИ-12, 3 курс, 2023
        </footer>
         </body>
</html>
"""

