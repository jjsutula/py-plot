#Plot
###Command Line Invocation (see plot.py):

usage: plot [-h] -f FILE -d DISTANCE [-g GAP]

Example:
plot -d 1 -f ./<Your points file name>.xlsx

###Installation Notes:
       Make sure the following libraries are installed via
         pip install <library name>:
         (If pip is not found, try py -m pip install <library name>)
            numpy
            openpyxl
            scipy
            flask

###Excel File Format:
    The expected file format is that Column A will contain all the x values
    and column B will contain all the y values. The first row(s) may be header(s)
    but once the first row of numbers is encountered all subsequent rows should
    be filled with numbers.
