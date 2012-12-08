%define name gdl
%define version 2.30.1
%define release %mkrel 3
%define api 1
%define major 3
%define libname %mklibname %name %api %major
%define libnamedev %mklibname -d %name

Summary: Gnome Devtool Libraries
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/gdl/%{name}-%{version}.tar.bz2
License: LGPLv2+
Group: System/Libraries
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgnomeui2-devel
BuildRequires: libglade2.0-devel
BuildRequires: intltool
BuildRequires: chrpath
BuildRequires: gtk-doc

%description
This package contains components and libraries that are intended to be
shared between GNOME development tools, including gnome-debug,
gnome-build, and anjuta2.

The current pieces of GDL include:

 - A symbol browser bonobo component (symbol-browser-control).

 - A docking widget (gdl).

 - A utility library that also contains the stubs and skels for
   the symbol browser and text editor components (gdl, idl).

%package -n %libname
Group: System/Libraries
Summary: Gnome Devtool Libraries - shared library
Requires: %name >= %version

%description -n %libname
This package contains components and libraries that are intended to be
shared between GNOME development tools, including gnome-debug,
gnome-build, and anjuta2.

The current pieces of GDL include:

 - A symbol browser bonobo component (symbol-browser-control).

 - A docking widget (gdl).

 - A utility library that also contains the stubs and skels for
   the symbol browser and text editor components (gdl, idl).

%package -n %libnamedev
Group: Development/C
Summary: Gnome Devtool Libraries - development components
Requires: %libname = %version
Provides: lib%name-devel = %version-%release
Obsoletes: %mklibname -d gdl 1

%description -n %libnamedev
This package contains components and libraries that are intended to be
shared between GNOME development tools, including gnome-debug,
gnome-build, and anjuta2.

The current pieces of GDL include:

 - A symbol browser bonobo component (symbol-browser-control).

 - A docking widget (gdl).

 - A utility library that also contains the stubs and skels for
   the symbol browser and text editor components (gdl, idl).


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot} %name-1.lang
%makeinstall_std
%find_lang %name-%{api}
chrpath -d %buildroot%_libdir/lib*.so

%clean
rm -rf %{buildroot}

%files -f %name-%{api}.lang
%defattr(-,root,root)
%doc README NEWS MAINTAINERS AUTHORS
%_datadir/%name


%files -n %libname
%defattr(-,root,root)
%_libdir/libgdl-%{api}.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%doc ChangeLog
%_libdir/lib*.so
%_libdir/pkgconfig/*
%_includedir/*
%_datadir/gtk-doc/html/gdl



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.30.1-2mdv2011.0
+ Revision: 664816
- mass rebuild

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 2.30.1-1mdv2011.0
+ Revision: 581880
- update to new version 2.30.1

* Mon Aug 23 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-2mdv2011.0
+ Revision: 572413
- revert to 2.30.0

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 2.31.3-1mdv2011.0
+ Revision: 563500
- update build deps
- new version
- add introspection support

* Mon Mar 29 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528771
- update to new version 2.30.0

* Tue Mar 09 2010 Götz Waschk <waschk@mandriva.org> 2.29.92-1mdv2010.1
+ Revision: 516897
- update to new version 2.29.92

* Wed Dec 09 2009 Götz Waschk <waschk@mandriva.org> 2.29.2-1mdv2010.1
+ Revision: 475374
- update to new version 2.29.2

* Tue Nov 24 2009 Götz Waschk <waschk@mandriva.org> 2.28.2-1mdv2010.1
+ Revision: 469772
- update to new version 2.28.2

* Thu Oct 22 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.1-1mdv2010.0
+ Revision: 458786
- Release 2.28.1

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446959
- new version
- new major

* Thu Sep 10 2009 Götz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 437461
- update to new version 2.27.92

* Sun Jun 14 2009 Götz Waschk <waschk@mandriva.org> 2.27.3-1mdv2010.0
+ Revision: 385938
- new version
- drop patch

* Wed May 27 2009 Götz Waschk <waschk@mandriva.org> 2.27.2-2mdv2010.0
+ Revision: 380137
- readd a removed header

* Wed May 27 2009 Götz Waschk <waschk@mandriva.org> 2.27.2-1mdv2010.0
+ Revision: 380106
- new version
- new major

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 2.27.1-1mdv2010.0
+ Revision: 374188
- new version
- drop patch

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 356171
- update to new version 2.26.0

* Mon Mar 02 2009 Götz Waschk <waschk@mandriva.org> 2.25.92-1mdv2009.1
+ Revision: 347462
- update to new version 2.25.92

* Tue Feb 17 2009 Götz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 341347
- new version
- fix format strings

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 2.24.0-2mdv2009.1
+ Revision: 301479
- rebuilt against new libxcb

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286819
- new version
- fix license
- update file list

* Wed Aug 20 2008 Götz Waschk <waschk@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 274126
- new version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.7.11-2mdv2009.0
+ Revision: 221045
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Mar 09 2008 Götz Waschk <waschk@mandriva.org> 0.7.11-1mdv2008.1
+ Revision: 183049
- new version

* Mon Feb 25 2008 Götz Waschk <waschk@mandriva.org> 0.7.10-1mdv2008.1
+ Revision: 174976
- new version

* Mon Feb 11 2008 Götz Waschk <waschk@mandriva.org> 0.7.9-1mdv2008.1
+ Revision: 165505
- remove rpath
- new version
- update file list

* Mon Jan 28 2008 Götz Waschk <waschk@mandriva.org> 0.7.8-1mdv2008.1
+ Revision: 159195
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 0.7.7-1mdv2008.0
+ Revision: 63174
- new version
- new devel name

* Fri Jun 22 2007 Götz Waschk <waschk@mandriva.org> 0.7.6-1mdv2008.0
+ Revision: 42953
- new version

* Sun May 06 2007 Götz Waschk <waschk@mandriva.org> 0.7.5-1mdv2008.0
+ Revision: 23723
- new version

* Sun May 06 2007 Götz Waschk <waschk@mandriva.org> 0.7.4-1mdv2008.0
+ Revision: 23689
- new version


* Thu Mar 29 2007 Götz Waschk <waschk@mandriva.org> 0.7.3-1mdv2007.1
+ Revision: 149353
- new version
- move ChangeLog to devel package

* Mon Feb 12 2007 Götz Waschk <waschk@mandriva.org> 0.7.2-1mdv2007.1
+ Revision: 118849
- new version

* Thu Jan 18 2007 Götz Waschk <waschk@mandriva.org> 0.7.1-1mdv2007.1
+ Revision: 110392
- new version

* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 0.7.0-1mdv2007.1
+ Revision: 108731
- new version
- update file list

* Mon Dec 18 2006 Christiaan Welvaart <spturtle@mandriva.org> 0.6.1-3mdv2007.1
+ Revision: 98431
- rebuild to fix .la file in ppc -devel package
- Import gdl

* Tue Aug 01 2006 Götz Waschk <waschk@mandriva.org> 0.6.1-1mdv2007.0
- Rebuild

* Tue May 16 2006 Götz Waschk <waschk@mandriva.org> 0.6.1-1mdk
- New release 0.6.1
- use mkrel

* Tue Jun 28 2005 G�tz Waschk <waschk@mandriva.org> 0.6.0-1mdk
- update file list
- new version

* Wed May 18 2005 G�tz Waschk <waschk@mandriva.org> 0.5.0-1mdk
- initial package

