#
# Conditional build:
%bcond_with	tests	# perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	ReturnValue
Summary:	Class::ReturnValue - a return-value object that may be treated as a boolean, array or object
Summary(pl):	Class::ReturnValue - obiekt warto¶ci zwracanej, któru mo¿e byæ traktowany jak warto¶æ logiczna, tablica lub obiekt
Name:		perl-Class-ReturnValue
Version:	0.52
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d4836df29f817d839e2c87147d5efc9e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::ReturnValue is a "clever" return value object that can allow code
calling your routine to expect: a boolean value (did it fail) or a list
(what are the return values).

%description -l pl
Class::ReturnValue jest ,,m±drym'' obiektem, który pozwala, aby kod
wywo³uj±cy Twoje funkcje oczekiwa³: warto¶ci boolowskiej (czy siê uda³o)
lub listy (jakie warto¶ci zwrócono).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
#%{__perl} -pi -e 'BEGIN{undef $/};s/\{\s*package MY;.*$//s' Makefile.PL

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
# Warning: test script in this package IS broken (wrong name)
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
