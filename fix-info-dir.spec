%define no_install_post_compress_docs 1

Summary:	Creates a top-level info `dir' file
Summary(pl):	Tworzy g³ówny plik 'dir' dla systemu Info
Name:		fix-info-dir
Version:	0.13
Release:	3
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.pld.org.pl/software/fix-info-dir/%{name}-%{version}.tar.gz
BuildRequires:	zlib-devel
Prereq:		zlib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility which creates a top-level `dir' file in the Info system.

%description -l pl
Narzêdzie tworz±ce g³ówny plik 'dir' dla systemu Info

%prep 
%setup -q 

%build
%{__make} CFLAGS="%{rpmcflags} \
	-fomit-frame-pointer -DNDEBUG"
 
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_infodir}}

install %{name} $RPM_BUILD_ROOT/%{_sbindir}

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
