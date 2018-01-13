from flask import Flask
from line.FitLine import FitLine
from points.Points import Points

app = Flask(__name__)


@app.route('/')
def py_math():

    # Get a list containing an array of x values and an array of y values.
    points = Points()
    point_list = points.parse_points('matrix.xlsx')

    # Use the points from the file as input for the fit module
    fit_line = FitLine()
    return 'The output point is '+fit_line.do_fit(point_list)



if __name__ == '__main__':
    app.run()
