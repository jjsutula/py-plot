import argparse
import sys
from line.FitLine import FitLine
from points.Points import Points


def main(argv):
    """Main function.
       Make sure the following libraries are installed via pip3 install <library name>:
            numpy
            openpyxl
            scipy
    """
    parser = argparse.ArgumentParser(prog='plot', description="Given an excel file of points, find and graph the Simmons' curve that best fits the points")
    parser.add_argument('-f', '--file', required=True, type=str, help='a comma separated file of points to fit')
    parser.add_argument('-d', '--distance', required=True, type=int, help='distance guess')
    parser.add_argument('-g', '--gap', type=int, help='energy gap guess')
    args = parser.parse_args()

    # Get a list containing an array of x values and an array of y values.
    points = Points()
    point_list = points.parse_points(args.file)
    print(point_list)

    # Use the points from the file as input for the fit module
    fit_line = FitLine()
    print('The output point from fit_line is '+fit_line.do_fit(point_list))


# Do this so that main() only gets called if invoked via command line, but not if invoked programmatically
if __name__ == "__main__":
    main(sys.argv[1:])
