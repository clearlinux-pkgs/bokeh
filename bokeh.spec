#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bokeh
Version  : 2.1.0
Release  : 52
URL      : https://files.pythonhosted.org/packages/5f/9e/7df853096e2d82de05f3612d48484c6afee1620b6665d174b405f6cc5f38/bokeh-2.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5f/9e/7df853096e2d82de05f3612d48484c6afee1620b6665d174b405f6cc5f38/bokeh-2.1.0.tar.gz
Summary  : Interactive plots and applications in the browser from Python
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause ISC MIT WTFPL
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
%setup -q -n bokeh-2.1.0
cd %{_builddir}/bokeh-2.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592235847
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bokeh
cp %{_builddir}/bokeh-2.1.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/19f653e42c734907a4384cd22d54edadf6f0c14e
cp %{_builddir}/bokeh-2.1.0/bokeh/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/19f653e42c734907a4384cd22d54edadf6f0c14e
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/@types/jquery/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/fc3defdb0ec07babc6fa8696113812c5a4ccd74a
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/@types/katex/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/fc3defdb0ec07babc6fa8696113812c5a4ccd74a
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/@types/sizzle/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/fc3defdb0ec07babc6fa8696113812c5a4ccd74a
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/@types/slickgrid/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/fc3defdb0ec07babc6fa8696113812c5a4ccd74a
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/commander/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/63513188251d15fcdc716703fbee89be4a3a20e6
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/d/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/47a77621ca1e034281d734b932626160e3f2282d
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/deepmerge/license.txt %{buildroot}/usr/share/package-licenses/bokeh/ac744a970e9d7e5037f856fd4c35545d495d66fc
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/es5-ext/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/a0455df512fc34622c02badf48e1a43d31953a15
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/es6-iterator/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/79394f8970296d1df1faab7874d1df6413e84e94
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/es6-map/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/c551c40c6610ad8398847785578a7d2ed694a6db
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/es6-promise/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/018939bf52537ea641014ab9a140718634c9420f
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/es6-set/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/c551c40c6610ad8398847785578a7d2ed694a6db
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/es6-set/node_modules/es6-symbol/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/e1dbb4fa0cc8faebb415ee77ffcf08c28b811439
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/es6-symbol/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/47a77621ca1e034281d734b932626160e3f2282d
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/event-emitter/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/20ebd36b0ae2ac536d0727eb241c561e2f114d34
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/ext/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/a0455df512fc34622c02badf48e1a43d31953a15
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/ext/node_modules/type/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/5460543b29176b37aefd07904ba3fd68a0925f13
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/hammerjs/LICENSE.md %{buildroot}/usr/share/package-licenses/bokeh/9a2bf26ac8e1d93fe76698b3232da6bbfdb643b6
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/15df6665dfd90f5cd8fdfde4c0c43051fbb76dae
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/globalize/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/47257650961f07b3ba3884d2da35a6eda2728068
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-1.11.0/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/e321abbfe02338fd699b66e0da13bdab4ee47594
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-1.11.1/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/e321abbfe02338fd699b66e0da13bdab4ee47594
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-1.11.2/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/e321abbfe02338fd699b66e0da13bdab4ee47594
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-1.11.3/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/e321abbfe02338fd699b66e0da13bdab4ee47594
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-1.12.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/1238983d71130d0d96aad2acc946818007c77734
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-1.12.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/1238983d71130d0d96aad2acc946818007c77734
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-1.12.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/1238983d71130d0d96aad2acc946818007c77734
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-1.12.3/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/1238983d71130d0d96aad2acc946818007c77734
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-1.12.4/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/1238983d71130d0d96aad2acc946818007c77734
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-1.7.0/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/7e1d6c027dccc9bfcab9f36d3e1ec645c34a77e9
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-1.7.1/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/7e1d6c027dccc9bfcab9f36d3e1ec645c34a77e9
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-1.7.2/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/7e1d6c027dccc9bfcab9f36d3e1ec645c34a77e9
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-1.8.0/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/4d66f2e049344c2200f05c402708d7a36df1af75
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-1.8.1/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/4d66f2e049344c2200f05c402708d7a36df1af75
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-1.8.2/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/4d66f2e049344c2200f05c402708d7a36df1af75
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-1.8.3/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/4d66f2e049344c2200f05c402708d7a36df1af75
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-1.9.0/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/4d66f2e049344c2200f05c402708d7a36df1af75
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-1.9.1/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/4d66f2e049344c2200f05c402708d7a36df1af75
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-2.1.0/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/e321abbfe02338fd699b66e0da13bdab4ee47594
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-2.1.1/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/e321abbfe02338fd699b66e0da13bdab4ee47594
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-2.1.2/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/e321abbfe02338fd699b66e0da13bdab4ee47594
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-2.1.3/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/e321abbfe02338fd699b66e0da13bdab4ee47594
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-2.1.4/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/e321abbfe02338fd699b66e0da13bdab4ee47594
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-2.2.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/1238983d71130d0d96aad2acc946818007c77734
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-2.2.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/1238983d71130d0d96aad2acc946818007c77734
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-2.2.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/1238983d71130d0d96aad2acc946818007c77734
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-2.2.3/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/1238983d71130d0d96aad2acc946818007c77734
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-2.2.4/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/1238983d71130d0d96aad2acc946818007c77734
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-3.0.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/1238983d71130d0d96aad2acc946818007c77734
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-3.1.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/1238983d71130d0d96aad2acc946818007c77734
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-custom/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/e321abbfe02338fd699b66e0da13bdab4ee47594
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-mousewheel/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/b00865128de96ede266b066d82ff9d484f9460d6
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery-simulate/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/620bab08a3e5f3c38afe5a3bf6f188c87b9e7851
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/1238983d71130d0d96aad2acc946818007c77734
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jquery/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/e321abbfe02338fd699b66e0da13bdab4ee47594
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/jshint/LICENSE/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/d8f7f981396c9350e54f91d3f743a6098a4f3683
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/qunit-assert-classes/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/8fc977208f9e2d0f2f47dbb7972108708bfc03fc
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/qunit-composite/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/2fa29dcd07ee62c697de517a8c48f412104ce685
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery-ui/external/qunit/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/1ce4b5d7914f571c9b944c9acbfa32a5673ce237
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/jquery/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/fcf3a2474ae0d8e6ce39e4bc915915e4b4bd32b8
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/js-tokens/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/f1c13e8c00a23a075cb581b6d6262fd755b08eed
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/loose-envify/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/75b1377c10a3452794d8a83ed6629441f97079bd
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/next-tick/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/051b5b0f028b8eea145e06289267e00fcf282749
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/nouislider/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/ceffa174420c734f28329d45a2782584cb693192
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/redux/LICENSE.md %{buildroot}/usr/share/package-licenses/bokeh/8377bf32b37fd605c430e4fe198f840fd8fd36b7
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/symbol-observable/license %{buildroot}/usr/share/package-licenses/bokeh/c41ef4b8497e270b6b472e254410ec5e751f1574
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/tslib/LICENSE.txt %{buildroot}/usr/share/package-licenses/bokeh/557ce4c1f2d1480bef1fe3db9c14615e3b213a99
cp %{_builddir}/bokeh-2.1.0/tests/unit/bokeh/embed/latex_label/node_modules/type/LICENSE %{buildroot}/usr/share/package-licenses/bokeh/5460543b29176b37aefd07904ba3fd68a0925f13
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
/usr/share/package-licenses/bokeh/018939bf52537ea641014ab9a140718634c9420f
/usr/share/package-licenses/bokeh/051b5b0f028b8eea145e06289267e00fcf282749
/usr/share/package-licenses/bokeh/1238983d71130d0d96aad2acc946818007c77734
/usr/share/package-licenses/bokeh/15df6665dfd90f5cd8fdfde4c0c43051fbb76dae
/usr/share/package-licenses/bokeh/19f653e42c734907a4384cd22d54edadf6f0c14e
/usr/share/package-licenses/bokeh/1ce4b5d7914f571c9b944c9acbfa32a5673ce237
/usr/share/package-licenses/bokeh/20ebd36b0ae2ac536d0727eb241c561e2f114d34
/usr/share/package-licenses/bokeh/2fa29dcd07ee62c697de517a8c48f412104ce685
/usr/share/package-licenses/bokeh/47257650961f07b3ba3884d2da35a6eda2728068
/usr/share/package-licenses/bokeh/47a77621ca1e034281d734b932626160e3f2282d
/usr/share/package-licenses/bokeh/4d66f2e049344c2200f05c402708d7a36df1af75
/usr/share/package-licenses/bokeh/5460543b29176b37aefd07904ba3fd68a0925f13
/usr/share/package-licenses/bokeh/557ce4c1f2d1480bef1fe3db9c14615e3b213a99
/usr/share/package-licenses/bokeh/620bab08a3e5f3c38afe5a3bf6f188c87b9e7851
/usr/share/package-licenses/bokeh/63513188251d15fcdc716703fbee89be4a3a20e6
/usr/share/package-licenses/bokeh/75b1377c10a3452794d8a83ed6629441f97079bd
/usr/share/package-licenses/bokeh/79394f8970296d1df1faab7874d1df6413e84e94
/usr/share/package-licenses/bokeh/7e1d6c027dccc9bfcab9f36d3e1ec645c34a77e9
/usr/share/package-licenses/bokeh/8377bf32b37fd605c430e4fe198f840fd8fd36b7
/usr/share/package-licenses/bokeh/8fc977208f9e2d0f2f47dbb7972108708bfc03fc
/usr/share/package-licenses/bokeh/9a2bf26ac8e1d93fe76698b3232da6bbfdb643b6
/usr/share/package-licenses/bokeh/a0455df512fc34622c02badf48e1a43d31953a15
/usr/share/package-licenses/bokeh/ac744a970e9d7e5037f856fd4c35545d495d66fc
/usr/share/package-licenses/bokeh/b00865128de96ede266b066d82ff9d484f9460d6
/usr/share/package-licenses/bokeh/c41ef4b8497e270b6b472e254410ec5e751f1574
/usr/share/package-licenses/bokeh/c551c40c6610ad8398847785578a7d2ed694a6db
/usr/share/package-licenses/bokeh/ceffa174420c734f28329d45a2782584cb693192
/usr/share/package-licenses/bokeh/d8f7f981396c9350e54f91d3f743a6098a4f3683
/usr/share/package-licenses/bokeh/e1dbb4fa0cc8faebb415ee77ffcf08c28b811439
/usr/share/package-licenses/bokeh/e321abbfe02338fd699b66e0da13bdab4ee47594
/usr/share/package-licenses/bokeh/f1c13e8c00a23a075cb581b6d6262fd755b08eed
/usr/share/package-licenses/bokeh/fc3defdb0ec07babc6fa8696113812c5a4ccd74a
/usr/share/package-licenses/bokeh/fcf3a2474ae0d8e6ce39e4bc915915e4b4bd32b8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
