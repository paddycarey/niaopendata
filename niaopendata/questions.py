# -*- coding: utf-8 -*-
"""The functions in this file provide access to the Questions Web Service of
the Northern Ireland Assembly Open Data API.
"""
# future imports
from __future__ import absolute_import

# third-party imports
import xmltodict

# local imports
from .api import ParseError
from .api import _call_service
from .api import _parse_list_response
from .api import _parse_service_response


def _call_questions_service(endpoint, **kwargs):
    """Call the questions service using the given endpoint. All additional
    kwargs will be serialised in the query string used when calling the service.
    """
    try:
        resp = _call_service("questions", endpoint, **kwargs)
        return _parse_service_response(resp)
    except ParseError:
        return {}


def question_details(document_id):
    """Returns all details for specific Question.
    """
    q_args = {"documentId": str(document_id)}

    resp = _call_questions_service("GetQuestionDetails", **q_args)
    return _parse_list_response(resp, "QuestionsList", "Question")


def questions_by_department(department_id):
    """Returns a list of all Questions tabled to a specific Department.
    """
    q_args = {"departmentId": str(department_id)}

    resp = _call_questions_service("GetQuestionsByDepartment", **q_args)
    return _parse_list_response(resp, "QuestionsList", "Question")


def questions_by_member(person_id):
    """Returns a list of all Questions tabled by a specific Member.
    """
    q_args = {"personId": str(person_id)}

    resp = _call_questions_service("GetQuestionsByMember", **q_args)
    return _parse_list_response(resp, "QuestionsList", "Question")


def questions_by_search_text(term):
    """Returns a list of all Questions where Question Text contains specified
    search term. Search term must be 3 characters or more.
    """
    term = str(term)
    if len(term) < 3:
        return []
    q_args = {"searchText": term}

    resp = _call_questions_service("GetQuestionsBySearchText", **q_args)
    return _parse_list_response(resp, "QuestionsList", "Question")


def questions_for_oral_answer_answered_in_range(start, end):
    """Returns a list of all Questions for Oral Answer, and links to Hansard
    Answers, answered in date range.
    """
    try:
        _start = start.isoformat()
    except AttributeError:
        return []
    try:
        _end = end.isoformat()
    except AttributeError:
        return []

    q_args = {'startDate': _start, 'endDate': _end}
    resp = _call_questions_service("GetQuestionsForOralAnswer_AnsweredInRange", **q_args)
    return _parse_list_response(resp, "QuestionsList", "Question")


def questions_for_oral_answer_tabled_in_range(start, end):
    """Returns a list of all Questions for Oral Answer tabled in date range.
    """
    try:
        _start = start.isoformat()
    except AttributeError:
        return []
    try:
        _end = end.isoformat()
    except AttributeError:
        return []

    q_args = {'startDate': _start, 'endDate': _end}
    resp = _call_questions_service("GetQuestionsForOralAnswer_TabledInRange", **q_args)
    return _parse_list_response(resp, "QuestionsList", "Question")


def questions_for_written_answer_answered_in_range(start, end):
    """Returns a list of all Questions for Written Answer, and respective
    Answers, answered in date range.
    """
    try:
        _start = start.isoformat()
    except AttributeError:
        return []
    try:
        _end = end.isoformat()
    except AttributeError:
        return []

    q_args = {'startDate': _start, 'endDate': _end}
    resp = _call_questions_service("GetQuestionsForWrittenAnswer_AnsweredInRange", **q_args)
    return _parse_list_response(resp, "QuestionsList", "Question")


def questions_for_written_answer_tabled_in_range(start, end):
    """Returns a list of all Questions for Written Answer tabled in date range.
    """
    try:
        _start = start.isoformat()
    except AttributeError:
        return []
    try:
        _end = end.isoformat()
    except AttributeError:
        return []

    q_args = {'startDate': _start, 'endDate': _end}
    resp = _call_questions_service("GetQuestionsForWrittenAnswer_TabledInRange", **q_args)
    return _parse_list_response(resp, "QuestionsList", "Question")


def written_answer_html(document_id):
    """Returns Html format of Written Answer for specific Question.
    """
    q_args = {"documentId": str(document_id)}

    resp = _call_service("questions", "GetWrittenAnswerHtml", **q_args)
    # TODO: should this return a beautifulsoup instance instead of a string?
    return xmltodict.parse(resp.text)['string']['#text']


def written_answer_open_xml(document_id):
    """Returns OpenXml format of Written Answer for specific Question.
    """
    q_args = {"documentId": str(document_id)}

    resp = _call_service("questions", "GetWrittenAnswerOpenXml", **q_args)
    # TODO: Need to figure out how to reconstruct a proper `.docx` file here
    return resp.content
