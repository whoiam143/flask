from flask import Flask
from flask import url_for, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def x():
   return "<h1>Миссия Колонизация Марса<h1>"


@app.route("/index")
def index():
    return "<h1>И на Марсе будут яблони цвести!<h1>"


@app.route("/promotion")
def promotion():
    lst = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
           "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return "<br>".join(lst)


@app.route("/image_mars")
def image_mars():
    return f''' <h1>Жди нас, Марс!<h1><br>
                <img src="{url_for('static', filename='static/mars.png')}"><br>
                Вот она какая, красивая планета.'''


@app.route("/promotion_image")
def promotion_image():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')