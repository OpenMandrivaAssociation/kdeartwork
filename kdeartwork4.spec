%define branch 0
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define kde_snapshot svn1198704
%endif

Name: kdeartwork4
Summary: K Desktop Environment
Version: 4.6.4
%if %branch
Release: 0.%kde_snapshot.2
%else
Release: 1
%endif
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
%if %branch
Source: ftp://ftp.kde.org/pub/kde/unstable/%version/src/kdeartwork-%version%kde_snapshot.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeartwork-%version.tar.bz2
%endif
Buildroot: %_tmppath/%name-%version-%release-root
BuildRequires: xscreensaver-base
BuildRequires: mesaglu-devel
BuildRequires: eigen2
BuildRequires: kdebase4-workspace-devel >= 2:4.6.0
BuildRequires: kdegraphics4-devel
BuildRequires: libxt-devel
Suggests: %{name}-emoticons
Suggests: %{name}-kscreensaver
Suggests: %{name}-sounds
Suggests: %{name}-styles
Suggests: %{name}-wallpapers
Suggests: %{name}-color-schemes
Obsoletes: kdeartwork4-core

%description
Additional artwork (themes, sound themes, icons,etc...) for KDE.

%files
%defattr(-,root,root,-)
%doc README

#-------------------------------------------------------------------------

%package icons-theme-nuvola
Summary:  Default Icons from kde4
Group: Graphical desktop/KDE
Buildarch: noarch
Obsoletes: kdeartwork-icons-theme-nuvola <= 3.5.9-6
Obsoletes: %name-icons-theme-nuvola < %epoch:%version-%release

%description icons-theme-nuvola
nuvola icons theme

%files icons-theme-nuvola
%defattr(-,root,root,-)
%_kde_iconsdir/nuvola

#-------------------------------------------------------------------------

%package emoticons
Summary: %{name} emoticons
Group: Graphical desktop/KDE
Buildarch: noarch
Obsoletes: %name-emoticons < %epoch:%version-%release

%description emoticons
%{name} emoticons.

%files emoticons
%defattr(-,root,root)
%_kde_datadir/emoticons/*

#-------------------------------------------------------------------------

%package sounds
Summary: %{name} sounds
Group: Graphical desktop/KDE
Buildarch: noarch
Obsoletes: %name-sounds < %epoch:%version-%release

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
Conflicts: kdebase-workspace < 2:4.5.68

%description styles
%{name} styles.

%files styles
%defattr(-,root,root)
%_kde_appsdir/kstyle
%_kde_libdir/kde4/kstyle_phase_config.so
%_kde_libdir/kde4/plugins/styles/phasestyle.so
%_kde_libdir/kde4/kwin3_kde2.so
%_kde_libdir/kde4/kwin3_keramik.so
%_kde_libdir/kde4/kwin3_modernsys.so
%_kde_libdir/kde4/kwin3_quartz.so
%_kde_libdir/kde4/kwin3_redmond.so
%_kde_libdir/kde4/kwin3_web.so
%_kde_libdir/kde4/kwin_kde2_config.so
%_kde_libdir/kde4/kwin_keramik_config.so
%_kde_libdir/kde4/kwin_modernsys_config.so
%_kde_libdir/kde4/kwin_quartz_config.so
%_kde_appsdir/kwin/kde2.desktop
%_kde_appsdir/kwin/keramik.desktop
%_kde_appsdir/kwin/modernsystem.desktop
%_kde_appsdir/kwin/quartz.desktop
%_kde_appsdir/kwin/redmond.desktop
%_kde_appsdir/kwin/web.desktop

#-------------------------------------------------------------------------

%package color-schemes
Summary: %{name} color schemes
Group: Graphical desktop/KDE
Buildarch: noarch
Obsoletes: %name-color-schemes < %epoch:%version-%release

%description color-schemes
%{name} color schemes.

%files color-schemes
%defattr(-,root,root)
%_kde_appsdir/color-schemes

#-------------------------------------------------------------------------

%package wallpapers
Summary: %{name} wallpapers
Group: Graphical desktop/KDE
Buildarch: noarch
Obsoletes: %name-wallpapers < %epoch:%version-%release

%description wallpapers
%{name} wallpapers.

%files wallpapers
%defattr(-,root,root)
%_kde_datadir/wallpapers/*

#-------------------------------------------------------------------------

%package aurorae-themes-air-oxygen
Summary: %{name} wallpapers
Group: Graphical desktop/KDE
Buildarch: noarch
Obsoletes: %name-aurorae-themes-air-oxygen < %epoch:%version-%release

%description aurorae-themes-air-oxygen
%{name} wallpapers.

%files aurorae-themes-air-oxygen
%defattr(-,root,root)
%_kde_appsdir/aurorae/themes/Air-Oxygen

#-------------------------------------------------------------------------

%package aurorae-themes-oxygen
Summary: %{name} wallpapers
Group: Graphical desktop/KDE
Buildarch: noarch
Obsoletes: %name-aurorae-themes-oxygen < %epoch:%version-%release

%description aurorae-themes-oxygen
%{name} wallpapers.

%files aurorae-themes-oxygen
%defattr(-,root,root)
%_kde_appsdir/aurorae/themes/Oxygen

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-aya
Summary: Plasma aya desktopthemes
Group: Graphical desktop/KDE
Provides: plasma-desktoptheme
Buildarch: noarch
Conflicts: extragear-plasma < 4.0.82
Obsoletes: plasma-desktoptheme-aya < %epoch:%version-%release

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
Buildarch: noarch
Conflicts: extragear-plasma < 4.0.82
Obsoletes: plasma-desktoptheme-slim-glow < %epoch:%version-%release

%description -n plasma-desktoptheme-slim-glow
Plasma slim-glow desktopthemes.

%files -n plasma-desktoptheme-slim-glow
%defattr(-,root,root)
%_kde_appsdir/desktoptheme/slim-glow

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
Obsoletes: %name-kscreensaver < %epoch:%version-%release

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

#-----------------------------------------------------------------------------

%prep
%if %branch
%setup -q -n kdeartwork-%version%kde_snapshot
%else
%setup -q -n kdeartwork-%version
%endif

%build
%cmake_kde4
%make

%install
rm -fr %buildroot

%makeinstall_std -C build

%clean
rm -fr %buildroot

