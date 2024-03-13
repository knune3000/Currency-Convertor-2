from flask import Flask, render_template, request
import currency_converter

app = Flask(__name__)

""""@app.route('/')
def index():
    return render_template("index.html")"""

@app.route('/')
def currency_converter():

    return render_template("currency_converter.html")


@app.route('/', methods=['POST'])
def getValue():
    usd = request.form["USD"]
    return render_template('pass.html', n=usd)

""""@app.route('/add' , methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        print(request.form.get("USD"))

    return render_template("currency_converter.html")"""


if __name__ == '__main__':
    app.run(debug=True)