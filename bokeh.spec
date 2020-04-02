#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bokeh
Version  : 2.0.1
Release  : 50
URL      : https://files.pythonhosted.org/packages/45/83/20bd995c4d79f8947fb2c9b80fa729157300d252a63c412d0f5a4915ff07/bokeh-2.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/45/83/20bd995c4d79f8947fb2c9b80fa729157300d252a63c412d0f5a4915ff07/bokeh-2.0.1.tar.gz
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
Requires: numpy
Requires: packaging
Requires: python-dateutil
Requires: tornado
Requires: typing_extensions
BuildRequires : Jinja2
BuildRequires : Pillow
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : numpy
BuildRequires : packaging
BuildRequires : python-dateutil
BuildRequires : setuptools-python
BuildRequires : tornado

%description
<a href="https://bokeh.org">
<img src="https://static.bokeh.org/logos/logotype.svg" height="60" alt="Bokeh logotype" />
</a>

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
Provides: pypi(bokeh)
Requires: pypi(jinja2)
Requires: pypi(numpy)
Requires: pypi(packaging)
Requires: pypi(pillow)
Requires: pypi(python_dateutil)
Requires: pypi(pyyaml)
Requires: pypi(tornado)
Requires: pypi(typing_extensions)

%description python3
python3 components for the bokeh package.


%prep
%setup -q -n bokeh-2.0.1
cd %{_builddir}/bokeh-2.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585852503
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
cp %{_builddir}/bokeh-2.0.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/19f653e42c734907a4384cd22d54edadf6f0c14e
cp %{_builddir}/bokeh-2.0.1/bokeh/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/19f653e42c734907a4384cd22d54edadf6f0c14e
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
/usr/share/package-licenses/bokeh/19f653e42c734907a4384cd22d54edadf6f0c14e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
