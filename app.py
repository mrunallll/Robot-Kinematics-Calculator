from flask import Flask, request, flash, redirect, url_for, send_file, render_template
import pandas as pd

from functions.t1d1 import t1d1
from functions.t1d2 import t1d2
from functions.t1d3 import t1d3
from functions.t2d1 import t2d1
from functions.t2d2 import t2d2
from functions.t2d3 import t2d3

app = Flask(__name__)
app.secret_key = 'wshofj90792jwfjw903u2m093840298.!rajrajhans!'


@app.route("/", methods=["POST", "GET"])
def index():

    return render_template('homepage.html')

@app.route("/calculate", methods=["POST", "GET"])
def calculate():
    if request.method == 'POST':
        t = int(request.form['kinematicsType'])
        d = int(request.form['robotType'])

        # try:
        if t == 1 and d == 1:
            Lx = int(request.form['t1d1Lx'])
            Ly = int(request.form['t1d1Ly'])
            Lz = int(request.form['t1d1Lz'])
            res = t1d1(Lx, Ly, Lz)

            return render_template('printMatrix.html', data=res)

        if t == 1 and d == 2:
            Lx = int(request.form['t1d2Lx'])
            Qz = int(request.form['t1d2Qz'])
            Lz = int(request.form['t1d2Lz'])
            res = t1d2(Lx, Qz, Lz)

            return render_template('printMatrix.html', data=res)

        if t == 1 and d == 3:
            Lz = int(request.form['t1d3Lz'])
            Qy = int(request.form['t1d3Qy'])
            Qz = int(request.form['t1d3Qz'])
            res = t1d3(Lz, Qy, Qz)

            return render_template('printMatrix.html', data=res)

        if t == 2:
            input_string = request.form['t2point'].strip()
            points = [int(x) for x in input_string.split()]

            if d == 1:
                res = t2d1(points)
                return render_template('printString.html', data=res)

            if d == 2:
                res = t2d2(points)
                return render_template('printString.html', data=res)

            if d == 3:
                res = t2d3(points)
                return render_template('printString.html', data=res)

        # except:
        #     flash('An error occurred. Please make sure the inputs are valid.', 'error')
    return render_template('homepage.html')


if __name__ == '__main__':
    app.run(debug=True)
