from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def town_old():
    context = {
        "link": "Экскурсии по городам старой России"
    }
    return render_template('home.html', **context)
@app.route('/newtime/')
def town_new():
    context = {
        "link": "Экскурсии по городам новой России"
    }
    return render_template('about.html', **context)

if __name__ == '__main__':
    app.run()