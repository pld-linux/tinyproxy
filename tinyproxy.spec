#
# TODO:
# - init script
#
Summary:	Small HTTP/SSL proxy deamon
Summary(pl):	Ma³y demon proxy
Name:		tinyproxy
Version:	1.6.1
Release:	2
License:	GPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	e4164b06bbd296dd312df22465a550f6
Patch0:		tinyproxy-config.patch
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
%patch0 -p1

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
