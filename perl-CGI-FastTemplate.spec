%define module	CGI-FastTemplate
%define name	perl-%{module}
%define version 1.09
%define release %mkrel 8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl extension for managing templates, and performing variable interpolation
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/J/JM/JMOORE/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
What is a template?
A template is a text file with variables in it. When a template is parsed, the
variables are interpolated to text. (The text can be a few bytes or a few
hundred kilobytes.) Here is a simple template with one variable ('$NAME'):
 Hello $NAME.  How are you?
 
When are templates useful?
Templates are very useful for CGI programming, because adding HTML to your perl
code clutters your code and forces you to do any HTML modifications. By putting
all of your HTML in separate template files, you can let a graphic or interface
designer change the look of your application without having to bug you, or let
them muck around in your perl code.

There are other templating modules on CPAN, what makes FastTemplate different?
CGI::FastTemplate has the following attributes:
- Speed
- Efficiency
- Flexibility

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README templates
%{perl_vendorlib}/CGI
%{_mandir}/*/*



