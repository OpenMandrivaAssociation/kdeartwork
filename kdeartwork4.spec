Name: kdeartwork4
Summary: K Desktop Environment
Version: 4.2.0
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
Release: %mkrel 2
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeartwork-%version.tar.bz2
Patch0: slideshow-crossfade_and_effects.patch
Patch1: kdeartwork-4.1.70-fix-build.patch
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

%description
Additional artwork (themes, sound themes, icons,etc...) for KDE.

%files
%defattr(-,root,root,-)

#----------------------------------------------------------------------

%package core
Summary: %{name} core package
Group: Graphical desktop/KDE
Obsoletes: kdearwork <= 3.5.9-6

%description core
%{name} core package

%files core
%doc README

#-------------------------------------------------------------------------

%package icons-theme-kdeclassic
Summary:  Default Icons from kde4
Group: Graphical desktop/KDE
Obsoletes: kdeartwork-icons-theme-kdeclassic <= 3.5.9-6

%description icons-theme-kdeclassic
Kdeclassic icons theme

%files icons-theme-kdeclassic
%defattr(-,root,root,-)
%_kde_iconsdir/kdeclassic

#-------------------------------------------------------------------------

%package emoticons
Summary: %{name} emoticons
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version

%description emoticons
%{name} emoticons.

%files emoticons
%defattr(-,root,root)
%_kde_datadir/emoticons/*

#-------------------------------------------------------------------------

%package sounds
Summary: %{name} sounds
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version

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
Requires: %name-core = %epoch:%version

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
Requires: %name-core = %epoch:%version

%description wallpapers
%{name} wallpapers.

%files wallpapers
%defattr(-,root,root)
%_kde_datadir/wallpapers/*

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-heron
Summary: Plasma heron desktopthemes
Group: Graphical desktop/KDE
Requires: kdebase4-workspace
Provides: plasma-desktoptheme
Requires: plasma-desktoptheme-default
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
Requires: kdebase4-workspace
Provides: plasma-desktoptheme
Requires: plasma-desktoptheme-default
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
Requires: kdebase4-workspace
Provides: plasma-desktoptheme
Requires: plasma-desktoptheme-default
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
Requires: kdebase4-workspace
Provides: plasma-desktoptheme
Requires: plasma-desktoptheme-default
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
Requires: kdebase4-workspace
Provides: plasma-desktoptheme
Requires: plasma-desktoptheme-default
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
Requires: kdebase4-workspace
Provides: plasma-desktoptheme
Requires: plasma-desktoptheme-default
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
Requires: %name-core = %epoch:%version
Obsoletes: kdeartwork-screensavers <= 3.5.9-6

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
%patch0 -p1 -b .effects
%patch1 -p1

%build
%cmake_kde4

%make

%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install

%clean
rm -fr %buildroot

