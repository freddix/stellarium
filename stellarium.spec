Summary:	Realistic sky generator
Name:		stellarium
Version:	0.11.4
Release:	2
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://downloads.sourceforge.net/stellarium/%{name}-%{version}.tar.gz
# Source0-md5:	f5b409745f393d80003d57fd276142f4
URL:		http://www.stellarium.org/
BuildRequires:	ImageMagick-coders
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Stellarium renders 3D realistic skies in real time with OpenGL. It
displays stars, constellations, planets, nebulas and others things
like ground, landscape, fog, etc.

%prep
%setup -q

sed -i 's|-Wall|-Wall %{rpmcxxflags}|g' CMakeLists.txt

%build
mkdir build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

convert -geometry 48x48 data/icon.bmp $RPM_BUILD_ROOT%{_pixmapsdir}/stellarium.png

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

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{cv,ht,haw,hrx,lb,sah,sco,su}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/stellarium.desktop
%{_pixmapsdir}/stellarium.png
%{_mandir}/man1/%{name}.1*

