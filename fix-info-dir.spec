Summary:	Creates a top-level info `dir' file
Name:		fix-info-dir
Version:	0.1
Release:	1
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	zlib-devel

%description
Utility which creates a top-level `dir' file in the Info system

%prep 
%setup -q 

%build
make CFLAGS='-O2 -fomit-frame-pointer -DNDEBUG'
 
%install
install -d 755 $RPM_BUILD_ROOT/%{_sbindir}
install -s -m 755 %{name} $RPM_BUILD_ROOT/%{_sbindir}
install -d 755 $RPM_BUILD_ROOT/%{_infodir}
touch $RPM_BUILD_ROOT/%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/%{name}
%ghost %{_infodir}/dir
