import time

from flask import Flask, request
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    return render_template('hello.html',name=name)


@app.route('/eval', methods=['GET', 'POST'])
def evaluate():
    numbEval=int(request.args['number'])

    if request.method == 'POST':
        return do_the_evaluation(numbEval)
    else:
        return do_the_evaluation(numbEval)


def do_the_evaluation(numbEval):
    time.sleep(numbEval)

    return 'Ok'


if __name__ == '__main__':
    app.run()
