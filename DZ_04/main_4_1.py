import datetime
from flask import Flask
app = Flask(__name__)

@app.route('/')
def current_datetime():
    current_datetime = datetime.datetime.now()
    current_datetime_string = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return f"Текущая дата и время: {current_datetime_string}"

if __name__ == '__main__':
    app.run()

