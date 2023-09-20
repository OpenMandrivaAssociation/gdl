%define api	3
%define major	5
%define libname	%mklibname %{name} %{api} %{major}
%define devname	%mklibname -d %{name} %{api}
%define girname	%mklibname %{name}-gir %{api}

Summary:	Gnome Development/Docking library
Name:		gdl
Version:	3.40.0
Release:	5
License:	LGPLv2+
Group:		System/Libraries
Url:		https://www.gnome.org
Source0:	https://ftp.gnome.org/pub/GNOME/sources/gdl/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
%rename		gdl3

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
Group:		System/Libraries
Summary:	Gnome Development/Docking library - shared libraries
Suggests:	%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{girname}
Group:		System/Libraries
Summary:	GObject Introspection interface library for %{name}

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{devname}
Group:		Development/C
Summary:	Gnome Development/Docking library headers and development libraries
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This packages contains the headers and libraries for %{name}.

%prep
%setup -qn %{name}-%{version}

%build
%configure

%make_build

%install
%make_install
%find_lang %{name}-%{api}

%files -f %{name}-%{api}.lang

%files -n %{libname}
%{_libdir}/libgdl-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Gdl-%{api}.typelib

%files -n %{devname}
%doc ChangeLog README NEWS MAINTAINERS AUTHORS
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gtk-doc/html/gdl-*
%{_datadir}/gir-1.0/Gdl-%{api}.gir

