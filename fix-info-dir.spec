Summary:	Creates a top-level info `dir' file
Summary(pl):	Tworzy g��wny plik 'dir' dla systemu Info.
Name:		fix-info-dir
Version:	0.12
Release:	2
License:	GPL
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Source0:	ftp://ftp.pld.org.pl/software/fix-info-dir/%{name}-%{version}.tar.gz
BuildRequires:	zlib-devel
Prereq:		zlib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility which creates a top-level `dir' file in the Info system.

%description -l pl
Narz�dzie tworz�ce g��wny plik 'dir' dla systemu Info

%prep 
%setup -q 

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS -fomit-frame-pointer -DNDEBUG"
 
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_infodir}}

install -s %{name} $RPM_BUILD_ROOT/%{_sbindir}
touch $RPM_BUILD_ROOT/%{_infodir}/{dir,dir.old}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/fix-info-dir %{_infodir}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/%{name}
%ghost %{_infodir}/dir 
%ghost %{_infodir}/dir.old
