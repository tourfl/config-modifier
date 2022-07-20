import copy

import pytest

from modify_config import modify_config

@pytest.fixture
def config():
    """
    basic config
    """

    my_conf = {
        "page1": {
            "initialSettings": {
                "coordinates": [10, 12],
                "color": "white"
            },
            "available-filters": {
                "name-filter": {
                    "column": "name",
                    "sort": "desc"
                }
            }
        }
    }

    return my_conf

@pytest.fixture
def config2():
    """
    second config
    """
    my_conf = {
        "page1": {
            "initialSettings": {
                "coordinates": [10, 12],
                "color": "green"
            },
            "available-filters": {
                "name-filter": {
                    "column": "name",
                    "sort": "asc"
                }
            },
            "data": [
                {
                    "x": 10,
                    "value": 100
                },
                {
                    "x": 20,
                    "value": 200
                }
            ]
        }
    }

    return my_conf


@pytest.fixture
def config3():
    """
    config with arrays at different levels
    """
    my_conf = {
        "vessels": [{"coordinates": [13, 15], "name": "flying dutch"}, {"coordinates": [42, 21], "name": "maltese hawk"}]
    }

    return my_conf

def test_change_value_OK(config):
    """
    basic change of a config value
    """
    change = {"page1.initialSettings.color": "green"}
    modify_config(config, change)

    assert config["page1"]["initialSettings"]["color"] == "green"

def test_change_double_value_OK(config):
    """
    the change affects two different pathes
    """
    change = {"page1.available-filters.name-filter.sort": "asc", "page1.initialSettings.color": "green"}
    modify_config(config, change)

    assert config["page1"]["initialSettings"]["color"] == "green"
    assert config["page1"]["available-filters"]["name-filter"]["sort"] == "asc"

def test_wrong_path_KO(config):
    """
    change affects an unexisting path
    """
    initial_config = copy.deepcopy(config)  # copy in order to be sure that no change occured

    change = {"page1.unexisting-key.sort": "should not exist"}
    modify_config(config, change)  # should do nothing

    assert "unexisting-key" not in config["page1"]
    assert initial_config == config

def test_change_array_OK(config):
    """
    the change affects an array
    """
    change = {"page1.initialSettings.coordinates[0]": {"value": "Wow JSON injected!!"}}
    modify_config(config, change)

    assert config["page1"]["initialSettings"]["coordinates"][0] == {"value": "Wow JSON injected!!"}

def test_change_array_2_OK(config2):
    """
    change affects an array at an intermediate level
    """
    change = {"page1.data[0].value": 400}
    modify_config(config2, change)

    assert config2["page1"]["data"][0]["value"] == 400

def test_change_array_3_OK(config3):
    """
    the change affects array at two different levels
    """
    change = {"vessels[0].coordinates[1]": {"value": "Wow JSON injected!!"}}

    modify_config(config3, change)

    assert config3["vessels"][0]["coordinates"][1] == {"value": "Wow JSON injected!!"}

def test_index_out_of_range_KO(config):
    """
    the change affects an array but it's out of range
    """
    initial_config = copy.deepcopy(config)  # copy in order to be sure that no change occured

    change = {"page1.initialSettings.coordinates[25]": {"value": "Wow JSON injected!!"}}

    modify_config(config, change)

    assert config == initial_config
