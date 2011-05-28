%define upstream_name    Algorithm-Munkres
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    %{upstream_name} module for perl
License:    GPLv2+
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp.perl.org/pub/CPAN/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Perl extension for Munkres' solution to 
classical Assignment problem for square and rectangular matrices 
This module extends the solution of Assignment problem for square
matrices to rectangular matrices by padding zeros. Thus a rectangular 
matrix is converted to square matrix by padding necessary zeros.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Algorithm
%{_mandir}/*/*
