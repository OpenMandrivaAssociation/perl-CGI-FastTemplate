%define upstream_name	 CGI-FastTemplate
%define upstream_version 1.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl extension for managing templates, and performing variable interpolation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JM/JMOORE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc README templates
%{perl_vendorlib}/CGI
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.90.0-2mdv2011.0
+ Revision: 680686
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.90.0-1mdv2011.0
+ Revision: 402997
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.09-8mdv2009.0
+ Revision: 255758
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.09-6mdv2008.1
+ Revision: 131271
- kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.09-6mdv2007.0
+ Revision: 73360
- import perl-CGI-FastTemplate-1.09-6mdv2007.0

* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-6mdv2007.0
- Rebuild

* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-5mdk
- spec cleanup
- enable tests
- better URL
- %%{1}mdv2007.1

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.09-4mdk
- fix buildrequires in a backward compatible way

* Thu Jul 22 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.09-3mdk 
- rpmbuildupdate aware

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.09-2mdk
- fixed dir ownership (distlint)

* Sun Dec 07 2003 Guillaume Rousse <guillomovitch@mandrake.org> 1.09-1mdk
- first mdk release

