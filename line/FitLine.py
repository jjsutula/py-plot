# Given an excel file of points, find and graph the line that best fits the points.
# Next, find and graph a more complex exponential curve.
# The finished program will scan over a range of phis and ds (see equation) where
#   the inputs will be the range and the  increment (we may default the increment).
#   The outputs will be the optimal phi, d, error (avg distance) and the graph.

import numpy as np
from scipy.optimize import curve_fit


class FitLine:
    status = 0
    x = np.array([1, 2, 3, 9])
    y = np.array([1, 4, 1, 3])

    def fit_func(self, x, a, b):
        return a*x + b

    def do_fit(self):
        params = curve_fit(self.fit_func, self.x, self.y)

        [a, b] = params[0]
        return 'a='+str(a)+' b='+str(b)
