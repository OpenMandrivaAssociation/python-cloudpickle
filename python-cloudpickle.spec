%define module cloudpickle

Name:		python-cloudpickle
Version:	3.1.2
Release:	2
Summary:	Extended pickling support for Python objects
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/cloudpickle/
Source0:	https://files.pythonhosted.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:		python-cloudpickle-flit4.patch

BuildSystem:	python
BuildArch:	noarch
BuildRequires:  python%{pyver}dist(flit-core)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
Extended pickling support for Python objects.

%{module} makes it possible to serialize Python constructs not
supported by the default pickle module from the Python standard library.

%{module} is especially useful for cluster computing where Python code
is shipped over the network to execute on remote hosts, possibly close
to the data.

%files
%doc README.md
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
