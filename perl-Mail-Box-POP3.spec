#
# Conditional build:
%bcond_with	tests		# perform "make test"
#
%define		pdir	Mail
%define		pnam	Box-POP3
Summary:	Mail::Box::POP3 - handle POP3 folders as client
#Summary(pl.UTF-8):
Name:		perl-Mail-Box-POP3
Version:	3.004
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mail/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bb67146e3b3367db3714363f2f0d9698
#URL:		https://metacpan.org/release/Mail-Box-POP3/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Mail::Box::Net) >= 3
BuildRequires:	perl(Mail::Box::Test) >= 3
BuildRequires:	perl(Mail::Transport::Receive) >= 3
BuildRequires:	perl-Mail-Message >= 3
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Maintain a folder which has its messages stored on a remote server.
The communication between the client application and the server is
implemented using the POP3 protocol. This class uses
Mail::Transport::POP3 to hide the transport of information, and
focusses solely on the correct handling of messages within a POP3
folder.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Mail/Box/POP3.pm
%{perl_vendorlib}/Mail/Box/POP3.pod
%{perl_vendorlib}/Mail/Box/POP3s.pm
%{perl_vendorlib}/Mail/Box/POP3s.pod
%{perl_vendorlib}/Mail/Box/POP3
%{perl_vendorlib}/Mail/Transport/POP3.pm
%{perl_vendorlib}/Mail/Transport/POP3.pod
%{_mandir}/man3/*
