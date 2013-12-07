%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	1
%define major	3
%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname -d %{name}

Summary:	Gnome Devtool Libraries
Name:		gdl
Version:	2.30.1
Release:	7
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gdl/%{url_ver}/%{name}-%{version}.tar.bz2

BuildRequires:	chrpath
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)

%description
This package contains components and libraries that are intended to be
shared between GNOME development tools, including gnome-debug,
gnome-build, and anjuta2.

The current pieces of GDL include:
 - A symbol browser bonobo component (symbol-browser-control).
 - A docking widget (gdl).
 - A utility library that also contains the stubs and skels for
   the symbol browser and text editor components (gdl, idl).

%package -n %{libname}
Summary:	Gnome Devtool Libraries - shared library
Group:		System/Libraries

%description -n %{libname}
This package contains a shared library for %{name}.

%package -n %{devname}
Summary:	Gnome Devtool Libraries - development components
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.


%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %{name}-%{api}
chrpath -d %buildroot%{_libdir}/lib*.so

%files -f %{name}-%{api}.lang
%doc README NEWS MAINTAINERS AUTHORS
%{_datadir}/%{name}

%files -n %{libname}
%{_libdir}/libgdl-%{api}.so.%{major}*

%files -n %{devname}
%doc ChangeLog
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gtk-doc/html/gdl

