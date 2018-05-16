#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bokeh
Version  : 0.12.15
Release  : 21
URL      : https://pypi.python.org/packages/ad/67/82f17df7d1f4b9e81c9263c1a1dc3897c43cf5a9461872f9054517331f77/bokeh-0.12.15.tar.gz
Source0  : https://pypi.python.org/packages/ad/67/82f17df7d1f4b9e81c9263c1a1dc3897c43cf5a9461872f9054517331f77/bokeh-0.12.15.tar.gz
Summary  : Interactive plots and applications in the browser from Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: bokeh-bin
Requires: bokeh-python3
Requires: bokeh-python
Requires: Jinja2
Requires: PyYAML
Requires: bkcharts
Requires: numpy
Requires: packaging
Requires: python-dateutil
Requires: six
Requires: tornado
BuildRequires : bkcharts
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-python

%description
Bokeh
=====
*Bokeh is a fiscally sponsored project of [NumFOCUS](http://numfocus.org), a nonprofit dedicated to supporting the open-source scientific computing community. If you like Bokeh and would like to support our mission, please consider [making a donation](https://www.flipcause.com/secure/cause_pdetails/MzE5NjE=).*

%package bin
Summary: bin components for the bokeh package.
Group: Binaries

%description bin
bin components for the bokeh package.


%package python
Summary: python components for the bokeh package.
Group: Default
Requires: bokeh-python3

%description python
python components for the bokeh package.


%package python3
Summary: python3 components for the bokeh package.
Group: Default
Requires: python3-core

%description python3
python3 components for the bokeh package.


%prep
%setup -q -n bokeh-0.12.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523556489
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bokeh

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
