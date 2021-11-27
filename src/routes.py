from src import *
from src.Plots import *
import json
from flask import render_template
import plotly
import os


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

    country = request.form.get('group', countries[0])
    x = request.form.get('X', numeric_columns[0])
    y = request.form.get('Y', numeric_columns[1])

    fig = bar_plot(x=x, y=y, country=country)
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('bar_plot.html', graph_json=graph_json, Groups=countries, Y=numeric_columns,
                           X=numeric_columns, title="Bar Plot page")


@app.route('/view_scatter_plot', methods=["GET", "POST"])
def view_scatter_plot():
    numeric_columns = float_columns()
    # cat_columns = categorical_columns()

    x = request.form.get('X', numeric_columns[0])
    y = request.form.get('Y', numeric_columns[1])
    size = request.form.get('size', numeric_columns[2])
    # color = request.form.get('color', cat_columns[0])

    fig = scatter_plot(x=x, y=y, size=size)

    scatter_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('scatter_plot.html', graph_json=scatter_json, X=numeric_columns, Y=numeric_columns,
                           Sizes=numeric_columns, title="Scatter Plot Graph")


@app.route('/view_line_plot', methods=["GET", "POST"])
def view_line_plot():
    numeric_columns = float_columns()
    cat_columns = categorical_columns()

    x = request.form.get('X', numeric_columns[0])
    y = request.form.get('Y', numeric_columns[1])

    column, sub_group = request.form.get('option', 'continent,Oceania').split(',')
    color = request.form.get('color', cat_columns[0])
    mode = request.form.get('mode', "lines+markers")

    options = unique_subgroup()

    fig = line_plot(x=x, y=y, color=color, mode=mode, column=column, sub_group=sub_group)

    line_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('line_plot.html', graph_json=line_json,
                           X=numeric_columns, Y=numeric_columns, Options=options,
                           Colors=cat_columns,
                           title="Line Plot Page")


@app.route('/view_sunburst_plot', methods=["GET", "POST"])
def view_sunburst_plot():

    fig = sunburst_plot()
    sunburst_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    countries = unique_countries()
    return render_template('sunburst_plot.html', graph_json=sunburst_json, countries=countries,
                           title="Sunburst Plot Page")


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