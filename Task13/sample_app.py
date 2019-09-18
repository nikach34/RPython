import flask
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


def gcd(x, y):
  while x != 0 and y != 0:
      if x > y:
          x %= y
      else:
          y %= x
  return x + y

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

