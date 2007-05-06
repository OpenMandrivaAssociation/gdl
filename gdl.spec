%define name gdl
%define version 0.7.5
%define release %mkrel 1
%define libname %mklibname %name 1

Summary: Gnome Devtool Libraries
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/gdl/%{name}-%{version}.tar.bz2
License: GPL
Group: System/Libraries
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgnomeui2-devel
BuildRequires: libglade2.0-devel
BuildRequires: perl-XML-Parser


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

%package -n %libname-devel
Group: Development/C
Summary: Gnome Devtool Libraries - development components
Requires: %libname = %version
Provides: lib%name-devel = %version-%release

%description -n %libname-devel
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
rm -rf $RPM_BUILD_ROOT %name-1.lang
%makeinstall_std
%find_lang %name-1

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -f %name-1.lang
%defattr(-,root,root)
%doc README NEWS MAINTAINERS AUTHORS
%_datadir/%name


%files -n %libname
%defattr(-,root,root)
%_libdir/libgdl-1.so.0*
%_libdir/libgdl-gnome-1.so.0*

%files -n %libname-devel
%defattr(-,root,root)
%doc ChangeLog
%_libdir/lib*.so
%_libdir/lib*.la
%_libdir/pkgconfig/*
%_includedir/*


