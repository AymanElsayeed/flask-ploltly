
def test_get_api(get_api_client):
    """test availability of the api"""
    client = get_api_client
    assert client.get("/").status_code == 200


def test_bar_plot(get_api_client):
    response = get_api_client.get("/view_bar_plot")
    assert response.status_code == 200


def test_line_plot(get_api_client):
    response = get_api_client.get("/view_line_plot")
    assert response.status_code == 200


def test_view_scatter_plot(get_api_client):
    response = get_api_client.get("/view_scatter_plot")
    assert response.status_code == 200
