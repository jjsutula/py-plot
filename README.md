#Plot
###Command Line Invocation (see plot.py):

usage: py plot.py [-h] -f FILE -d DISTANCE [-g GAP]

Example:
py plot.py -d 1 -f ./<Your points file name>.xlsx

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

###Alternatively Run As Web Program:
usage: py pymath.py

Then, open a web browser and go to:
 http://127.0.0.1:5000/

To quit the program, type CTRL-C
