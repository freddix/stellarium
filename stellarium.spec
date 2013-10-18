Summary:	Realistic sky generator
Name:		stellarium
Version:	0.12.4
Release:	1
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://downloads.sourceforge.net/stellarium/%{name}-%{version}.tar.gz
# Source0-md5:	4d2ec96b9b4d9c8fc722f864409cf4fa
URL:		http://www.stellarium.org/
BuildRequires:	OpenGL-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	QtScript-devel
BuildRequires:	QtSql-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtTest-devel
BuildRequires:	QtXml-devel
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	qt-build
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Stellarium renders 3D realistic skies in real time with OpenGL. It
displays stars, constellations, planets, nebulas and others things
like ground, landscape, fog, etc.

%prep
%setup -q

%{__sed} -i 's|-Wall|-Wall %{rpmcxxflags}|g' CMakeLists.txt

%build
mkdir build
cd build
%cmake .. \
	-DENABLE_SOUND=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

cat > $RPM_BUILD_ROOT%{_desktopdir}/stellarium.desktop <<EOF
[Desktop Entry]
Type=Application
Exec=stellarium
Icon=stellarium
Terminal=false
Name=Stellarium
Comment=Planetarium for your computer
StartupNotify=true
Categories=GTK;Astronomy;Education;Science;
EOF

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{cv,gn,ht,haw,hrx,lb,nan,sah,sco,su}
%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/hicolor/512x512

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/stellarium.desktop
%{_iconsdir}/hicolor/*/apps/stellarium.png
%{_mandir}/man1/%{name}.1*

