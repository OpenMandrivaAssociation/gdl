%define api 1
%define major 3
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname -d %{name}

Summary: Gnome Devtool Libraries
Name: gdl
Version: 2.30.1
Release: 4
Source0: http://ftp.gnome.org/pub/GNOME/sources/gdl/%{name}-%{version}.tar.bz2
License: LGPLv2+
Group: System/Libraries
Url: http://www.gnome.org

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

%package -n %{libname}
Group: System/Libraries
Summary: Gnome Devtool Libraries - shared library

%description -n %{libname}
This package contains shared libraries for %{name}.

%package -n %{develname}
Group: Development/C
Summary: Gnome Devtool Libraries - development components
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %mklibname -d gdl 1

%description -n %{develname}
This package contains development libraries and header files for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot} %{name}-1.lang
%makeinstall_std
find %{buildroot} -name *.la | xargs rm
%find_lang %{name}-%{api}
chrpath -d %{buildroot}%{_libdir}/lib*.so

%files -f %{name}-%{api}.lang
%doc README NEWS MAINTAINERS AUTHORS
%{_datadir}/%{name}


%files -n %{libname}
%{_libdir}/libgdl-%{api}.so.%{major}*

%files -n %{develname}
%doc ChangeLog
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gtk-doc/html/gdl

