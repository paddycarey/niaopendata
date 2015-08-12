"""Tests for the niaopendata.questions module
"""
# stdlib imports
import datetime
import random

# third-party imports
from bs4 import BeautifulSoup
from lxml import etree

# local imports
import niaopendata
from test_utils import _check_invalid_list_response
from test_utils import _check_valid_list_response


def _random_date(start, end):
    rand_delta = random.randint(0, int(_total_seconds(end - start)))
    return start + datetime.timedelta(seconds=rand_delta)


def _total_seconds(td):
    # Keep backward compatibility with Python 2.6 which doesn't have the
    # `total_seconds` method on datetime.timedelta objects
    if hasattr(td, 'total_seconds'):
        return td.total_seconds()
    else:
        return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6


def test_question_details():
    """question_details works as expected
    """
    department = niaopendata.department_list_current()[0]
    questions = niaopendata.questions_by_department(department['OrganisationId'])
    rand_smpl = [questions[i] for i in sorted(random.sample(range(len(questions)), 3))]
    for question in rand_smpl:
        r = niaopendata.question_details(question['DocumentId'])
        _check_valid_list_response(r)


def test_questions_by_department():
    """questions_by_department works as expected
    """
    departments = niaopendata.department_list_current()
    rand_smpl = [departments[i] for i in sorted(random.sample(range(len(departments)), 3))]
    for department in rand_smpl:
        r = niaopendata.questions_by_department(department['OrganisationId'])
        _check_valid_list_response(r)


def test_questions_by_member():
    """questions_by_member works as expected
    """
    members = niaopendata.all_current_members()
    rand_smpl = [members[i] for i in sorted(random.sample(range(len(members)), 3))]
    for member in rand_smpl:
        r = niaopendata.questions_by_member(member['PersonId'])
        _check_valid_list_response(r)


def test_questions_by_search_text():
    """questions_by_search_text works as expected
    """
    for term in ["ane", "Watson", "Kell"]:
        r = niaopendata.questions_by_search_text(term)
        _check_valid_list_response(r)
    for term in ["", "asdlkj", 21408]:
        r = niaopendata.questions_by_search_text(term)
        _check_invalid_list_response(r)


def test_questions_for_oral_answer_answered_in_range():
    """questions_for_oral_answer_answered_in_range works as expected
    """
    for _start in [_random_date(datetime.datetime(2008, 1, 1), datetime.datetime(2014, 1, 1))]:
        _end = _start + datetime.timedelta(days=365)
        r = niaopendata.questions_for_oral_answer_answered_in_range(_start, _end)
        _check_valid_list_response(r)
    for term in ["", "asdlkj", 21408]:
        r = niaopendata.questions_for_oral_answer_answered_in_range(term, term)
        _check_invalid_list_response(r)


def test_questions_for_oral_answer_tabled_in_range():
    """department_list_current works as expected
    """
    for _start in [_random_date(datetime.datetime(2008, 1, 1), datetime.datetime(2014, 1, 1))]:
        _end = _start + datetime.timedelta(days=365)
        r = niaopendata.questions_for_oral_answer_tabled_in_range(_start, _end)
        _check_valid_list_response(r)
    for term in ["", "asdlkj", 21408]:
        r = niaopendata.questions_for_oral_answer_tabled_in_range(term, term)
        _check_invalid_list_response(r)


def test_questions_for_written_answer_answered_in_range():
    """questions_for_written_answer_answered_in_range works as expected
    """
    for _start in [_random_date(datetime.datetime(2008, 1, 1), datetime.datetime(2014, 1, 1))]:
        _end = _start + datetime.timedelta(days=365)
        r = niaopendata.questions_for_written_answer_answered_in_range(_start, _end)
        _check_valid_list_response(r)
    for term in ["", "asdlkj", 21408]:
        r = niaopendata.questions_for_written_answer_answered_in_range(term, term)
        _check_invalid_list_response(r)


def test_questions_for_written_answer_tabled_in_range():
    """questions_for_written_answer_tabled_in_range works as expected
    """
    for _start in [_random_date(datetime.datetime(2008, 1, 1), datetime.datetime(2014, 1, 1))]:
        _end = _start + datetime.timedelta(days=365)
        r = niaopendata.questions_for_written_answer_tabled_in_range(_start, _end)
        _check_valid_list_response(r)
    for term in ["", "asdlkj", 21408]:
        r = niaopendata.questions_for_written_answer_tabled_in_range(term, term)
        _check_invalid_list_response(r)


def test_written_answer_html():
    """written_answer_html works as expected
    """
    for _start in [_random_date(datetime.datetime(2008, 1, 1), datetime.datetime(2014, 1, 1))]:
        _end = _start + datetime.timedelta(days=365)
        questions = niaopendata.questions_for_written_answer_answered_in_range(_start, _end)
        rand_smpl = [questions[i] for i in sorted(random.sample(range(len(questions)), 3))]
        for question in rand_smpl:
            html = niaopendata.written_answer_html(question['DocumentId'])
            # use beautifulsoup to validate that the returned string is actually HTML
            assert bool(BeautifulSoup(html, "html.parser").find())


def test_written_answer_open_xml():
    """written_answer_open_xml works as expected
    """
    for _start in [_random_date(datetime.datetime(2008, 1, 1), datetime.datetime(2014, 1, 1))]:
        _end = _start + datetime.timedelta(days=365)
        questions = niaopendata.questions_for_written_answer_answered_in_range(_start, _end)
        rand_smpl = [questions[i] for i in sorted(random.sample(range(len(questions)), 3))]
        for question in rand_smpl:
            open_xml = niaopendata.written_answer_open_xml(question['DocumentId'])
            # use ElementTree to validate that the returned string is actually XML
            try:
                etree.fromstring(open_xml)
            except Exception as e:
                assert e is None
