from flask import Flask
from line.FitLine import FitLine

app = Flask(__name__)


@app.route('/')
def py_math():
    #return 'Hello World plus Jon!'

    fit_line = FitLine()
    return fit_line.do_fit()



if __name__ == '__main__':
    app.run()
