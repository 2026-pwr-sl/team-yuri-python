import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


from lab7 import HTTPRequest, reqstr2obj


def test_reqstr2obj_raises_type_error_for_non_string():
    with pytest.raises(TypeError):
        reqstr2obj(123)


def test_reqstr2obj_returns_http_request_object():
    result = reqstr2obj("GET / HTTP1.1")

    assert isinstance(result, HTTPRequest)

def test_3():
    result = reqstr2obj("GET / HTTP1.1")

    assert result.request_type  == "GET"
    assert result.resource_path == "/"
    assert result.http_protocol == "HTTP1.1"

def test_4():
    test_strings = ["GET / HTTP1.1", "POST /index.html HTTP2", "DELETE /index.php HTTP3", "CONNECT /home HTTP3"]
    for i in test_strings:
        result = reqstr2obj(i)

        assert result.request_type  == i.split(' ')[0]
        assert result.resource_path == i.split(' ')[1]
        assert result.http_protocol == i.split(' ')[2]

def test_5():
    test_strings = ["GET / HTTP1.1 sadnkja", "POST /index", "DELETE / ", "  / HTTP3"]
    for i in test_strings:
        result = reqstr2obj(i)

        assert result is None

def test_6():
    test_strings = ["DOWNLOAD /movie.mp4 HTTP1.1", "IDK /file HTTP4", "SHITPOST / HTTP2"]
    for i in test_strings:
        with pytest.raises(TypeError):
            reqstr2obj(i)

def test_8():
    test_strings = ["GET index HTTP1.1", "POST index.html HTTP2", "DELETE index.php HTTP3", "CONNECT home/index HTTP3"]
    for i in test_strings:
        with pytest.raises(TypeError):
            reqstr2obj(i)


def test_7():
    test_strings = ["GET / HTTP1.01", "POST /index.html HTTPS2", "DELETE /index.php HTT3", "CONNECT /home HTTP2.1"]
    for i in test_strings:
        with pytest.raises(TypeError):
            reqstr2obj(i)

