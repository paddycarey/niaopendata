# -*- coding: utf-8 -*-
"""The functions in this file provide access to the Organisations Web Service
of the Northern Ireland Assembly Open Data API.
"""
# future imports
from __future__ import absolute_import

# local imports
from .api import ParseError
from .api import _call_service
from .api import _parse_list_response


def _call_organisations_service(endpoint, **kwargs):
    """Call the organisations service using the given endpoint. All additional
    kwargs will be serialised in the query string used when calling the service
    """
    try:
        return _call_service("organisations", endpoint, **kwargs)
    except ParseError:
        return {}


def all_party_groups_list_current():
    """Returns a list of all All Party Groups as of today's date.
    """
    resp = _call_organisations_service("GetAllPartyGroupsListCurrent")
    return _parse_list_response(resp, "OrganisationsList", "Organisation")


def committees_list_current_ad_hoc():
    """Returns a list of all Ad Hoc Committees as of today's date.
    """
    resp = _call_organisations_service("GetCommitteesListCurrent_AdHoc")
    return _parse_list_response(resp, "OrganisationsList", "Organisation")


def committees_list_current_other():
    """Returns a list of all Other Committees as of today's date.
    """
    resp = _call_organisations_service("GetCommitteesListCurrent_Other")
    return _parse_list_response(resp, "OrganisationsList", "Organisation")


def committees_list_current_standing():
    """Returns a list of all Standing Committees as of today's date.
    """
    resp = _call_organisations_service("GetCommitteesListCurrent_Standing")
    return _parse_list_response(resp, "OrganisationsList", "Organisation")


def committees_list_current_statutory():
    """Returns a list of all Statutory Committees as of today's date.
    """
    resp = _call_organisations_service("GetCommitteesListCurrent_Statutory")
    return _parse_list_response(resp, "OrganisationsList", "Organisation")


def department_list_current():
    """Returns a list of all Departments as of today's date.
    """
    resp = _call_organisations_service("GetDepartmentListCurrent")
    return _parse_list_response(resp, "OrganisationsList", "Organisation")


def organisation_list_current():
    """Returns a list of all Organisations as of today's date.
    """
    resp = _call_organisations_service("GetOrganisationListCurrent")
    return _parse_list_response(resp, "OrganisationsList", "Organisation")


def parties_list_current():
    """Returns a list of all Political Parties as of today's date.
    """
    resp = _call_organisations_service("GetPartiesListCurrent")
    return _parse_list_response(resp, "OrganisationsList", "Organisation")
