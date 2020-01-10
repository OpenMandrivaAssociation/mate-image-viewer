Summary:	The Eye of MATE image viewer
Name:		mate-image-viewer
Version:	1.4.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{lua: print (string.match(rpm.expand("%{version}"),"%d+.%d+"))}/%{name}-%{version}.tar.xz

BuildRequires:	docbook-dtd412-xml
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(exempi-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(mate-doc-utils)
BuildRequires:	pkgconfig(mate-icon-theme)
BuildRequires:	pkgconfig(lcms)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(x11)

Requires:	librsvg
Requires:	mate-icon-theme

Provides:	eom = %{version}-%{release}

%description
This is the Eye of MATE, an image viewer program. It is meant
to be a fast and functional image viewer as well as an image
cataloging program. It does proper handling of large images and
images with full opacity information, and can zoom and scroll
images quickly while keeping  memory usage constant.

%package devel
Group:		Development/C
Summary:	C headers needed to build EOG plugins

%description devel
This is the Eye of MATE, an image viewer program. It is meant
to be a fast and functional image viewer as well as an image
cataloging program. It does proper handling of large images and
images with full opacity information, and can zoom and scroll
images quickly while keeping  memory usage constant.

Install this if you want to build EOG plugins.

%prep
%setup -q
%autopatch -p1

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--enable-introspection=yes \
	--disable-schemas-compile \
	--disable-scrollkeeper

%make LIBS='-lgmodule-2.0 -lz'

%install
%makeinstall_std

%find_lang eom --with-gnome --all-name

find %{buildroot} -name *.la -delete

%files -f eom.lang
%doc AUTHORS NEWS README
%{_sysconfdir}/mateconf/schemas/eom.schemas
%{_bindir}/*
%dir %{_libdir}/eom
%dir %{_libdir}/eom/plugins
%{_libdir}/eom/plugins/fullscreen.eom-plugin
%{_libdir}/eom/plugins/reload.eom-plugin
%{_libdir}/eom/plugins/statusbar-date.eom-plugin
%{_libdir}/eom/plugins/*.so*
%{_datadir}/applications/*
%{_datadir}/eom
%{_iconsdir}/hicolor/*/*/*

%files devel
%{_includedir}/eom-2.20
%{_libdir}/pkgconfig/eom.pc



%changelog
* Thu Jun 07 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 803206
- imported package mate-image-viewer

