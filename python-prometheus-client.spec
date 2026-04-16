%define module prometheus-client
%define oname prometheus_client

Name:		python-prometheus-client
Version:	0.25.0
Release:	1
Summary:	Python client for the Prometheus monitoring system.
License:	Apache-2.0 AND BSD-2-Clause
Group:		Development/Python
URL:		https://pypi.org/project/prometheus-client
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Suggests:	python%{pyver}dist(aiohttp)
Suggests:	python%{pyver}dist(django)
Suggests:	python%{pyver}dist(twisted)

%description
Python client for the Prometheus monitoring system.

%files
%{py_sitedir}/%{oname}
%{py_sitedir}/%{oname}-%{version}.dist-info
