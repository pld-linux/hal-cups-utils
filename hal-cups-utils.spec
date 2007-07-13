Summary:	Halified CUPS utilities 
Name:		hal-cups-utils
Version:	0.6.9
Release:	1
License:	GPL
Group:		Applications/System
Source:		%{name}-%{version}.tar.gz
Patch0:		%{name}-configure.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cups-devel
BuildRequires:	dbus-devel >= 0.92
BuildRequires:	hal-devel >= 0.5.7
Requires:	cups
Requires:	hal
Requires:	system-config-printer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Halified utilities for CUPS:
	- hal_lpadmin
	- hal CUPS backend

%prep
%setup -q
%patch0 -p1

%build
%configure --enable-printconf 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libexecdir}/hal_lpadmin
%{_libdir}/cups/backend/hal
%{_datadir}/hal/fdi/policy/10osvendor/10-hal_lpadmin.fdi
