#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bokeh
Version  : 1.1.0
Release  : 34
URL      : https://files.pythonhosted.org/packages/55/3b/14ab63362486a2c9593bff66b813e34b71d16ad65b5f7d4bfe4934f17ffb/bokeh-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/55/3b/14ab63362486a2c9593bff66b813e34b71d16ad65b5f7d4bfe4934f17ffb/bokeh-1.1.0.tar.gz
Summary  : Interactive plots and applications in the browser from Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: bokeh-bin = %{version}-%{release}
Requires: bokeh-license = %{version}-%{release}
Requires: bokeh-python = %{version}-%{release}
Requires: bokeh-python3 = %{version}-%{release}
Requires: Jinja2
Requires: PyYAML
Requires: bkcharts
Requires: numpy
Requires: packaging
Requires: python-dateutil
Requires: six
Requires: tornado
BuildRequires : bkcharts
BuildRequires : buildreq-distutils3
BuildRequires : setuptools-python

%description
Bokeh
=====
*Bokeh is a fiscally sponsored project of [NumFOCUS](http://numfocus.org), a nonprofit dedicated to supporting the open-source scientific computing community. If you like Bokeh and would like to support our mission, please consider [making a donation](https://numfocus.salsalabs.org/donate-to-bokeh/index.html).

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
%setup -q -n bokeh-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557015607
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
