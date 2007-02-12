Summary:	Small HTTP/SSL proxy daemon
Summary(pl.UTF-8):   Mały demon proxy
Name:		tinyproxy
Version:	1.7.0
Release:	1
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/tinyproxy/%{name}-%{version}.tar.gz
# Source0-md5:	ccacdd9cb093202886b6c7c9e453a804
Source1:	%{name}.init
Patch0:		%{name}-config.patch
URL:		http://tinyproxy.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tinyproxy is a small, efficient HTTP/SSL proxy daemon. Tinyproxy is
very useful in a small network.

%description -l pl.UTF-8
Tinyproxy jest małym, wydajnym demonem proxy HTTP/SSL. Jest bardzo
przydatny w małych sieciach lokalnych.

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
%{_sysconfdir}/tinyproxy
%attr(754,root,root) /etc/rc.d/init.d/tinyproxy
%{_mandir}/man8/tinyproxy*
