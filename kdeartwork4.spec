Name: kdeartwork4
Summary: K Desktop Environment
Version: 4.3.1
Release: %mkrel 1
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeartwork-%version.tar.bz2
Buildroot: %_tmppath/%name-%version-%release-root
BuildRequires: X11-devel 
BuildRequires: freetype2-devel
BuildRequires: kdebase4-devel  >= %version
BuildRequires: bzip2-devel 
BuildRequires: libintl 
BuildRequires: jpeg-devel 
BuildRequires: lcms-devel 
BuildRequires: mng-devel
BuildRequires: png-devel 
BuildRequires: libz-devel 
BuildRequires: xscreensaver
BuildRequires: xscreensaver-gl
BuildRequires: xscreensaver-base
BuildRequires: mesaglut-devel
BuildRequires: mesaglu-devel
BuildRequires: kdebase4-workspace-devel >= %version
Suggests: %{name}-emoticons
Suggests: %{name}-kscreensaver
Suggests: %{name}-sounds
Suggests: %{name}-styles
Suggests: %{name}-wallpapers
Suggests: %{name}-color-schemes
Obsoletes: kdeartwork4-core
%if %mdkversion >= 201000
Obsoletes:     kdemoreartwork-plastik < 3.5.3
Obsoletes:     kde-style-phase kde-theme-phase
Obsoletes:     kwin-style-smoothblend
Obsoletes:     kdearwork3 < 3.5.10-1
Obsoletes:     kdearwork3-icons-theme-kdeclassic < 3.5.10-1
Obsoletes:     kdearwork-icons-theme-kdeclassic < 3.5.10-1
Obsoletes:     kdearwork3-icons-theme-Locolor < 3.5.10-1
Obsoletes:     kdearwork-icons-theme-Locolor < 3.5.10-1
Obsoletes:     kdearwork3-icons-theme-ikons < 3.5.10-1
Obsoletes:     kdearwork-icons-theme-ikons < 3.5.10-1
Obsoletes:     kdearwork3-icons-theme-kids < 3.5.10-1
Obsoletes:     kdearwork-icons-theme-kids < 3.5.10-1
Obsoletes:     kdearwork3-icons-theme-slick < 3.5.10-1
Obsoletes:     kdearwork-icons-theme-slick < 3.5.10-1
%endif
%description
Additional artwork (themes, sound themes, icons,etc...) for KDE.

%files
%defattr(-,root,root,-)
%doc README

#-------------------------------------------------------------------------

%package icons-theme-nuvola
Summary:  Default Icons from kde4
Group: Graphical desktop/KDE
Obsoletes: kdeartwork-icons-theme-nuvola <= 3.5.9-6

%description icons-theme-nuvola
nuvola icons theme

%files icons-theme-nuvola
%defattr(-,root,root,-)
%_kde_iconsdir/nuvola

#-------------------------------------------------------------------------

%package emoticons
Summary: %{name} emoticons
Group: Graphical desktop/KDE

%description emoticons
%{name} emoticons.

%files emoticons
%defattr(-,root,root)
%_kde_datadir/emoticons/*

#-------------------------------------------------------------------------

%package sounds
Summary: %{name} sounds
Group: Graphical desktop/KDE

%description sounds
%{name} sounds.

%files sounds
%defattr(-,root,root)
%_kde_datadir/sounds/KDE_Logout_new.wav
%_kde_datadir/sounds/KDE_Startup_new.wav

#-------------------------------------------------------------------------

%package styles
Summary: %{name} styles
Group: Graphical desktop/KDE

%description styles
%{name} styles.

%files styles
%defattr(-,root,root)
%_kde_appsdir/kstyle
%_kde_libdir/kde4/kstyle_phase_config.so
%_kde_libdir/kde4/plugins/styles/phasestyle.so

#-------------------------------------------------------------------------

%package color-schemes
Summary: %{name} color schemes
Group: Graphical desktop/KDE

%description color-schemes
%{name} color schemes.

%files color-schemes
%defattr(-,root,root)
%_kde_appsdir/color-schemes

#-------------------------------------------------------------------------

%package wallpapers
Summary: %{name} wallpapers
Group: Graphical desktop/KDE

%description wallpapers
%{name} wallpapers.

%files wallpapers
%defattr(-,root,root)
%_kde_datadir/wallpapers/*

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-heron
Summary: Plasma heron desktopthemes
Group: Graphical desktop/KDE
Provides: plasma-desktoptheme
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-desktoptheme-heron
Plasma heron desktopthemes.

%files -n plasma-desktoptheme-heron
%defattr(-,root,root)
%_kde_appsdir/desktoptheme/heron

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-aya
Summary: Plasma aya desktopthemes
Group: Graphical desktop/KDE
Provides: plasma-desktoptheme
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-desktoptheme-aya
Plasma aya desktopthemes.

%files -n plasma-desktoptheme-aya
%defattr(-,root,root)
%_kde_appsdir/desktoptheme/Aya

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-slim-glow
Summary: Plasma slim-glow desktopthemes
Group: Graphical desktop/KDE
Provides: plasma-desktoptheme
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-desktoptheme-slim-glow
Plasma slim-glow desktopthemes.

%files -n plasma-desktoptheme-slim-glow
%defattr(-,root,root)
%_kde_appsdir/desktoptheme/slim-glow

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-silicon
Summary: Plasma silicon desktopthemes
Group: Graphical desktop/KDE
Provides: plasma-desktoptheme
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-desktoptheme-silicon
Plasma silicon desktopthemes.

%files -n plasma-desktoptheme-silicon
%defattr(-,root,root)
%_kde_appsdir/desktoptheme/Silicon

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-elegance
Summary: Plasma elegance desktopthemes
Group: Graphical desktop/KDE
Provides: plasma-desktoptheme
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-desktoptheme-elegance
Plasma elegance desktopthemes.

%files -n plasma-desktoptheme-elegance
%defattr(-,root,root)
%_kde_appsdir/desktoptheme/Elegance

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-clean-blend
Summary: Plasma Clean-Blend desktopthemes
Group: Graphical desktop/KDE
Provides: plasma-desktoptheme
Conflicts: extragear-plasma < 4.0.82

%description -n plasma-desktoptheme-clean-blend
Plasma Clean-Blend desktopthemes.

%files -n plasma-desktoptheme-clean-blend
%defattr(-,root,root)
%_kde_appsdir/desktoptheme/Clean-Blend

#-----------------------------------------------------------------------------

%package kscreensaver
Summary: %{name} kscreensaver
Group: Graphical desktop/KDE
%if %mdkversion >= 201000
Obsoletes: kdeartwork-screensavers < 3.5.10-1
Obsoletes: kdeartwork3-screensavers < 3.5.10-1
Obsoletes: kdeartwork-screensavers-gl < 3.5.10-1
Obsoletes: kdeartwork3-screensavers-gl < 3.5.10-1
%endif

%description kscreensaver
%{name} kscreensaver.

%files kscreensaver
%defattr(-,root,root)
%_kde_appsdir/kfiresaver
%_kde_appsdir/kscreensaver
%_kde_bindir/*.kss
%_kde_datadir/kde4/services/ScreenSavers/*
%_kde_bindir/kxsconfig
%_kde_bindir/kxsrun

#-------------------------------------------------------------------------

%prep
%setup -q -n kdeartwork-%version

%build
%cmake_kde4

%make

%install
rm -fr %buildroot

%makeinstall_std -C build

%clean
rm -fr %buildroot

