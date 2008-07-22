%define name    vertex
%define version 0.1.15
%define release %mkrel 5

%define title       Vertex
%define longtitle   3D model assembler

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    3D model assembler
License:    GPL
Group:      Graphics
Source0:    ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
Patch:      %{name}-0.1.15.build.patch.bz2
Source1:    %{name}-16.png.bz2
Source2:    %{name}-32.png.bz2
Source3:    %{name}-48.png.bz2
Url:        http://wolfpack.twu.net/Vertex
BuildRequires:  Mesa-common-devel
BuildRequires:  gtk+1.2-devel
BuildRequires:  gtkglarea-devel
BuildRequires:  imlib-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Vertex 3D Model Assembler (often reffered to as just Vertex) is a unique
modeller designed specifically for generating high-performance and
efficient 3D models which can contain additional third party proprietery
data suitable for applications using OpenGL style of graphics rendering.

Vertex features support for multiple models and editing of proprietery
data found within these models. It has many tools for mass editing and
gives instant rendering feedback.

%prep
%setup -q
%patch
# mv LICENSE at usual location
mv -f vertex/data/LICENSE .
bzcat %{SOURCE1} > %{name}-16.png
bzcat %{SOURCE2} > %{name}-32.png
bzcat %{SOURCE3} > %{name}-48.png

%build
./configure Linux -v --disable=arch-i686 --libdir=-L%{_libdir}
make CFLAGS="%{optflags} -D__USE_BSD -DHAVE_IMLIB `gtk-config --cflags`"

%install
rm -rf %{buildroot}
make PREFIX=%{buildroot}%_prefix MAN_DIR=%{buildroot}%{_mandir}/man1 install

# icons
install -D -m 644 %{name}-16.png %{buildroot}%{_miconsdir}/%{name}.png 
install -D -m 644 %{name}-32.png %{buildroot}%{_iconsdir}/%{name}.png 
install -D -m 644 %{name}-48.png %{buildroot}%{_liconsdir}/%{name}.png

# menu entry
mkdir -p %{buildroot}%{_libdir}/menu

install -d -m 755 %{buildroot}%{_datadir}/applications
cat >  %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{title}
Comment=%{longtitle}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=3DGraphics
EOF

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files 
%defattr(-,root,root)
%doc AUTHORS INSTALL LICENSE README
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.xpm

