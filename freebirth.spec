%define name	freebirth
%define version	0.3.2
%define release	19
%define	Summary	Bass synth/sequencer/sample player for linux

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch1:		freebirth-0.3.2-debian-fixes.patch
Patch2:		freebirth-0.3.2-mdv-fix-str-fmt.patch
URL:		https://www.bitmechanic.com/projects/freebirth/
License:	GPLv2+ 
Group:		Sound
BuildRequires:	gtk+2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Freebirth is a free software bass synthesizer / step sequencer
 / sample player. The bass synthesizer is vaguely 303ish but
also has other capabilities such as 

 - Three oscillators (saw, sin, sqr)
 - Phase offsets for each oscillator
 - Separate filter and amplitude envelopes
 - Separate tuning for each oscillator
 - Two effects busses (reverb and delay).

%prep
%setup -q
%patch1 -p0
%patch2 -p1 -b .strfmt

%build
%setup_compile_flags
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/freebirth/raw/
install -m755 %{name} -D %{buildroot}%{_bindir}/%{name}
install -m755 wav_to_raw -D %{buildroot}%{_bindir}/wav_to_raw
install -m644 raw/*.raw %{buildroot}%{_datadir}/freebirth/raw/

#menu item

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{Summary}
Exec=%{name} 
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;
EOF


install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES INSTALL NEXT_VERSION README
%{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/raw
%{_datadir}/%{name}/raw/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/*




%changelog
* Thu Jan 06 2011 Funda Wang <fwang@mandriva.org> 0.3.2-18mdv2011.0
+ Revision: 629098
- update with gentoo's patch to fix segment fault

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Mon Dec 07 2009 Jérôme Brenier <incubusss@mandriva.org> 0.3.2-17mdv2010.1
+ Revision: 474506
- fix str fmt
- fix license tag

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.3.2-15mdv2009.0
+ Revision: 245357
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.3.2-13mdv2008.1
+ Revision: 136419
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Feb 28 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.3.2-13mdv2007.0
+ Revision: 127168
- fix category in menu
- Import freebirth

* Thu Aug 10 2006 Lenny Cartier <lenny@mandriva.com> 0.3.2-12mdv2007.0
- xdg

* Thu Jul 07 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.3.2-11mdk
- update from Sat Jan 22 2005 that got lost
- Fixed segmentation fault on file load in Sample Pitch (P1 from debian)
- compile with -O3
- a little nicer description (from debian)
- change summary macro to avoid possible conflicts if we were to build debug package
- don't bzip2 icons

* Thu May 27 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.3.2-10mdk
- rebuild

