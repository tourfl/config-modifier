import pytest

from load_change_file import load_change_file


@pytest.fixture
def change_file1():
    with open("./inputs/changes1.txt") as change_file:
        changes_str = change_file.read()

    return changes_str


@pytest.fixture
def change_file2():
    with open("./inputs/changes2.txt") as change_file:
        changes_str = change_file.read()

    return changes_str


def test_load_OK(change_file1):
    changes = load_change_file(change_file1)

    assert changes == {
        "page1.initialSettings.color": "green",
        "page1.available-filters.name-filter.sort": "asc",
    }


def test_load_json_OK(change_file2):
    changes = load_change_file(change_file2)

    assert changes == {
        "page1.initialSettings.coordinates": [24, 30],
        "page1.available-filters.name-filter": {"column": "lastName", "sort": "desc"},
    }
