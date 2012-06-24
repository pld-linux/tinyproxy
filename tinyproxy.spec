Summary:	Small HTTP/SSL proxy deamon
Summary(pl):	Ma�y demon proxy
Name:		tinyproxy
Version:	1.6.0
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	a3c1e5ea2ab9972bec30e1cd035a96aa
URL:		http://tinyproxy.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tinyproxy is a small, efficient HTTP/SSL proxy daemon.Tinyproxy is
very useful in a small network.

%description -l pl
Tinyproxy jest ma�ym, wydajnym demonem proxy. Jest bardzo przydatny w
ma�ych sieciach lokalnych.

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
