"""Tests for the niaopendata.members module
"""
# stdlib imports
import datetime

# local imports
import niaopendata
from test_utils import _check_invalid_list_response
from test_utils import _check_valid_list_response


def test_all_current_committee_chairs():
    """all_current_committee_chairs works as expected
    """
    r = niaopendata.all_current_committee_chairs()
    _check_valid_list_response(r)


def test_all_current_members():
    """all_current_members works as expected
    """
    r = niaopendata.all_current_members()
    _check_valid_list_response(r)


def test_all_current_members_by_given_constituency_id():
    """all_current_members_by_given_constituency_id works as expected
    """
    for i in set([x["ConstituencyId"] for x in niaopendata.all_current_members()]):
        r = niaopendata.all_current_members_by_given_constituency_id(i)
        _check_valid_list_response(r)
    for i in ["", "asdlkj", 21408]:
        r = niaopendata.all_current_members_by_given_constituency_id(i)
        _check_invalid_list_response(r)


def test_all_current_members_by_given_party_id():
    """all_current_members_by_given_party_id works as expected
    """
    for i in set([x["PartyOrganisationId"] for x in niaopendata.all_current_members()]):
        r = niaopendata.all_current_members_by_given_party_id(i)
        _check_valid_list_response(r)
    for i in ["", "asdlkj", 21408]:
        r = niaopendata.all_current_members_by_given_party_id(i)
        _check_invalid_list_response(r)


def test_all_current_members_by_surname_search():
    """all_current_members_by_surname_search works as expected
    """
    for term in ["ane", "Watson", "Kell"]:
        r = niaopendata.all_current_members_by_surname_search(term)
        _check_valid_list_response(r)
    for term in ["", "asdlkj", 21408]:
        r = niaopendata.all_current_members_by_surname_search(term)
        _check_invalid_list_response(r)


def test_all_current_ministers():
    """all_current_ministers works as expected
    """
    r = niaopendata.all_current_ministers()
    _check_valid_list_response(r)


def test_all_member_contact_details():
    """all_member_contact_details works as expected
    """
    r = niaopendata.all_member_contact_details()
    _check_valid_list_response(r)


def test_all_member_roles():
    """all_member_roles works as expected
    """
    r = niaopendata.all_member_roles()
    _check_valid_list_response(r)


def test_all_members_by_given_date():
    """all_members_by_given_date works as expected
    """
    for term in [datetime.datetime.utcnow(), datetime.datetime(2009, 3, 12)]:
        r = niaopendata.all_members_by_given_date(term)
        _check_valid_list_response(r)
    for term in ["", "asdlkj", 21408]:
        r = niaopendata.all_members_by_given_date(term)
        _check_invalid_list_response(r)


def test_member_contact_details_by_person_id():
    """member_contact_details_by_person_id works as expected
    """
    for i in [127, 67, "8"]:
        r = niaopendata.member_contact_details_by_person_id(i)
        _check_valid_list_response(r)
    for i in ["", "asdlkj", 21408]:
        r = niaopendata.member_contact_details_by_person_id(i)
        _check_invalid_list_response(r)


def test_member_roles_by_person_id():
    """member_roles_by_person_id works as expected
    """
    for i in [127, 67, "8"]:
        r = niaopendata.member_roles_by_person_id(i)
        _check_valid_list_response(r)
    for i in ["", "asdlkj", 21408]:
        r = niaopendata.member_roles_by_person_id(i)
        _check_invalid_list_response(r)
