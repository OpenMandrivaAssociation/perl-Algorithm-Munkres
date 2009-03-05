%define module Algorithm-Munkres
%define name perl-%{module}
%define version 0.08
%define release %mkrel 1

Name: %{name}
Version: %{version}
Release: %{release}
Summary: %{module} module for perl
Source0: ftp.perl.org/pub/CPAN/modules/by-module/Algorithm/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Development/Perl
Url: http://search.cpan.org/~tpederse/%{name}-%{version}

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Perl extension for Munkres' solution to 
classical Assignment problem for square and rectangular matrices 
This module extends the solution of Assignment problem for square
matrices to rectangular matrices by padding zeros. Thus a rectangular 
matrix is converted to square matrix by padding necessary zeros.

%prep
%setup -q -n %{module}-%{version}

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

