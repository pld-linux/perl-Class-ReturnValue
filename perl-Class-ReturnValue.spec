#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	ReturnValue
Summary:	%{pdir}::%{pnam} perl module
Summary(cs):	Modul %{pdir}::%{pnam} pro Perl
Summary(da):	Perlmodul %{pdir}::%{pnam}
Summary(de):	%{pdir}::%{pnam} Perl Modul
Summary(es):	Módulo de Perl %{pdir}::%{pnam}
Summary(fr):	Module Perl %{pdir}::%{pnam}
Summary(it):	Modulo di Perl %{pdir}::%{pnam}
Summary(ja):	%{pdir}::%{pnam} Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	%{pdir}::%{pnam} ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul %{pdir}::%{pnam}
Summary(pl):	Modu³ perla %{pdir}::%{pnam}
Summary(pt_BR):	Módulo Perl %{pdir}::%{pnam}
Summary(pt):	Módulo de Perl %{pdir}::%{pnam}
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl %{pdir}::%{pnam}
Summary(sv):	%{pdir}::%{pnam} Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl %{pdir}::%{pnam}
Summary(zh_CN):	%{pdir}::%{pnam} Perl Ä£¿é
Name:		perl-Class-ReturnValue
Version:	0.51
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
%{__perl} -pi -e 'BEGIN{undef $/};s/\{\s*package MY;.*$//s' Makefile.PL

%build
%{__perl} Makefile.PL
%{__make}
# Warning: test script in this package IS broken (wrong name)
%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
