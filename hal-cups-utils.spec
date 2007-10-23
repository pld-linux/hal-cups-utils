Summary:	Halified CUPS utilities 
Summary(pl.UTF-8):	HAL-owe narzędzia dla CUPS-a
Name:		hal-cups-utils
Version:	0.6.13
Release:	0.r83.1
License:	CUPS (GPL v2 with OpenSSL linking exception)
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	435e0a2127677e7a6b06f1890e13af78
Patch0:		%{name}-python.patch
BuildRequires:	cups-devel
# dbus just to satisfy configure
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	glib2-devel >= 1:2.4
BuildRequires:	hal-devel >= 0.5.7
BuildRequires:	sed >= 4.0
Requires:	cups
Requires:	hal >= 0.5.7
Requires:	system-config-printer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Halified utilities for CUPS:
 - hal_lpadmin
 - hal CUPS backend

%description -l pl.UTF-8
HAL-owe narzędzia dla CUPS-a:
 - hal_lpadmin
 - backend hal dla CUPS-a

%prep
%setup -q -n trunk
%patch0 -p1

sed -i -e 's,/usr/libexec/,%{_libexecdir}/,' systemv/10-hal_lpadmin.fdi

%build
%configure \
	--enable-printconf 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS COPYING ChangeLog README
%{_libexecdir}/hal_lpadmin
%{_prefix}/lib/cups/backend/hal
%{_datadir}/hal/fdi/policy/10osvendor/10-hal_lpadmin.fdi
