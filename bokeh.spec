#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bokeh
Version  : 1.3.4
Release  : 40
URL      : https://files.pythonhosted.org/packages/89/25/a07183dd96ca22dafe429254985cbf8241ccd35730c5568d6502b3bc6bb7/bokeh-1.3.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/89/25/a07183dd96ca22dafe429254985cbf8241ccd35730c5568d6502b3bc6bb7/bokeh-1.3.4.tar.gz
Summary  : Interactive plots and applications in the browser from Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: bokeh-bin = %{version}-%{release}
Requires: bokeh-license = %{version}-%{release}
Requires: bokeh-python = %{version}-%{release}
Requires: bokeh-python3 = %{version}-%{release}
Requires: Jinja2
Requires: Pillow
Requires: PyYAML
Requires: bkcharts
Requires: numpy
Requires: packaging
Requires: python-dateutil
Requires: six
Requires: tornado
BuildRequires : Jinja2
BuildRequires : Pillow
BuildRequires : PyYAML
BuildRequires : bkcharts
BuildRequires : buildreq-distutils3
BuildRequires : numpy
BuildRequires : packaging
BuildRequires : python-dateutil
BuildRequires : setuptools-python
BuildRequires : six
BuildRequires : tornado

%description
# Bokeh WebGL examples
This directory contains examples that demonstrate the various glyphs that have
support for WebGL rendering. Most of these examples have a testing purpose, e.g.
to compare the appearance of the WebGL glyph with its regular appearance, or to
test another aspect of WebGL (e.g. blending of transparent glyphs).

%package bin
Summary: bin components for the bokeh package.
Group: Binaries
Requires: bokeh-license = %{version}-%{release}

%description bin
bin components for the bokeh package.


%package license
Summary: license components for the bokeh package.
Group: Default

%description license
license components for the bokeh package.


%package python
Summary: python components for the bokeh package.
Group: Default
Requires: bokeh-python3 = %{version}-%{release}

%description python
python components for the bokeh package.


%package python3
Summary: python3 components for the bokeh package.
Group: Default
Requires: python3-core

%description python3
python3 components for the bokeh package.


%prep
%setup -q -n bokeh-1.3.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565271826
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bokeh
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/LICENSE.txt
cp bokeh/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/bokeh_LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3.7/site-packages/tests/__init__.py
rm -f %{buildroot}/usr/lib/python3.7/site-packages/tests/__pycache__/__init__.cpython-36.pyc
rm -f %{buildroot}/usr/lib/python2.7/site-packages/tests/__init__.py
rm -f %{buildroot}/usr/lib/python3.7/site-packages/tests/conftest.py
rm -f %{buildroot}/usr/lib/python2.7/site-packages/tests/conftest.pyc
rm -f %{buildroot}/usr/lib/python2.7/site-packages/tests/conftest.py
rm -f %{buildroot}/usr/lib/python2.7/site-packages/tests/__init__.pyc
rm -f %{buildroot}/usr/lib/python3.7/site-packages/tests/__pycache__/conftest.cpython-36.pyc

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bokeh

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bokeh/LICENSE.txt
/usr/share/package-licenses/bokeh/bokeh_LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
