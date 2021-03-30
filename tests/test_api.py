import pytest
from stl_rda_lg.api import GET_DATA


def test_api_global():
    assert GET_DATA == {"a": 1, "b": 2}
