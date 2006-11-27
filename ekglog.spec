Summary:	ekg logs viewer
Summary(pl):	Przegl±darka logów ekg
Name:		ekglog
Version:	20040928
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	http://dom.comernet.pl/ekglog/%{name}-%{version}.tar.bz2
# Source0-md5:	a17016a0009f4a8792de5d60dca6bc20
URL:		http://dom.comernet.pl/ekglog/
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ekglog can be used to view logfiles created by ekg.

%description -l pl
Program ekglog s³u¿y do przegl±dania logów z ekg.

%prep
%setup -q -c

%build
%{__make} -C src \
	CC="%{__cxx}" \
	CFLAGS="%{rpmcflags} -Wall -I. -Icommands"

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
