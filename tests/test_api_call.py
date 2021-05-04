import pytest
from src import brewery_api


def test_correct_state_returns_result():
    assert len(brewery_api.get_breweries_by_state('ohio')) > 0


def test_incorrect_state_returns_no_result():
    assert len(brewery_api.get_breweries_by_state('not a real state')) == 0


def test_incorrect_argument_raises_error():
    dummy_args = ['a', 'b', 'c']
    with pytest.raises(ValueError):
        brewery_api.main(dummy_args)
