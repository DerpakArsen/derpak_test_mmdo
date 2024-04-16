from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    r = requests.get('https://api.github.com/events')
    data = r.text
    return render_template("index.html", data=data)

@app.route('/help')
def help():
    count =+ 1
    return f"""
    <body style="background-color:powderblue;">
    <p>Це сторінка з документацією. Поки що вона є пуста.</p>
    <p>Сайт запущений на {os.environ["OS"]}</p>
    <p>Ви відвідали цю сторінку {count} разів</p>
    """

# Екзамен
@app.route('/info')
def info():
    return '<p>Ура я здав екзамен!</p>'

if __name__ == '__main__':
    app.run(debug=True)