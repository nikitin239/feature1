from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello GSOM!'

def sum(a,b):
    return a+b

if __name__ == '__main__':
    app.run(port=8888, debug=True)
