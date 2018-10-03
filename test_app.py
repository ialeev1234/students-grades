import requests

from app import url


def test_request_charts():
    r = requests.get(url + '/api/charts?student=0&room=0&quarter=0&subject=0&grouping=student')
    assert r.headers['content-type'] == "application/json"
    data = r.json()
    assert isinstance(data, dict)
