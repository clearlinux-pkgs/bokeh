#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bokeh
Version  : 0.12.14
Release  : 16
URL      : https://pypi.python.org/packages/f3/b1/69d6b3544de4d31d7b735e6e3e075afc8ef962c4e1bce93cb4252632122f/bokeh-0.12.14.tar.gz
Source0  : https://pypi.python.org/packages/f3/b1/69d6b3544de4d31d7b735e6e3e075afc8ef962c4e1bce93cb4252632122f/bokeh-0.12.14.tar.gz
Summary  : Interactive plots and applications in the browser from Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: bokeh-bin
Requires: bokeh-legacypython
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

%description
Bokeh
=====
<table>
<tr>
<td>Latest Release</td>
<td><img src="https://badge.fury.io/gh/bokeh%2Fbokeh.svg" alt="latest release" /></td>
</tr>
<tr>
<td>License</td>
<td>
<a href="https://github.com/bokeh/bokeh/blob/master/LICENSE.txt">
<img src="https://img.shields.io/github/license/bokeh/bokeh.svg" alt="Bokeh license" />
</a>
</td>
</tr>
<tr>
<td>Build Status</td>
<td>
<a href="https://travis-ci.org/bokeh/bokeh">
<img src="https://travis-ci.org/bokeh/bokeh.svg?branch=master" alt="build status" />
</a>
</td>
</tr>
<tr>
<td>Static Analyis</td>
<td>
<a href="https://bettercodehub.com/edge/badge/bokeh/bokeh?branch=master">
<img src='https://bettercodehub.com/edge/badge/bokeh/bokeh?branch=master'>
</a>
</td>
</tr>
<tr>
<td>Conda</td>
<td>
<a href="https://bokeh.pydata.org/en/latest/docs/installation.html">
<img src="http://pubbadges.s3-website-us-east-1.amazonaws.com/pkgs-downloads-bokeh.png" alt="conda downloads" />
</a>
</td>
</tr>
<tr>
<td>PyPI</td>
<td>
<img src="https://bokeh.pydata.org/pip-bokeh-badge.png" />
</td>
</tr>
<tr>
<td>Live Tutorial</td>
<td>
<a href="https://mybinder.org/v2/gh/bokeh/bokeh-notebooks/master?filepath=tutorial%2F00%20-%20Introduction%20and%20Setup.ipynb">
<img src="https://mybinder.org/badge.svg" />
</a>
</td>
</tr>
<tr>
<td>Gitter</td>
<td>
<a href="https://gitter.im/bokeh/bokeh?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge">
<img src="https://badges.gitter.im/bokeh/bokeh.svg" />
</a>
</td>
</tr>
<tr>
<td>Twitter</td>
<td>
<a href="https://twitter.com/BokehPlots">
<img src="https://img.shields.io/twitter/follow/bokehplots.svg?style=social&label=Follow" />
</a>
</td>
</tr>
</table>

%package bin
Summary: bin components for the bokeh package.
Group: Binaries

%description bin
bin components for the bokeh package.


%package legacypython
Summary: legacypython components for the bokeh package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the bokeh package.


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
%setup -q -n bokeh-0.12.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1518037063
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1518037063
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bokeh

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
