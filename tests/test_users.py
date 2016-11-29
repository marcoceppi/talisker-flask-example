from json import loads

from pytest import fixture

from hw_fixtures import *


@fixture(scope='module')
def users():
    return [
        {'id': 1, 'username': 'bob'},
        {'id': 2, 'username': 'fred'},
        {'id': 3, 'username': 'alice'},
    ]


def test_no_users(client, database):
    rsp = client.get('/users/')
    assert rsp.status == '200 OK'
    data = loads(rsp.get_data(as_text=True))
    assert data == {'json_list': []}


def test_new_users(client, database, users):
    for user in users:
        rsp = client.post('/users/', data=user)
        assert rsp.status == '200 OK'
        data = loads(rsp.get_data(as_text=True))
        assert data == user

    rsp = client.get('/users/')
    assert rsp.status == '200 OK'
    data = loads(rsp.get_data(as_text=True))
    assert data == {'json_list': users}
