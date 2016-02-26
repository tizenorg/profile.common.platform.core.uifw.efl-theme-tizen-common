%define DEVEL_PREFIX /opt/var/efl-theme-tizen-common-devel
Summary: EFL themes for Tizen Common
Name: efl-theme-tizen-common
Version: 1.0
Release: 0
Group: Common/Themes
License: BSD 2-Clause
Source: %{name}-%{version}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: edje
BuildRequires: edje-bin
BuildRequires: embryo
BuildRequires: embryo-bin

%description -n efl-theme-tizen-common
EFL themes for Tizen Common

%package -n efl-theme-tizen-common-devel
Summary: Development package

%description -n efl-theme-tizen-common-devel
Development package for Tizen Common theme

%prep
%setup -q

%build
autoreconf -ivf
%configure
export CFLAGS+=" --fPIC"
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed -Wl,--rpath=/usr/lib"
make

%install
rm -rf %{buildroot}
%make_install

#for efl-theme-tizen-common
%files
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/efl-theme-tizen-common.edj
%{_datadir}/elementary/themes/default-common.edj
%manifest %{name}.manifest
#license
#elementary config for common

%files -n efl-theme-tizen-common-devel
%defattr(-,root,root,-)
#TODO  - later
#%{DEVEL_PREFIX}/*
