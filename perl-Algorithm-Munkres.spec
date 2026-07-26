%define upstream_name    Algorithm-Munkres
Name:		perl-%{upstream_name}
Version:	0.08
Release:	6

Summary:	%{upstream_name} module for perl
License:	GPLv2+
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	ftp.perl.org/pub/CPAN/modules/by-module/Algorithm/%{upstream_name}-%{version}.tar.bz2

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Perl extension for Munkres' solution to 
classical Assignment problem for square and rectangular matrices 
This module extends the solution of Assignment problem for square
matrices to rectangular matrices by padding zeros. Thus a rectangular 
matrix is converted to square matrix by padding necessary zeros.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Algorithm
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.80.0-2mdv2011.0
+ Revision: 680447
- mass rebuild

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 409021
- rebuild using %0.08 Thu Mar 05 2009 Stéphane Téletchéa <steletch@mandriva.org> 0.08-1mdv2009.1
+ Revision: 348890
- Initial revision, needed by perl-bioperl


* Thu Mar 5 2009 Stéphane Téletchéa <steletch@mandriva.org> 0.08-1mdv2009.1
- Initial revision, needed by perl-bioperl
