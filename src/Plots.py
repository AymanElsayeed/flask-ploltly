"""
Basic Plots base on gap-minder data set.
"""
import plotly.express as px


def unique_countries():
    """
    unique countries in the data set.
    :return: list
    """
    df = px.data.gapminder()
    countries = df.country.unique().tolist()
    return countries


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


def bar_plot(x: str = 'year', y: str = 'pop', country: str = 'New Zealand'):
    """
    Generate Bar Plot
    :param x:
    :param y:
    :param country:
    :return: figure
    """
    nz = px.data.gapminder().query(f"country == '{country}'")
    fig = px.bar(nz, x=x, y=y, title=f"{country} Population over time")
    return fig


def line_plot(x='year', y='lifeExp', color='country', continent='Oceania', mode="lines+markers"):
    """
    Generate Line Plot
    :param x:
    :param y:
    :param color:
    :param continent:
    :param mode:
    :return: figure
    """
    df = px.data.gapminder().query(f"continent=='{continent}'")
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
    fig = px.scatter(df, x=x, y=y, color=color, size=size)
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
