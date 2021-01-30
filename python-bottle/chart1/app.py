from flask import Flask
from flask import render_template
from time import time
import pygal
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenido a la lreria charting "

@app.route("/bar")
def bar():
    with open('bar.json','r') as bar_file:
        data = json.load(bar_file)
    chart = pygal.Bar()
    mark_list = [x['mark'] for x in data]
    chart.add('Anual mark lista',mark_list)
    chart.x_labels = [x['year'] for x in data]
    chart.render_to_file('static/images/bar_chart.svg')
    img_url = 'static/images/bar_chart.svg?cache='+str(time())
    return render_template('app.html',image_url= img_url)

if __name__ == "__main__":
    app.run(debug=True)

