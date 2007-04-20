
# remove it when kde4 will be official kde package
%define _prefix /opt/kde4/
%define _libdir %_prefix/%_lib
%define _datadir %_prefix/share/
%define _bindir %_prefix/bin
%define _includedir %_prefix/include/
%define _iconsdir %_datadir/icons/
%define _sysconfdir %_prefix/etc/
%define _docdir %_datadir/doc/

%define branch_date 20070418

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define compile_apidox 1
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}


Name:		kdeartwork4
Version:   	3.80.3
Release:    %mkrel 0.%branch_date.1
Group: 		Graphical desktop/KDE
Summary: 	Kdeartwork
URL:		ftp://ftp.kde.org/pub/kde/stable/%version/src/
# Source comes from kde branch.
License:  	GPL
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeartwork-%version-%branch_date.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdeartwork-%version.tar.bz2
%endif
BuildRoot: 	%_tmppath/%name-%version-%release-root
Packager:	Mandriva Linux KDE Team <kde@mandriva.com>
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
BuildRequires:	xscreensaver
BuildRequires:	xscreensaver-gl
BuildRequires: mesaglut-devel
BuildRequires:	mesaglu-devel
Requires: kdebase4-progs

Patch1:		kdeartwork-3.5.4-fix-screensaver-only-showin-kde.patch

%description
Additional artwork (themes, sound themes, icons,etc...) for KDE.

%files
%defattr(-,root,root,-)

%_bindir/kbanner.kss       
%_bindir/klines.kss        
%_bindir/kblob.kss         
%_bindir/klorenz.kss       
%_bindir/kpolygon.kss      
%_bindir/kslideshow.kss    
%_bindir/kswarm.kss
%_bindir/kclock.kss
%_bindir/kpartsaver.kss    
%_bindir/kscience.kss      
%_bindir/kvm.kss
%_bindir/keuphoria.kss
%_bindir/kflux.kss
%_bindir/kfountain.kss
%_bindir/kgravity.kss
%_bindir/ksolarwinds.kss
%_bindir/kwave.kss
%_bindir/kxsrun
%_bindir/kxsconfig
%_bindir/krotation.kss
%dir %_datadir/apps/kscreensaver/
%_datadir/apps/kscreensaver/*.png
%dir %_datadir/emoticons/
%dir %_datadir/emoticons/tweakers.net/
%_datadir/emoticons/tweakers.net/*.png
%_datadir/emoticons/tweakers.net/*.xml
%dir %_datadir/emoticons/phpBB/
%_datadir/emoticons/phpBB/*.png
%_datadir/emoticons/phpBB/*.xml
%dir %_datadir/emoticons/greggman.com/
%_datadir/emoticons/greggman.com/*.png
%_datadir/emoticons/greggman.com/*.xml
%dir %_datadir/emoticons/ccmathteam.com/
%_datadir/emoticons/ccmathteam.com/*.png
%_datadir/emoticons/ccmathteam.com/*.xml
%dir %_datadir/emoticons/RedOnes/
%_datadir/emoticons/RedOnes/*.png
%_datadir/emoticons/RedOnes/*.xml
%dir %_datadir/emoticons/Plain/
%_datadir/emoticons/Plain/*.png
%_datadir/emoticons/Plain/*.xml
%dir %_datadir/emoticons/KMess/
%_datadir/emoticons/KMess/*.png
%_datadir/emoticons/KMess/*.xml
%dir %_datadir/emoticons/KMess-Violet/
%_datadir/emoticons/KMess-Violet/*.png
%_datadir/emoticons/KMess-Violet/*.xml
%dir %_datadir/emoticons/KMess-Cartoon/
%_datadir/emoticons/KMess-Cartoon/*.png
%_datadir/emoticons/KMess-Cartoon/*.xml
%dir %_datadir/emoticons/KMess-Blue/
%_datadir/emoticons/KMess-Blue/*.png
%_datadir/emoticons/KMess-Blue/*.xml
%dir %_datadir/emoticons/Boxed/
%_datadir/emoticons/Boxed/*.png
%_datadir/emoticons/Boxed/*.xml
%dir %_datadir/emoticons/GroupWise/
%_datadir/emoticons/GroupWise/emoticons.xml
%dir %_datadir/apps/kworldclock/
%dir %_datadir/apps/kworldclock/maps/
%dir %_datadir/apps/kworldclock/maps/alt/
%_datadir/apps/kworldclock/maps/alt/*.jpg
%_datadir/apps/kworldclock/maps/alt/*.desktop
%dir %_datadir/apps/kworldclock/maps/bio/
%_datadir/apps/kworldclock/maps/bio/*.jpg
%_datadir/apps/kworldclock/maps/bio/*.desktop
%dir %_datadir/apps/kworldclock/maps/caida/
%_datadir/apps/kworldclock/maps/caida/*.jpg
%_datadir/apps/kworldclock/maps/caida/*.desktop
%dir %_datadir/apps/kworldclock/maps/caida_bw/
%_datadir/apps/kworldclock/maps/caida_bw/*.jpg
%_datadir/apps/kworldclock/maps/caida_bw/*.desktop
%dir %_datadir/apps/kworldclock/maps/mggd/
%_datadir/apps/kworldclock/maps/mggd/*.jpg
%_datadir/apps/kworldclock/maps/mggd/*.desktop
%dir %_datadir/apps/kworldclock/maps/rainfall/
%_datadir/apps/kworldclock/maps/rainfall/*.jpg
%_datadir/apps/kworldclock/maps/rainfall/*.desktop
%dir %_datadir/sounds/
%_datadir/sounds/*.wav

%_datadir/apps/kfiresaver/*.ogg
%_datadir/apps/kfiresaver/*.desc
%_datadir/apps/kfiresaver/*.png
%_iconsdir/Locolor/*
%_iconsdir/Locolor/index.theme
%_iconsdir/ikons/*
%_iconsdir/kids/*
%_iconsdir/slick/*
%_datadir/apps/kwin/icewm-themes/MenschMaschine/*
%_datadir/apps/kwin/icewm-themes/Model/*
%_datadir/services/ScreenSavers/*.desktop
%_datadir/wallpapers/*.jpg
%_datadir/wallpapers/*.desktop
%_datadir/wallpapers/*.svgz
%_datadir/wallpapers/*.png


#-------------------------------------------------------------------------

%package 	kde-classic
Summary:    Default Icons from kde4.0 
Group:      Graphical desktop/KDE

%description kde-classic
Default Icons from kde4.0.

%files kde-classic
%defattr(-,root,root,-)
%dir %_iconsdir/kdeclassic/
%_iconsdir/kdeclassic/*


#-------------------------------------------------------------------------

%package	screensaver-gl
Summary:    Screensaver using OpenGL 
Group:      Graphical desktop/KDE
Requires:	kdebase4-progs 
Requires:	%name = %version-%release, xscreensaver-gl

%description screensaver-gl
Screensaver using OpenGL.

%files screensaver-gl
%defattr(-,root,root,-)

#-------------------------------------------------------------------------

%prep
%setup  -q -nkdeartwork-%version-%branch_date

%build
cd $RPM_BUILD_DIR/kdeartwork-%version-%branch_date
mkdir build
cd build
export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=Debug \
%endif
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
	../

%make

%install

rm -fr %buildroot
cd $RPM_BUILD_DIR/kdeartwork-%version-%branch_date
cd build


export PATH=%_bindir:$PATH

make DESTDIR=%buildroot install

%clean
rm -fr %buildroot


