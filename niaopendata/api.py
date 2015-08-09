# -*- coding: utf-8 -*-
"""Common API functionality shared between all niaopendata services
"""
# future imports
from __future__ import absolute_import

# Third party imports
import requests
import xmltodict


def _call_service(service, endpoint, **kwargs):

    # Base URL for all API calls
    base_url = 'http://data.niassembly.gov.uk'
    url = "{0}/{1}.asmx/{2}".format(base_url, service, endpoint)
    resp = requests.get(url, params=kwargs)
    return _parse_service_response(resp)


def _parse_list_response(response, outer_key, inner_key):
    """Responses from the niaopendata service aren't entirely consistent across
    the board, so we can't rely on a single consistent format even for a single
    endpoint. This function checks and can parse all known return formats into
    simple lists suitable for returning to callers.
    """
    outer = response.get(outer_key)
    if outer is None:
        return []
    inner = outer[inner_key]
    if isinstance(inner, dict):
        return [inner]
    return inner


def _parse_service_response(response):
    """Parses a given service response using an appropriate parser for the
    given mimetype
    """
    mimetype = response.headers['content-type'].split(";")[0]
    parsers = {
        "application/json": _parse_service_response_json,
        "text/plain": _parse_service_response_plain,
        "text/xml": _parse_service_response_xml,
    }
    return parsers[mimetype](response)


class ParseError(Exception):
    pass


def _parse_service_response_json(response):
    """Parse service response as JSON
    """
    return response.json()


def _parse_service_response_plain(response):
    """A text/plain response from the API indicates something has gone horribly
    wrong, all we can reasonably do is raise an appropriate exception.
    """
    raise ParseError("text/plain response returned from API")


def _parse_service_response_xml(response):
    """Parse service response as XML
    """
    # parse the xml into an ordered dict and return it
    return xmltodict.parse(response.text)
