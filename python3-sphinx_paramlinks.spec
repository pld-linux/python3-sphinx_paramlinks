Summary:	Allows param links in Sphinx function/method descriptions to be linkable
Summary(pl.UTF-8):	Klikalne odnośniki w sphinksowych opisach funkcji/method
Name:		python3-sphinx_paramlinks
Version:	0.6.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-paramlinks/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-paramlinks/sphinx-paramlinks-%{version}.tar.gz
# Source0-md5:	74a1cc657c1ef7015f137bcdf3d30a16
URL:		https://pypi.org/project/sphinx-paramlinks/
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx extension which allows ":param:" directives within Python
documentation to be linkable.

%description -l pl.UTF-8
Rozszerzenie Sphinksa, pozwalające, aby dyrektywy ":param:" w
pythonowej dokumentacji były odnośnikami.

%prep
%setup -q -n sphinx-paramlinks-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/sphinx_paramlinks
%{py3_sitescriptdir}/sphinx_paramlinks-%{version}-py*.egg-info
