"""Tests that ensure compliance with the published API specification
"""
# stdlib imports
import inspect
import re
import sys

# third-party imports
import pytest
from pysimplesoap.client import SoapClient

# local imports
import niaopendata


def _convert_soap_method_to_python_func(method_name):
    _n = method_name.replace("Get", "", 1)
    _n = re.sub('_JSON$', '', _n)
    _n = re.sub('_JSONP$', '', _n)
    _n = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', _n)
    _n = re.sub('([a-z0-9])([A-Z])', r'\1_\2', _n).lower()
    _n = _n.replace("__", "_")
    return _n


def _check_method_exists(method_name):
    """Check that the given remote method is implemented locally by the
    niaopendata library. The method name is converted from CamelCase to
    snake_case before checking.
    """
    func_name = _convert_soap_method_to_python_func(method_name)
    _f = getattr(niaopendata, func_name, None)
    assert _f is not None
    return _f


def _check_method_signature(method, function):
    _i = method['input']
    if _i is not None:
        assert len(_i.keys()) == 1
        _r_args = _i.values()[0]
    else:
        _r_args = {}
    _l_args = inspect.getargspec(function)
    assert len(_r_args) == len(_l_args.args)


def _check_method_docstring(method, function):
    _r_d = method['documentation']
    _l_d = ' '.join(function.__doc__.split()).split(".")[0]
    assert _l_d in _r_d


def _generate_remote_methods():
    """Retrieve a list of remote endpoint definitions from WSDL endpoints.
    """
    seen_methods = set()
    remote_methods = []
    service_names = ["members", "organisations"]
    for service_name in service_names:
        _wsdl = "http://data.niassembly.gov.uk/{0}.asmx?WSDL".format(service_name)
        client = SoapClient(wsdl=_wsdl)
        service = client.services[service_name]
        methods = service['ports']['{0}HttpGet'.format(service_name)]['operations']
        for method_name, method in sorted(methods.items(), key=lambda tup: tup[0]):
            if _convert_soap_method_to_python_func(method_name) in seen_methods:
                continue
            remote_methods.append(method)
            seen_methods.add(_convert_soap_method_to_python_func(method_name))
    return remote_methods


@pytest.mark.skipif(sys.version_info[0] > 2, reason="requires python2")
def test_remote_method(remote_method):
    """Test that a remote method is implemented correctly
    """
    # check that this method exists locally
    _func = _check_method_exists(remote_method['name'])
    # check that the signature of this method is implemented correctly
    _check_method_signature(remote_method, _func)
    # check that the local docstring matches the documentation for the
    # remote method
    _check_method_docstring(remote_method, _func)


def pytest_generate_tests(metafunc):
    if 'remote_method' not in metafunc.fixturenames:
        return
    if sys.version_info[0] > 2:
        return
    metafunc.parametrize("remote_method", _generate_remote_methods())
