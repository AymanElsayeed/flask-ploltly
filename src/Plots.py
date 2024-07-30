"""
Basic Plots base on gap-minder data set.
"""
import plotly.express as px
import asyncio
import plotly.io as pio
png_renderer = pio.renderers["svg"]
png_renderer.width = 500
png_renderer.height = 500
pio.renderers.default = "svg"


def unique_countries():
    """
    unique countries in the data set.
    :return: list
    """
    df = px.data.gapminder()
    countries = df.country.unique().tolist()
    return countries


def unique_subgroup():
    df = px.data.gapminder()
    s = df.select_dtypes(exclude=[float, int])
    sub_group = s.apply(lambda x: x.unique().tolist()).to_dict()
    return sub_group


def unique_continent():
    """
    unique continent in the data set.
    :return: list
    """
    df = px.data.gapminder()
    continent = df.continent.unique().tolist()
    return continent


def unique_iso_alpha():
    """
    unique_iso_alpha in the data set.
    :return: list
    """
    df = px.data.gapminder()
    iso_alpha = df.iso_alpha.unique().tolist()
    return iso_alpha


def unique_year():
    """
    unique year in the data set.
    :return: list
    """
    df = px.data.gapminder()
    year = df.year.unique().tolist()
    return year


def unique_columns():
    """
    unique columns in the data set.
    :return: list
    """
    df = px.data.gapminder()
    columns = df.columns.to_list()
    return columns


def float_columns():
    """
    float columns in the data set.
    :return: list
    """
    df = px.data.gapminder()
    return df.select_dtypes(include=[float, int]).columns.to_list()


def categorical_columns():
    """
    float columns in the data set.
    :return: list
    """
    df = px.data.gapminder()
    return df.select_dtypes(exclude=[float, int]).columns.to_list()


def bar_plot(x: str = 'year', y: str = 'pop', country: str = 'New Zealand'):
    """
    Generate Bar Plot
    :param x:
    :param y:
    :param country:
    :return: figure
    """
    nz = px.data.gapminder().query(f"country == '{country}'")
    title = f"{country} Population over time"
    fig = px.bar(nz, x=x, y=y, title="", height=300, width=300)
    return fig


def line_plot(x: str, y: str, color: str, sub_group: str, mode: str, column: str):
    """
    Generate Line Plot
    :param x:
    :param y:
    :param color:
    :param sub_group:
    :param column:
    :param mode:
    :return: figure
    """
    df = px.data.gapminder().query(f"{column}=='{sub_group}'")
    fig = px.line(df, x=x, y=y, color=color)
    fig.update_traces(mode=mode)
    return fig


def scatter_plot(x='lifeExp', y='gdpPercap', color='country', size='pop'):
    """
    Generate Scatter Plot
    :param x:
    :param y:
    :param color:
    :param size:
    :return: figure
    """
    df = px.data.gapminder()
    fig = px.scatter(df, x=x, y=y, color=color, size=size, render_mode='svg')
    return fig


def sunburst_plot(color='lifeExp', values='pop', year=2007, path=None):
    """
    Generate Sunburst Plot
    :param color:
    :param values:
    :param year:
    :param path:
    :return: figure
    """
    if path is None:
        path = ['continent', 'country']
    df = px.data.gapminder().query(f"year == {year}")
    fig = px.sunburst(df, path=path, color=color, values=values)
    return fig
