
def test_get_api(get_api_client):
    """test availability of the api"""
    client = get_api_client
    assert client.get("/").status_code == 200
