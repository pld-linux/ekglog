Summary:	ekg logs viewer
Summary(pl):	Przegl±darka logów ekg
Name:		ekglog
Version:	20031103
Release:	0.1
License:	GPL
Group:		Applications/Console
Source0:	http://dom.comernet.pl/ekglog/%{name}-%{version}.tar.bz2
# Source0-md5:	918cd7010c4a39c82410363122467782
Patch0:		%{name}-includes_fix.patch
Patch1:		%{name}-ncurses_fix.patch
Patch2:		%{name}-inline.patch
URL:		http://dom.comernet.pl/ekglog/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ekglog can be used to view logfiles created by ekg.

%description -l pl
Program ekglog s³u¿y do przegl±dania logów z ekg.

%prep
%setup -q -c
%patch0 -p0
%patch1 -p0
%patch2 -p1

%build
%{__make} -C src \
	CC="%{__cxx}" \
	CFLAGS="%{rpmcflags} -Wall -I. -Icommands -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/ekglog $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Docs/{AUTHORS,ChangeLog,README,TODO}
%attr(755,root,root) %{_bindir}/*
