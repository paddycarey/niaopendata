# -*- coding: utf-8 -*-
"""The functions in this file provide access to the Members Web Service of the
Northern Ireland Assembly Open Data API.
"""
# future imports
from __future__ import absolute_import

# local imports
from .api import ParseError
from .api import _call_service
from .api import _parse_list_response


def _call_members_service(endpoint, **kwargs):
    """Call the members service using the given endpoint. All additional kwargs
    will be serialised in the query string used when calling the service.
    """
    try:
        return _call_service("members", endpoint, **kwargs)
    except ParseError:
        return {}


def all_current_committee_chairs():
    """Returns a list of all current Committee Chairs as of today's date
    """
    resp = _call_members_service("GetAllCurrentCommitteeChairs")
    return _parse_list_response(resp, "AllCommitteeChairsList", "CommitteeChair")


def all_current_members():
    """Returns a list of all current MLAs as of today's date
    """
    resp = _call_members_service("GetAllCurrentMembers")
    return _parse_list_response(resp, "AllMembersList", "Member")


def all_current_members_by_given_constituency_id(constituency_id):
    """Returns a list of all current MLAs in a specific constituency
    """
    q_args = {"constituencyId": str(constituency_id)}

    resp = _call_members_service("GetAllCurrentMembersByGivenConstituencyId", **q_args)
    return _parse_list_response(resp, "AllMembersList", "Member")


def all_current_members_by_given_party_id(party_id):
    """Returns a list of all current MLAs in a specific party
    """
    q_args = {"partyId": str(party_id)}

    resp = _call_members_service("GetAllCurrentMembersByGivenPartyId", **q_args)
    return _parse_list_response(resp, "AllMembersList", "Member")


def all_current_members_by_surname_search(term):
    """Returns a list of all current MLAs by surname search. Search term must
    be 3 characters or more
    """
    term = str(term)
    if len(term) < 3:
        return []
    q_args = {"searchText": term}

    resp = _call_members_service("GetAllCurrentMembersBySurnameSearch", **q_args)
    return _parse_list_response(resp, "AllMembersList", "Member")


def all_current_ministers():
    """Returns a list of all current Ministers as of today's date
    """
    resp = _call_members_service("GetAllCurrentMinisters")
    return _parse_list_response(resp, "AllMinistersList", "Minister")


def all_member_contact_details():
    """Returns a list of Member's contact details
    """
    resp = _call_members_service("GetAllMemberContactDetails")
    return _parse_list_response(resp, "AllMembersList", "Member")


def all_member_roles():
    """Returns a list of all roles held by all MLAs
    """
    resp = _call_members_service("GetAllMemberRoles")
    return _parse_list_response(resp, "AllMembersRoles", "Role")


def all_members_by_given_date(_datetime):
    """Returns a list of all MLAs on a specific date
    """
    try:
        _datetime = _datetime.isoformat()
    except AttributeError:
        return []

    q_args = {"specificDate": _datetime}
    resp = _call_members_service("GetAllMembersByGivenDate", **q_args)
    return _parse_list_response(resp, "AllMembersList", "Member")


def member_contact_details_by_person_id(person_id):
    """Returns a list of Member's contact details
    """
    q_args = {"personId": str(person_id)}
    resp = _call_members_service("GetMemberContactDetailsByPersonId", **q_args)
    return _parse_list_response(resp, "AllMembersList", "Member")


def member_roles_by_person_id(person_id):
    """Returns a list of all roles held by specific MLA
    """
    q_args = {"personId": str(person_id)}
    resp = _call_members_service("GetMemberRolesByPersonId", **q_args)
    return _parse_list_response(resp, "AllMembersRoles", "Role")
