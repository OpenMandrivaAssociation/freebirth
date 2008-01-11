%define name	freebirth
%define version	0.3.2
%define release	%mkrel 13
%define	Summary	Bass synth/sequencer/sample player for linux

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		%{name}-optflags.patch
Patch1:		freebirth-0.3.2-debian-fixes.patch
URL:		http://www.bitmechanic.com/projects/freebirth/
License:	GPL 
Group:		Sound
BuildRequires:	libgtk+-devel libglib-devel X11-devel
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
%patch0 -p0
%patch1 -p1

%build
# quick patch for samples in /usr/share/freebirth
perl -pi -e "s|FB_SAMPLES \".\"|FB_SAMPLES \"/usr/share/freebirth\"||g;" \
  raw_wave.h

# actual make
#make all
%make OPTFLAGS="$RPM_OPT_FLAGS -O3"

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

%post
%update_menus

%postun
%clean_menus

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


