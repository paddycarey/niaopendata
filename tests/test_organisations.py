"""Tests for the niaopendata.organisations module
"""
# local imports
import niaopendata
from test_utils import _check_valid_list_response


def test_all_party_groups_list_current():
    """all_party_groups_list_current works as expected
    """
    r = niaopendata.all_party_groups_list_current()
    _check_valid_list_response(r)


def test_committees_list_current_ad_hoc():
    """committees_list_current_ad_hoc works as expected
    """
    r = niaopendata.committees_list_current_ad_hoc()
    _check_valid_list_response(r)


def test_committees_list_current_other():
    """committees_list_current_other works as expected
    """
    r = niaopendata.committees_list_current_other()
    _check_valid_list_response(r)


def test_committees_list_current_standing():
    """committees_list_current_standing works as expected
    """
    r = niaopendata.committees_list_current_standing()
    _check_valid_list_response(r)


def test_committees_list_current_statutory():
    """committees_list_current_statutory works as expected
    """
    r = niaopendata.committees_list_current_statutory()
    _check_valid_list_response(r)


def test_department_list_current():
    """department_list_current works as expected
    """
    r = niaopendata.department_list_current()
    _check_valid_list_response(r)


def test_organisation_list_current():
    """organisation_list_current works as expected
    """
    r = niaopendata.organisation_list_current()
    _check_valid_list_response(r)


def test_parties_list_current():
    """parties_list_current works as expected
    """
    r = niaopendata.parties_list_current()
    _check_valid_list_response(r)
