from flask import Flask, render_template
from local_values.reader import env_value

app = Flask(__name__)
app.debug = env_value('DEBUG', default='False')
app.secret_key = env_value('SECRET_KEY')


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')
