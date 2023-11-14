#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Allows param links in Sphinx function/method descriptions to be linkable
Summary(pl.UTF-8):	Klikalne odnośniki w sphinksowych opisach funkcji/method
Name:		python-sphinx_paramlinks
# keep 0.4.x here for python2/Sphinx 1.x support
Version:	0.4.3
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-paramlinks/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-paramlinks/sphinx-paramlinks-%{version}.tar.gz
# Source0-md5:	c56241aaf1b1a0e2b5ffeb1ea0eabb20
URL:		https://pypi.org/project/sphinx-paramlinks/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx extension which allows ":param:" directives within Python
documentation to be linkable.

%description -l pl.UTF-8
Rozszerzenie Sphinksa, pozwalające, aby dyrektywy ":param:" w
pythonowej dokumentacji były odnośnikami.

%package -n python3-sphinx_paramlinks
Summary:	Allows param links in Sphinx function/method descriptions to be linkable
Summary(pl.UTF-8):	Klikalne odnośniki w sphinksowych opisach funkcji/method
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-sphinx_paramlinks
Sphinx extension which allows ":param:" directives within Python
documentation to be linkable.

%description -n python3-sphinx_paramlinks -l pl.UTF-8
Rozszerzenie Sphinksa, pozwalające, aby dyrektywy ":param:" w
pythonowej dokumentacji były odnośnikami.

%prep
%setup -q -n sphinx-paramlinks-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/sphinx_paramlinks
%{py_sitescriptdir}/sphinx_paramlinks-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sphinx_paramlinks
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/sphinx_paramlinks
%{py3_sitescriptdir}/sphinx_paramlinks-%{version}-py*.egg-info
%endif
