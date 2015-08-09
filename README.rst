===============================
niaopendata
===============================

.. image:: https://img.shields.io/pypi/v/niaopendata.svg?style=flat
    :target: https://pypi.python.org/pypi/niaopendata/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/travis/paddycarey/niaopendata/master.png?style=flat
    :target: https://travis-ci.org/paddycarey/niaopendata
    :alt: Travis CI build status

niaopendata is a Python client library for accessing the `Northern Ireland Assembly Open Data API <http://data.niassembly.gov.uk/>`_. niaopendata has a full test suite and aims to have 100% coverage of the API. Tests exist both to ensure that the library is working as expected, and also that the library complies with and fully implements the API specification.

niaopendata supports Python 2.6, 2.7, PyPy, 3.3 and 3.4 (and probably later versions too, but I haven't tested on those).

* Free software: MIT license
* Documentation: https://github.com/paddycarey/niaopendata



Installation
------------

Distribute & Pip
~~~~~~~~~~~~~~~~

Installing niaopendata is simple with `pip <http://www.pip-installer.org/>`_::

    $ pip install niaopendata

or, with `easy_install <http://pypi.python.org/pypi/setuptools>`_::

    $ easy_install niaopendata

But, you really `shouldn't do that <http://www.pip-installer.org/en/latest/other-tools.html#pip-compared-to-easy-install>`_.


Get the Code
~~~~~~~~~~~~

niaopendata is actively developed on GitHub, where the code is `always available <https://github.com/paddycarey/niaopendata>`_.

You can either clone the public repository::

    $ git clone git://github.com/paddycarey/niaopendata.git

Or download the `tarball <https://github.com/paddycarey/niaopendata/tarball/master>`_::

    $ curl -OL https://github.com/paddycarey/niaopendata/tarball/master

Once you have a copy of the source, you can embed it in your Python package, or install it into your site-packages easily::

    $ python setup.py install



Usage
-----

niaopendata aims to provide a simple, pythonic interface to Northern Ireland Assembly Open Data API. It has been designed to be easy to use, and aims to provide full coverage of the API with a consistent interface.

First you'll need to import niaopendata.::

    import niaopendata


Retrieving data from the API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As an example of what is possible, it is easy to retrieve a list of all members.::

    >>> niaopendata.all_current_members()
    [
        OrderedDict([
            (u'PersonId', u'307'),
            (u'AffiliationId', u'2482'),
            (u'MemberName', u'Agnew, Steven'),
            (u'MemberLastName', u'Agnew'),
            (u'MemberFirstName', u'Steven'),
            (u'MemberFullDisplayName', u'Mr S Agnew'),
            (u'MemberSortName', u'AgnewSteven'),
            (u'MemberTitle', u'MLA - North Down'),
            (u'PartyName', u'Green Party'),
            (u'PartyOrganisationId', u'111'),
            (u'ConstituencyName', u'North Down'),
            (u'ConstituencyId', u'11'),
            (u'MemberImgUrl', u'http://aims.niassembly.gov.uk/images/mla/307_s.jpg'),
            (u'MemberPrefix', u'Mr')
        ]),
        ...
    ]

    >>> len(niaopendata.all_current_members())
    107


Full API documentation
~~~~~~~~~~~~~~~~~~~~~~

Full documentation is a work in progress, but the code itself should be easy to follow. All public functions are explicitly imported in ``__init__.py`` and all functions have appropriate docstrings.


Testing
-------

niaopendata has a full test suite. Assuming you have a full source checkout of the niaopendata repository, running the tests is simple with ``tox``::

    $ pip install tox
    $ tox

It is recommended that you use a virtualenv when developing or running the tests to ensure that system libraries do not interfere with the tests.

**TIP:** If you're using Ubuntu, you can find older/newer versions of python than the one shipped with your distribution `here <https://launchpad.net/~fkrull/+archive/ubuntu/deadsnakes>`_. You can install as many as you like side by side without affecting your default python install.


Copyright & License
-------------------

| Copyright © 2015 Patrick Carey (https://github.com/paddycarey)
| Licensed under the **MIT** license.
