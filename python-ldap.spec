#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-ldap
Version  : 3.2.0
Release  : 22
URL      : https://files.pythonhosted.org/packages/ea/93/596f875e003c770447f4b99267820a0c769dd2dc3ae3ed19afe460fcbad0/python-ldap-3.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ea/93/596f875e003c770447f4b99267820a0c769dd2dc3ae3ed19afe460fcbad0/python-ldap-3.2.0.tar.gz
Summary  : LDAP client API for Python
Group    : Development/Tools
License  : Python-2.0
Requires: python-ldap-license = %{version}-%{release}
Requires: python-ldap-python = %{version}-%{release}
Requires: python-ldap-python3 = %{version}-%{release}
Requires: pyasn1
Requires: pyasn1-modules
BuildRequires : buildreq-distutils3
BuildRequires : openldap-dev
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyasn1
BuildRequires : pyasn1-modules
BuildRequires : pytest
BuildRequires : tox
BuildRequires : util-linux
BuildRequires : virtualenv
Patch1: 0001-Remove-SASL-dependency.patch
Patch2: 0004-Custom-location-for-SLAPD.patch
Patch3: 0005-Add-stateless-dir-for-openldap-schema.patch

%description
---------------------------------------
python-ldap: LDAP client API for Python
---------------------------------------

%package license
Summary: license components for the python-ldap package.
Group: Default

%description license
license components for the python-ldap package.


%package python
Summary: python components for the python-ldap package.
Group: Default
Requires: python-ldap-python3 = %{version}-%{release}

%description python
python components for the python-ldap package.


%package python3
Summary: python3 components for the python-ldap package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-ldap package.


%prep
%setup -q -n python-ldap-3.2.0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571690736
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-ldap
cp %{_builddir}/python-ldap-3.2.0/LICENCE %{buildroot}/usr/share/package-licenses/python-ldap/1b4cf76aa889e8d20628b6fb45886a2c745cea19
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-ldap/1b4cf76aa889e8d20628b6fb45886a2c745cea19

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
