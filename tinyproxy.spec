Summary:	Small HTTP/SSL proxy deamon
Summary(pl):	Mały demon proxy
Name:		tinyproxy
Version:	1.6.4
Release:	1
License:	GPL v2
Group:		Networking/Daemons/HTTP
Source0:	https://www.banu.com/pub/tinyproxy/1.6/%{name}-%{version}.tar.gz
# Source0-md5:	3157b9159a8d005f4248cf4d4d6c65e2
Source1:	%{name}.init
Patch0:		%{name}-config.patch
URL:		http://tinyproxy.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.228
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tinyproxy is a small, efficient HTTP/SSL proxy daemon. Tinyproxy is
very useful in a small network.

%description -l pl
Tinyproxy jest małym, wydajnym demonem proxy. Jest bardzo przydatny w
małych sieciach lokalnych.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-transparent-proxy

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
%service tinyproxy restart "tinyproxy daemon"

%preun
if [ "$1" = "0" ]; then
	%service tinyproxy stop
	/sbin/chkconfig --del tinyproxy
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/tinyproxy
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tinyproxy
%attr(754,root,root) /etc/rc.d/init.d/tinyproxy
%{_mandir}/man8/tinyproxy.8*
