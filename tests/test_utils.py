"""Common utilities used across multiple test modules
"""


def _check_invalid_list_response(response):
    assert isinstance(response, list)
    assert len(response) == 0


def _check_valid_list_response(response):
    assert isinstance(response, list)
    assert len(response) > 0
