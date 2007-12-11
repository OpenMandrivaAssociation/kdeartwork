%define revision 746274

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %unstable
%define dont_strip 1
%endif

Name: kdeartwork4
Summary: K Desktop Environment
Version: 3.97.1
Release: %mkrel 0.%revision.1
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
%if %branch
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeartwork-%version.%revision.tar.bz2
%else
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeartwork-%version.tar.bz2
%endif
Buildroot:	%_tmppath/%name-%version-%release-root
BuildRequires: kde4-macros
BuildRequires: X11-devel 
BuildRequires: freetype2-devel
BuildRequires: kdebase4-devel 
BuildRequires: bzip2-devel 
BuildRequires: libintl 
BuildRequires: jpeg-devel 
BuildRequires: lcms-devel 
BuildRequires: mng-devel
BuildRequires: png-devel 
BuildRequires: libz-devel 
BuildRequires: xscreensaver
BuildRequires: xscreensaver-gl
BuildRequires: mesaglut-devel
BuildRequires: mesaglu-devel
BuildRequires: kdebase4-workspace-devel
Requires: kde4-kworldclock
Requires: %{name}-emoticons
Requires: %{name}-kwin-icewm-themes
Requires: %{name}-kscreensaver
Requires: %{name}-sounds
Requires: %{name}-styles
Requires: %{name}-wallpapers

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
Requires: %name-core = %version

%description emoticons
%{name} emoticons.

%files emoticons
%defattr(-,root,root)
%_kde_datadir/emoticons/*

#---------------------------------------------

%package kwin-icewm-themes
Summary: %{name} kwin-icewm-themes
Group: Graphical desktop/KDE
Requires: %name-core = %version

%description kwin-icewm-themes
%{name} icewm-themes.

%files kwin-icewm-themes
%defattr(-,root,root)
%_kde_appsdir/kwin/icewm-themes/*

#---------------------------------------------

%package kscreensaver
Summary: %{name} kscreensaver
Group: Graphical desktop/KDE
Requires: %name-core = %version

%description kscreensaver
%{name} kscreensaver.

%files kscreensaver
%defattr(-,root,root)
%_kde_appsdir/kfiresaver
%_kde_appsdir/kscreensaver
%_kde_bindir/*.kss
%_kde_bindir/kxsconfig
%_kde_bindir/kxsrun
%_kde_datadir/kde4/services/ScreenSavers/*

#---------------------------------------------

%package -n kde4-kworldclock
Summary: %{name} kworldclock
Group: Graphical desktop/KDE
Requires: %name-core = %version

%description -n kde4-kworldclock
%{name} kworldclock.

%files -n kde4-kworldclock
%defattr(-,root,root)
%_kde_appsdir/kworldclock

#---------------------------------------------

%package sounds
Summary: %{name} sounds
Group: Graphical desktop/KDE
Requires: %name-core = %version

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
Requires: %name-core = %version

%description styles
%{name} styles.

%files styles
%defattr(-,root,root)
%_kde_appsdir/kstyle
%_kde_libdir/kde4/kstyle_phase_config.so
%_kde_libdir/kde4/plugins/styles/phasestyle.so

#---------------------------------------------

%package wallpapers
Summary: %{name} wallpapers
Group: Graphical desktop/KDE
Requires: %name-core = %version

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

