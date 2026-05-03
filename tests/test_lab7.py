import pytest

from src.lab7 import HTTPRequest, reqstr2obj


def test_reqstr2obj_raises_type_error_for_non_string():
    with pytest.raises(TypeError):
        reqstr2obj(123)


def test_reqstr2obj_returns_http_request_object():
    result = reqstr2obj("GET / HTTP1.1")

    assert isinstance(result, HTTPRequest)