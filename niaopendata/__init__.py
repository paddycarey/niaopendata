# -*- coding: utf-8 -*-

# future imports
from __future__ import absolute_import

# local imports
from .members import all_current_committee_chairs
from .members import all_current_members
from .members import all_current_members_by_given_constituency_id
from .members import all_current_members_by_given_party_id
from .members import all_current_members_by_surname_search
from .members import all_current_ministers
from .members import all_member_contact_details
from .members import all_member_roles
from .members import all_members_by_given_date
from .members import member_contact_details_by_person_id
from .members import member_roles_by_person_id
from .questions import question_details
from .questions import questions_by_department
from .questions import questions_by_member
from .questions import questions_by_search_text
from .questions import questions_for_oral_answer_answered_in_range
from .questions import questions_for_oral_answer_tabled_in_range
from .questions import questions_for_written_answer_answered_in_range
from .questions import questions_for_written_answer_tabled_in_range
from .questions import written_answer_html
from .questions import written_answer_open_xml
from .organisations import all_party_groups_list_current
from .organisations import committees_list_current_ad_hoc
from .organisations import committees_list_current_other
from .organisations import committees_list_current_standing
from .organisations import committees_list_current_statutory
from .organisations import department_list_current
from .organisations import organisation_list_current
from .organisations import parties_list_current

# all of the following objects will be imported if the caller does
# `from niaopendata import *` (don't)
__all__ = [

    # Members Web Service
    'all_current_committee_chairs',
    'all_current_members',
    'all_current_members_by_given_constituency_id',
    'all_current_members_by_given_party_id',
    'all_current_members_by_surname_search',
    'all_current_ministers',
    'all_member_contact_details',
    'all_member_roles',
    'all_members_by_given_date',
    'member_contact_details_by_person_id',
    'member_roles_by_person_id',

    # Questions Web Service
    'question_details',
    'questions_by_department',
    'questions_by_member',
    'questions_by_search_text',
    'questions_for_oral_answer_answered_in_range',
    'questions_for_oral_answer_tabled_in_range',
    'questions_for_written_answer_answered_in_range',
    'questions_for_written_answer_tabled_in_range',
    'written_answer_html',
    'written_answer_open_xml',

    # Organisations Web Service
    'all_party_groups_list_current',
    'committees_list_current_ad_hoc',
    'committees_list_current_other',
    'committees_list_current_standing',
    'committees_list_current_statutory',
    'department_list_current',
    'organisation_list_current',
    'parties_list_current',

]
