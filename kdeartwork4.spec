Name:		kdeartwork4
Summary:	K Desktop Environment
Version:	4.9.0
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPL
URL:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/unstable/%{version}/src/kdeartwork-%{version}.tar.xz
Patch0:		kdeartwork-4.8.2-l10n-ru.patch
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	xscreensaver-base
BuildRequires:	pkgconfig(eigen2)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libkexiv2)
BuildRequires:	pkgconfig(xt)
Suggests:	%{name}-emoticons
Suggests:	%{name}-kscreensaver
Suggests:	%{name}-sounds
Suggests:	%{name}-styles
Suggests:	%{name}-wallpapers
Suggests:	%{name}-color-schemes

%description
Additional artwork (themes, sound themes, icons,etc...) for KDE.

%files
%doc README

#-------------------------------------------------------------------------

%package icons-theme-nuvola
Summary:	Default Icons from kde4
Group:		Graphical desktop/KDE
Buildarch:	noarch
Obsoletes:	%{name}-icons-theme-nuvola < %{EVRD}

%description icons-theme-nuvola
nuvola icons theme

%files icons-theme-nuvola
%{_kde_iconsdir}/nuvola

#-------------------------------------------------------------------------

%package icons-theme-mono
Summary:	Mono Icons from kde4
Group:		Graphical desktop/KDE
Buildarch:	noarch

%description icons-theme-mono
Mono icons theme

%files icons-theme-mono
%{_kde_iconsdir}/mono

#-------------------------------------------------------------------------

%package emoticons
Summary:	%{name} emoticons
Group:		Graphical desktop/KDE
Buildarch:	noarch
Obsoletes:	%{name}-emoticons < %{EVRD}

%description emoticons
%{name} emoticons.

%files emoticons
%{_kde_datadir}/emoticons/*

#-------------------------------------------------------------------------

%package sounds
Summary:	%{name} sounds
Group:		Graphical desktop/KDE
Buildarch:	noarch

%description sounds
%{name} sounds.

%files sounds
%{_kde_datadir}/sounds/KDE_Logout_new.wav
%{_kde_datadir}/sounds/KDE_Startup_new.wav

#-------------------------------------------------------------------------

%package styles
Summary:	%{name} styles
Group:		Graphical desktop/KDE
Conflicts:	kdebase4-workspace < 2:4.5.68

%description styles
%{name} styles.

%files styles
%{_kde_appsdir}/kstyle
%{_kde_libdir}/kde4/kstyle_phase_config.so
%{_kde_libdir}/kde4/plugins/styles/phasestyle.so
%{_kde_libdir}/kde4/kwin3_kde2.so
%{_kde_libdir}/kde4/kwin3_keramik.so
%{_kde_libdir}/kde4/kwin3_modernsys.so
%{_kde_libdir}/kde4/kwin3_quartz.so
%{_kde_libdir}/kde4/kwin3_redmond.so
%{_kde_libdir}/kde4/kwin3_web.so
%{_kde_libdir}/kde4/kwin_kde2_config.so
%{_kde_libdir}/kde4/kwin_keramik_config.so
%{_kde_libdir}/kde4/kwin_modernsys_config.so
%{_kde_libdir}/kde4/kwin_quartz_config.so
%{_kde_appsdir}/kwin/kde2.desktop
%{_kde_appsdir}/kwin/keramik.desktop
%{_kde_appsdir}/kwin/modernsystem.desktop
%{_kde_appsdir}/kwin/quartz.desktop
%{_kde_appsdir}/kwin/redmond.desktop
%{_kde_appsdir}/kwin/web.desktop

#-------------------------------------------------------------------------

%package color-schemes
Summary:	%{name} color schemes
Group:		Graphical desktop/KDE
Buildarch:	noarch

%description color-schemes
%{name} color schemes.

%files color-schemes
%{_kde_appsdir}/color-schemes

#-------------------------------------------------------------------------

%package wallpapers
Summary:	%{name} wallpapers
Group:		Graphical desktop/KDE
Buildarch:	noarch

%description wallpapers
%{name} wallpapers.

%files wallpapers
%{_kde_datadir}/wallpapers/*

#-------------------------------------------------------------------------

%package aurorae-themes-air-oxygen
Summary:	%{name} wallpapers
Group:		Graphical desktop/KDE
Buildarch:	noarch

%description aurorae-themes-air-oxygen
%{name} wallpapers.

%files aurorae-themes-air-oxygen
%{_kde_appsdir}/aurorae/themes/Air-Oxygen

#-------------------------------------------------------------------------

%package aurorae-themes-oxygen
Summary:	%{name} wallpapers
Group:		Graphical desktop/KDE
Buildarch:	noarch

%description aurorae-themes-oxygen
%{name} wallpapers.

%files aurorae-themes-oxygen
%{_kde_appsdir}/aurorae/themes/Oxygen

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-aya
Summary:	Plasma aya desktopthemes
Group:		Graphical desktop/KDE
Provides:	plasma-desktoptheme
Buildarch:	noarch

%description -n plasma-desktoptheme-aya
Plasma aya desktopthemes.

%files -n plasma-desktoptheme-aya
%{_kde_appsdir}/desktoptheme/Aya

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-androbit
Summary:	Plasma androbit desktopthemes
Group:		Graphical desktop/KDE
Provides:	plasma-desktoptheme
Buildarch:	noarch

%description -n plasma-desktoptheme-androbit
Plasma androbit desktopthemes.

%files -n plasma-desktoptheme-androbit
%{_kde_appsdir}/desktoptheme/Androbit

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-produkt
Summary:	Plasma produkt desktopthemes
Group:		Graphical desktop/KDE
Provides:	plasma-desktoptheme
Buildarch:	noarch

%description -n plasma-desktoptheme-produkt
Plasma produkt desktopthemes.

%files -n plasma-desktoptheme-produkt
%{_kde_appsdir}/desktoptheme/Produkt

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-tibanna
Summary:	Plasma tibanna desktopthemes
Group:		Graphical desktop/KDE
Provides:	plasma-desktoptheme
Buildarch:	noarch

%description -n plasma-desktoptheme-tibanna
Plasma tibanna desktopthemes.

%files -n plasma-desktoptheme-tibanna
%{_kde_appsdir}/desktoptheme/Tibanna

#-----------------------------------------------------------------------------

%package -n plasma-desktoptheme-slim-glow
Summary:	Plasma slim-glow desktopthemes
Group:		Graphical desktop/KDE
Provides:	plasma-desktoptheme
Buildarch:	noarch

%description -n plasma-desktoptheme-slim-glow
Plasma slim-glow desktopthemes.

%files -n plasma-desktoptheme-slim-glow
%{_kde_appsdir}/desktoptheme/slim-glow

#-----------------------------------------------------------------------------

%package kscreensaver
Summary:	%{name} kscreensaver
Group:		Graphical desktop/KDE

%description kscreensaver
%{name} kscreensaver.

%files kscreensaver
%{_kde_appsdir}/kfiresaver
%{_kde_appsdir}/kscreensaver
%{_kde_bindir}/*.kss
%{_kde_services}/ScreenSavers/*
%{_kde_bindir}/kxsconfig
%{_kde_bindir}/kxsrun

#-----------------------------------------------------------------------------

%prep
%setup -q -n kdeartwork-%{version}
%patch0 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

