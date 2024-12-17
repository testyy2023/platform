# conftest.py


import pytest
#定义一个全局变量，用于存储内容
global_data ={}

@pytest.fixture
def set_global_data():
    def _set_global_data(key,value):
        global_data[key] = value

    return _set_global_data

@pytest.fixture()
def get_global_data():
    def _get_global_data(key):
        return global_data.get(key)
    return _get_global_data