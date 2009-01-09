Summary:	Small HTTP/SSL proxy deamon
Summary(pl):	Ma³y demon proxy
Name:		tinyproxy
Version:	1.6.2
Release:	3
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	08abe93ebd3a229a68e471bb5e013c46
Source1:	tinyproxy.init
Patch0:		tinyproxy-config.patch
URL:		http://tinyproxy.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tinyproxy is a small, efficient HTTP/SSL proxy daemon. Tinyproxy is
very useful in a small network.

%description -l pl
Tinyproxy jest ma³ym, wydajnym demonem proxy. Jest bardzo przydatny w
ma³ych sieciach lokalnych.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8,%{_sysconfdir}/tinyproxy,/etc/rc.d/init.d}
install  src/tinyproxy $RPM_BUILD_ROOT%{_bindir}
install  doc/tinyproxy.8 $RPM_BUILD_ROOT%{_mandir}/man8
install  doc/tinyproxy.conf $RPM_BUILD_ROOT%{_sysconfdir}/tinyproxy

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/tinyproxy

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add tinyproxy
if [ -f /var/lock/subsys/tinyproxy ]; then
	/etc/rc.d/init.d/tinyproxy restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/tinyproxy start\" to start tinyproxy daemon."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/tinyproxy ]; then
		/etc/rc.d/init.d/tinyproxy stop 1>&2
	fi
	/sbin/chkconfig --del tinyproxy
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_sysconfdir}/tinyproxy
%attr(754,root,root) /etc/rc.d/init.d/tinyproxy
%{_mandir}/man8/tinyproxy*
