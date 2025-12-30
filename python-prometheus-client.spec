Name:		python-prometheus-client
Version:	0.21.1
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/p/prometheus-client/prometheus_client-%{version}.tar.gz
Summary:	Python client for the Prometheus monitoring system.
URL:		https://pypi.org/project/prometheus-client/
License:	Apache Software License 2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Python client for the Prometheus monitoring system.

%prep
%autosetup -p1 -n prometheus_client-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/prometheus_client
%{py_sitedir}/prometheus_client-*.*-info
