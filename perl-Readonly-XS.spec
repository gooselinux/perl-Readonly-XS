Name:           perl-Readonly-XS
Version:        1.05
Release:        3%{?dist}
Summary:        Companion module for Readonly

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Readonly-XS/
Source0:        http://search.cpan.org/CPAN/authors/id/R/RO/ROODE/Readonly-XS-%{version}.tar.gz
Patch0:         makefile.pl.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:  perl(Readonly) >= 1.02

# don't provide the private XS.so() lib
%global _use_internal_dependency_generator 0
%global __find_provides %{__perl_provides}

%description
Readonly::XS is a companion module for Readonly, to speed up read-only
scalar variables.


%prep
%setup -q -n Readonly-XS-%{version}
%patch0


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}


%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*


%check
make test


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README Changes
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Readonly/
%{_mandir}/man3/*.3*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.05-3
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.05-1
- update to 1.05
- filter our provides to prevent private lib from showing up
- drop patch1; incorporated upstream as of 1.05

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.04-11
- Rebuild for perl 5.10 (again)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.04-10.2
- Autorebuild for GCC 4.3

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.04-9.2
- patch Carp::croak call for new perl

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.04-9
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.04-8.2
- add BR: perl(Test::More)

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.04-8.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Tue Aug 21 2007 Chris Weyl <cweyl@alumni.drew.edu> 1.04-8
- bump

* Fri Oct 06 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.04-7
- bump for missing patch...

* Fri Oct 06 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.04-6
- drop br on perl(Readonly), patch Makefile.PL as well
- rework spec to use macros

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 1.04-5
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 Chris Weyl <cweyl@alumni.drew.edu> 1.04-4
- bump for mass rebuild

* Thu Dec 08 2005 Michael A. Peters <mpeters@mac.com> - 1.04-3
- proper version on perl(Readonly) BuildRequires & Requires

* Thu Dec 08 2005 Michael A. Peters <mpeters@mac.com> - 1.04-1
- New Version
- BuildRequires perl(Readonly), remove explicit requires on
- perl-Readonly version

* Thu Dec 08 2005 Michael A. Peters <mpeters@mac.com> - 1.03-2
- Fix license and BuildRequires

* Sat Nov 12 2005 Michael A. Peters <mpeters@mac.com> - 1.03-1
- created spec file
