Summary:	ekg logs viewer
Summary(pl):	przegl±darka logów ekg.
Name:		ekglog
Version:	20031019
Release:	0.1
License:	GPL
Group:		Applications/Console
Source0:	http://dom.comernet.pl/ekglog/%{name}-%{version}.tar.bz2
# Source0-md5:	90efecd0890e4a878faecd733709b598
Patch0:		%{name}-includes_fix.patch
Patch1:		%{name}-ncurses_fix.patch
URL:		http://dom.comernet.pl/ekglog/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ekglog can be used to view logfiles created by ekg.

%description -l pl
Program ekglog s³u¿y do przegl±dania logów z ekg.

%prep
%setup -q -c
%patch0 -p0
# This patch is ugly, I just wanted to go step further with the compilation...
%patch1 -p0

%build
cd src/
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/ekglog $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Docs/*
%attr(755,root,root) %{_bindir}/*
