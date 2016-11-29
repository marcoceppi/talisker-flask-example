from hw_fixtures import *


def test_hello_from_base_url(client):
    rsp = client.get('/')
    assert rsp.status == '200 OK'
    data = rsp.get_data(as_text=True)
    assert 'Hello, World!' in data
