# TODO
# - build with (static) trurlib
# - fix-info-dir.c: In function `usage':
#   fix-info-dir.c:391: warning: string length `1007' is greater than the length `509' ISO C89 compilers are required to support
Summary:	Creates a top-level info `dir' file
Summary(pl.UTF-8):	Tworzy główny plik 'dir' dla systemu Info
Name:		fix-info-dir
Version:	0.13
Release:	10
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.pld.org.pl/software/fix-info-dir/%{name}-%{version}.tar.gz
# Source0-md5:	27e91d3e5c91a2fdad85bf93c9e4cfcf
Patch0:		%{name}-Makefile.patch
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility which creates a top-level `dir' file in the Info system.

%description -l pl.UTF-8
Narzędzie tworzące główny plik 'dir' dla systemu Info

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fomit-frame-pointer -DNDEBUG" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_infodir}}

install %{name} $RPM_BUILD_ROOT%{_sbindir}

touch $RPM_BUILD_ROOT%{_infodir}/{dir,dir.old}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/fix-info-dir %{_infodir}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/%{name}
%ghost %{_infodir}/dir
%ghost %{_infodir}/dir.old
