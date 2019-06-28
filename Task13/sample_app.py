


import flask
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


def gcd(x, y):
    if (y == 0):
    return x
    else:
    return gcd (x, x % y)


@app.route('/', methods = ['GET'])
def hello_name():
    if request.method == 'GET':
        x=request.args.get('x')
        y=request.args.get('y')
    k = ""
    if (x == None or y == None):
        x = 0
        y = 0
        k = "Ошибка"
    if (k == ""):
        result = str(gcd(int(x), int(y)))
    else:
        result = k
    return flask.render_template(
        'gcd.html',
        name=result,
    )

if __name__ == '__main__':
   app.run(debug = True)
