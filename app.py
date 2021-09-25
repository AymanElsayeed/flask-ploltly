import sys
import os
from flask import Flask, url_for, jsonify, render_template, request
import json
import plotly
import argparse
from src.Plots import *
from src.config import FactoryConfigClass

app = Flask(__name__)


@app.route('/home')
@app.route('/')
def home():
    links = []
    for rule in app.url_map.iter_rules():
        links.append(rule.endpoint)
    return render_template('index.html', links=links)


@app.route('/view_bar_plot', methods=["GET", "POST"])
def view_bar_plot():
    countries = unique_countries()
    numeric_columns = float_columns()

    country = request.form.get('country', countries[0])
    x = request.form.get('X', numeric_columns[0])
    y = request.form.get('Y', numeric_columns[1])

    fig = bar_plot(x=x, y=y, country=country)
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('bar_plot.html', graph_json=graph_json, countries=countries, Y=numeric_columns,
                           X=numeric_columns)


@app.route('/view_scatter_plot', methods=["GET", "POST"])
def view_scatter_plot():
    x = request.form.get('x', 'lifeExp')
    y = request.form.get('y', 'gdpPercap')
    color = request.form.get('color', 'country')
    size = request.form.get('size', 'pop')

    fig = scatter_plot(x=x, y=y, color=color, size=size)

    scatter_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('scatter_plot.html', scatter_json=scatter_json)


@app.route('/view_line_plot', methods=["GET", "POST"])
def view_line_plot():
    country = request.form.get('countri', 'Oceania')
    fig = line_plot(x='year', y='lifeExp', color='country', mode="lines+markers", continent='Oceania')
    line_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    countries = unique_countries()
    return render_template('line_plot.html', line_json=line_json, countries=countries)


@app.route('/view_sunburst_plot', methods=["GET", "POST"])
def view_sunburst_plot():

    fig = sunburst_plot()
    sunburst_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    countries = unique_countries()
    return render_template('sunburst_plot.html', sunburst_json=sunburst_json, countries=countries)


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="input arguments")
    parser.add_argument("-env", "--environment", help="environment name: prod, qa, or dev", type=str,
                        required=False, default='dev')
    args = parser.parse_args()
    app.config.from_object(FactoryConfigClass(env=args.environment))
    app.run('0.0.0.0', 5000, debug=True, threaded=True, use_reloader=True)
