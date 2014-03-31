# TODO: Review -ac.patch if it's still neded.
Summary:	Small HTTP/SSL proxy daemon
Summary(pl.UTF-8):	Mały demon proxy
Name:		tinyproxy
Version:	1.8.3
Release:	1
License:	GPL v2
Group:		Networking/Daemons/HTTP
# Source0:	http://dl.sourceforge.net/tinyproxy/%{name}-%{version}.tar.gz
Source0:	https://files.banu.com/tinyproxy/1.8/%{name}-%{version}.tar.bz2
# Source0-md5:	292ac51da8ad6ae883d4ebf56908400d
Source1:	%{name}.init
## Patch1:		%{name}-ac.patch
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

%description -l pl.UTF-8
Tinyproxy jest małym, wydajnym demonem proxy HTTP/SSL. Jest bardzo
przydatny w małych sieciach lokalnych.

%prep
%setup -q
# %patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure  \
	--enable-transparent

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man5,%{_mandir}/man8,%{_sysconfdir}/tinyproxy,/etc/rc.d/init.d,%{_datadir}/%{name}}
cp -p src/tinyproxy $RPM_BUILD_ROOT%{_bindir}
cp -p data/templates/*.html $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -p docs/man8/tinyproxy.8 $RPM_BUILD_ROOT%{_mandir}/man8
cp -p docs/man5/tinyproxy.conf.5  $RPM_BUILD_ROOT%{_mandir}/man5
cp -p etc/tinyproxy.conf $RPM_BUILD_ROOT%{_sysconfdir}/tinyproxy
cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/tinyproxy

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
%{_datadir}/%{name}
%dir %{_sysconfdir}/tinyproxy
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tinyproxy/tinyproxy.conf
%attr(754,root,root) /etc/rc.d/init.d/tinyproxy
%{_mandir}/man8/tinyproxy.*
%{_mandir}/man5/tinyproxy.conf.*
