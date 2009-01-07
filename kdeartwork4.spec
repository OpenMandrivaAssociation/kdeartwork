Name: kdeartwork4
Summary: K Desktop Environment
Version: 4.1.96
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
Release: %mkrel 1
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
Suggests: %{name}-kworldclock
Suggests: %{name}-emoticons
Suggests: %{name}-kwin-icewm-themes
Suggests: %{name}-kscreensaver
Suggests: %{name}-sounds
Suggests: %{name}-styles
Suggests: %{name}-wallpapers
Suggests: %{name}-color-schemes
Suggests: %{name}-icons-theme-Locolor
Suggests: %{name}-icons-theme-crystalsvg
Suggests: %{name}-icons-theme-ikons
Suggests: %{name}-icons-theme-slick
Suggests: %{name}-icons-theme-nuvola
Suggests: %{name}-icons-theme-kids
Suggests: %{name}-icons-theme-kdeclassic

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

%package icons-theme-Locolor
Summary:  Default Icons from kde4
Group: Graphical desktop/KDE
Obsoletes: kdeartwork-icons-theme-Locolor <= 3.5.9-6

%description icons-theme-Locolor
Locolor icons theme

%files icons-theme-Locolor
%defattr(-,root,root,-)
%_kde_iconsdir/Locolor

#-------------------------------------------------------------------------

%package icons-theme-crystalsvg
Summary:  Default Icons from kde4
Group: Graphical desktop/KDE
Obsoletes: kdeartwork-icons-theme-crystalsvg <= 3.5.9-6

%description icons-theme-crystalsvg
Crystalsvg icons theme

%files icons-theme-crystalsvg
%defattr(-,root,root,-)
%_kde_iconsdir/crystalsvg

#-------------------------------------------------------------------------

%package icons-theme-ikons
Summary:  Default Icons from kde4
Group: Graphical desktop/KDE
Obsoletes: kdeartwork-icons-theme-ikons <= 3.5.9-6

%description icons-theme-ikons
Ikons icons theme

%files icons-theme-ikons
%defattr(-,root,root,-)
%_kde_iconsdir/ikons

#-------------------------------------------------------------------------

%package icons-theme-slick
Summary:  Default Icons from kde4
Group: Graphical desktop/KDE
Obsoletes: kdeartwork-icons-theme-slick <= 3.5.9-6

%description icons-theme-slick
Slick icons theme

%files icons-theme-slick
%defattr(-,root,root,-)
%_kde_iconsdir/slick

#-------------------------------------------------------------------------

%package icons-theme-nuvola
Summary:  Default Icons from kde4
Group: Graphical desktop/KDE
Obsoletes: kdeartwork-icons-theme-nuvola <= 3.5.9-6

%description icons-theme-nuvola
Nuvola icons theme

%files icons-theme-nuvola
%defattr(-,root,root,-)
%_kde_iconsdir/nuvola

#-------------------------------------------------------------------------

%package icons-theme-kids
Summary:  Default Icons from kde4
Group: Graphical desktop/KDE
Obsoletes: kdeartwork-icons-theme-kids <= 3.5.9-6

%description icons-theme-kids
kids icons theme

%files icons-theme-kids
%defattr(-,root,root,-)
%_kde_iconsdir/kids

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

%package kwin-icewm-themes
Summary: %{name} kwin-icewm-themes
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version

%description kwin-icewm-themes
%{name} icewm-themes.

%files kwin-icewm-themes
%defattr(-,root,root)
%_kde_appsdir/kwin/icewm-themes/*

#-------------------------------------------------------------------------

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

%package kworldclock
Summary: %{name} kworldclock
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version

%description kworldclock
%{name} kworldclock.

%files kworldclock
%defattr(-,root,root)
%_kde_appsdir/kworldclock

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

#----------------------------------------------------------------------

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

