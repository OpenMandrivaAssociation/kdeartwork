Name: kdeartwork4
Summary: K Desktop Environment
Version: 4.0.84
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
Release: %mkrel 1
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeartwork-%version.tar.bz2
Buildroot:	%_tmppath/%name-%version-%release-root
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
Requires: %{name}-kworldclock
Requires: %{name}-emoticons
Requires: %{name}-kwin-icewm-themes
Requires: %{name}-kscreensaver
Requires: %{name}-sounds
Requires: %{name}-styles
Requires: %{name}-wallpapers
Requires: %{name}-color-schemes

%description
Additional artwork (themes, sound themes, icons,etc...) for KDE.

%files
%defattr(-,root,root,-)

#----------------------------------------------------------------------

%package core
Summary: %{name} core package
Group: Graphical desktop/KDE

%description core
%{name} core package

%files core
%doc README
# We will not provide a duplicated icons copy this time
%exclude %_kde_iconsdir/*

#----------------------------------------------------------------------

%package emoticons
Summary: %{name} emoticons
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version

%description emoticons
%{name} emoticons.

%files emoticons
%defattr(-,root,root)
%_kde_datadir/emoticons/*

#---------------------------------------------

%package kwin-icewm-themes
Summary: %{name} kwin-icewm-themes
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version

%description kwin-icewm-themes
%{name} icewm-themes.

%files kwin-icewm-themes
%defattr(-,root,root)
%_kde_appsdir/kwin/icewm-themes/*

#---------------------------------------------

%package kscreensaver
Summary: %{name} kscreensaver
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version

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

#---------------------------------------------

%package kworldclock
Summary: %{name} kworldclock
Group: Graphical desktop/KDE
Requires: %name-core = %epoch:%version

%description kworldclock
%{name} kworldclock.

%files kworldclock
%defattr(-,root,root)
%_kde_appsdir/kworldclock

#---------------------------------------------

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

#---------------------------------------------

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

#---------------------------------------------

%package color-schemes
Summary: %{name} color schemes
Group: Graphical desktop/KDE

%description color-schemes
%{name} color schemes.

%files color-schemes
%defattr(-,root,root)
%_kde_appsdir/color-schemes

#---------------------------------------------

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

%build
%cmake_kde4

%make

%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install

%clean
rm -fr %buildroot

