%define name    vertex
%define version 0.1.16
%define release 4

%define debug_package %{nil}

%define title       Vertex
%define longtitle   3D model assembler

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    3D model assembler
License:    GPL
Group:      Graphics
Source0:    ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
Patch:      %{name}-0.1.16-lib64.patch
Source1:    %{name}-16.png.bz2
Source2:    %{name}-32.png.bz2
Source3:    %{name}-48.png.bz2
Url:        https://wolfpack.twu.net/Vertex
BuildRequires:  mesa-common-devel
BuildRequires:  gtk+1.2-devel
BuildRequires:  gtkglarea-devel
BuildRequires:  imlib-devel

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
%patch -p 1
# mv LICENSE at usual location
mv -f vertex/data/LICENSE .
bzcat %{SOURCE1} > %{name}-16.png
bzcat %{SOURCE2} > %{name}-32.png
bzcat %{SOURCE3} > %{name}-48.png

%build
%ifarch x86_64
./configure Linux64 -v --disable=arch-i686
%else
./configure Linux -v --disable=arch-i686
%endif
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



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.1.16-2mdv2010.0
+ Revision: 434668
- rebuild

* Mon Aug 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.16-1mdv2009.0
+ Revision: 270669
- fix lib64 build
- new version

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - import vertex

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Tue Jul 11 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.15-3mdv2007.0
- xdg menu

* Fri May 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.15-2mdk
- fix build
- fix optimisations

* Mon Apr 25 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.15-1mdk
- New release 0.1.15
- drop patch0 (merged upstream)
- spec cleanup

* Thu Jul 22 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.1.14-4mdk 
- explicit libdir

* Sat Jun 05 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.1.14-3mdk
- rebuild

* Mon Jan 12 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.1.14-2mdk
- added missing imlib-devel buildrequires (thx slbd)
- fixed buildrequires
- fix compilation

* Fri May 02 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.1.14-1mdk
- 0.1.14

* Thu Sep 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.1.10-3mdk
- rebuild

* Fri May 31 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.1.10-2mdk
- rebuild against new libstdc++

* Wed Feb 27 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.1.10-1mdk
- 0.1.10
- fixed changelog
- bzipped and converted icons to png

* Mon Dec 03 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.1.9-1mdk
- 0.1.9

* Tue Oct 30 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.1.8-1mdk
- 0.1.8
- fixed changelog

* Mon Oct 15 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.1.6-3mdk
- rebuild against new libpng

* Wed Oct 03 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.1.6-2mdk
- fixed by Guillaume Rousse <g.rousse@linux-mandrake.com> :
    - icons in right place

* Sat Sep 15 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.1.6-1mdk
- 0.1.6
- dropped gtk config patch

* Wed Aug 15 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.1.4-2mdk
- spec cleanup
- included forgotten man page

* Sat Aug 11 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.1.4-1mdk
- 0.1.4
- dropped demo files
- s/Copyright/License/
- adds Buildrequires libgtk+1.2-devel libgtkglarea-devel

* Fri Jun 15 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.1.2-1mdk
- 0.1.2
- added demo files

* Wed May 23 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.0.1d-1mdk
- first Mandrake release
