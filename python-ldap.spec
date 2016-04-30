#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-ldap
Version  : 2.4.25
Release  : 15
URL      : https://pypi.python.org/packages/source/p/python-ldap/python-ldap-2.4.25.tar.gz
Source0  : https://pypi.python.org/packages/source/p/python-ldap/python-ldap-2.4.25.tar.gz
Summary  : Python modules for implementing LDAP clients
Group    : Development/Tools
License  : Python-2.0
Requires: python-ldap-python
BuildRequires : openldap-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools
Patch1: disable-sasl.patch

%description
---------------------------------------
python-ldap: LDAP client API for Python
---------------------------------------

%package python
Summary: python components for the python-ldap package.
Group: Default

%description python
python components for the python-ldap package.


%prep
%setup -q -n python-ldap-2.4.25
%patch1 -p1

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
