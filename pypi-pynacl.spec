#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x235AE5F129F9ED98 (paul.l.kehrer@gmail.com)
#
Name     : pypi-pynacl
Version  : 1.4.0
Release  : 39
URL      : https://files.pythonhosted.org/packages/cf/5a/25aeb636baeceab15c8e57e66b8aa930c011ec1c035f284170cacb05025e/PyNaCl-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/cf/5a/25aeb636baeceab15c8e57e66b8aa930c011ec1c035f284170cacb05025e/PyNaCl-1.4.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/cf/5a/25aeb636baeceab15c8e57e66b8aa930c011ec1c035f284170cacb05025e/PyNaCl-1.4.0.tar.gz.asc
Summary  : Python binding to the Networking and Cryptography (NaCl) library
Group    : Development/Tools
License  : Apache-2.0 ISC
Requires: pypi-pynacl-license = %{version}-%{release}
Requires: pypi-pynacl-python = %{version}-%{release}
Requires: pypi-pynacl-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: PyNaCl
Provides: PyNaCl-python
Provides: PyNaCl-python3
BuildRequires : cffi
BuildRequires : llvm
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(cffi)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(six)
BuildRequires : pypi(wheel)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
===============================================
PyNaCl: Python binding to the libsodium library
===============================================

%package license
Summary: license components for the pypi-pynacl package.
Group: Default

%description license
license components for the pypi-pynacl package.


%package python
Summary: python components for the pypi-pynacl package.
Group: Default
Requires: pypi-pynacl-python3 = %{version}-%{release}

%description python
python components for the pypi-pynacl package.


%package python3
Summary: python3 components for the pypi-pynacl package.
Group: Default
Requires: python3-core
Provides: pypi(pynacl)
Requires: pypi(cffi)
Requires: pypi(six)

%description python3
python3 components for the pypi-pynacl package.


%prep
%setup -q -n PyNaCl-1.4.0
cd %{_builddir}/PyNaCl-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641476715
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pynacl
cp %{_builddir}/PyNaCl-1.4.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pynacl/43a3a49bd7af636c923a5ae475395b8e29320529
cp %{_builddir}/PyNaCl-1.4.0/src/libsodium/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pynacl/d3d81d32b0e1c11e180faffe1c9f1fedc7d04f58
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pynacl/43a3a49bd7af636c923a5ae475395b8e29320529
/usr/share/package-licenses/pypi-pynacl/d3d81d32b0e1c11e180faffe1c9f1fedc7d04f58

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
