Summary:	Small HTTP/SSL proxy deamon
Summary(pl):	Ma³y demon proxy
Name:		tinyproxy
Version:	1.5.0
Release:	2
License:	GPL
Group:		Networking/Daemons
Source0:	http://belnet.dl.sourceforge.net/sourceforge/tinyproxy/%{name}-%{version}.tar.gz
# Source0-md5:	2236b57f183b168dcfaaffbda43b4051
URL:		http://tinyproxy.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tinyproxy is a small, efficient HTTP/SSL proxy daemon.Tinyproxy is
very useful in a small network.

%description -l pl
Tinyproxy jest ma³ym, wydajnym demonem proxy. Jest bardzo przydatny w
ma³ych sieciach lokalnych.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8,%{_sysconfdir}/tinyproxy}
install  src/tinyproxy $RPM_BUILD_ROOT%{_bindir}
install  doc/tinyproxy.8 $RPM_BUILD_ROOT%{_mandir}/man8
install  doc/tinyproxy.conf $RPM_BUILD_ROOT%{_sysconfdir}/tinyproxy

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_sysconfdir}/tinyproxy
%{_mandir}/man8/tinyproxy*
