Summary:	Additional artwork (themes, sound themes, icons,etc...) for KDE
Name:		kdeartwork4
Version:	4.14.1
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdeartwork-%{version}.tar.xz
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	xscreensaver-base
BuildRequires:	pkgconfig(eigen2)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libkexiv2)
BuildRequires:	pkgconfig(xt)
Conflicts:	kde-wallpapers < 2:4.10.0
Obsoletes:	kdeartwork4-aurorae-themes-air-oxygen < 1:4.10.0
Obsoletes:	kdeartwork4-aurorae-themes-oxygen < 1:4.10.0
Obsoletes:	kdeartwork4-sounds < 1:4.12.0
Suggests:	%{name}-emoticons
Suggests:	%{name}-kscreensaver
Suggests:	%{name}-styles
Suggests:	%{name}-wallpapers
Suggests:	%{name}-color-schemes

%description
Additional artwork (themes, sound themes, icons,etc...) for KDE.

%files
%doc README

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

%package icons-theme-mono
Summary:	Mono Icons from kde4
Group:		Graphical desktop/KDE
Buildarch:	noarch

%description icons-theme-mono
Mono icons theme

%files icons-theme-mono
%{_kde_iconsdir}/mono

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

%package -n plasma-desktoptheme-tibanna
Summary:	Plasma tibanna desktopthemes
Group:		Graphical desktop/KDE
Provides:	plasma-desktoptheme
Buildarch:	noarch

%description -n plasma-desktoptheme-tibanna
Plasma tibanna desktopthemes.

%files -n plasma-desktoptheme-tibanna
%{_kde_appsdir}/desktoptheme/Tibanna

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

%package wallpapers
Summary:	%{name} wallpapers
Group:		Graphical desktop/KDE
Buildarch:	noarch

%description wallpapers
%{name} wallpapers.

%files wallpapers
%{_kde_datadir}/wallpapers/*

#-----------------------------------------------------------------------------

%prep
%setup -q -n kdeartwork-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1
- Drop sounds subpackage as it's no longer provided by upstream
- Sort subpackages

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4
- Fix main summary

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3
- Drop no longer needed l10n-ru patch

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0
- Drop and obsolete aurorae-themes-air-oxygen and aurorae-themes-oxygen
  subpackages as upstream did so
- Add Conflicts on older kde-wallpapers because some wallpapers were moved
  from it to kdeartwork4 in 4.10.0

* Sun Jan 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.5-1
- New version 4.9.5

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Mon Aug 13 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- Update to 4.9.0

* Wed Jul 18 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- Update to 4.8.97

* Sun Jul 01 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- Update to 4.8.95
- Add pkgconfig(libkexiv2) to BuildRequires
- Spec cleanup

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.3-1
- update to 4.8.3

* Thu Apr 19 2012 Mikhail Kompaniets <mkompan@mezon.ru> 1:4.8.2-2
- Russian localization for .desktop files

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 1:4.8.1-1
- update to 4.8.1

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-1
+ Revision: 762513
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758098
- New upstream tarball

* Tue Jan 03 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 748918
- New version

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-1
+ Revision: 739367
- New upstream tarball

* Sat Nov 19 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.80-1
+ Revision: 731895
- New upstream tarball 4.7.80

* Wed Sep 21 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.41-1
+ Revision: 700668
- Fix file list
- Fix buildrequires
- New version 4.7.41

* Mon Jun 13 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.4-1
+ Revision: 684401
- New version 4.6.4

* Fri May 13 2011 Funda Wang <fwang@mandriva.org> 1:4.6.3-1
+ Revision: 674321
- update br
- new version 4.6.3

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:4.6.2-2
+ Revision: 666019
- mass rebuild

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove mkrel
    - New version 4.6.2

* Mon Feb 28 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.1-1
+ Revision: 640723
- New version 4.6.1

* Mon Jan 31 2011 Funda Wang <fwang@mandriva.org> 1:4.6.0-1
+ Revision: 634356
- BR xt

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New version KDE 4.6 Final

* Thu Jan 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.95-2mdv2011.0
+ Revision: 629116
- New version KDE 4.6 RC2

* Fri Dec 24 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.90-2mdv2011.0
+ Revision: 624580
- Fix file list
- New upstream tarball

* Wed Dec 08 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.85-1mdv2011.0
+ Revision: 616340
- New upstream tarball

* Sat Nov 27 2010 Funda Wang <fwang@mandriva.org> 1:4.5.80-1mdv2011.0
+ Revision: 601705
- new version 4.5.80 (aka 4.6 beta1)

* Sat Nov 20 2010 Funda Wang <fwang@mandriva.org> 1:4.5.77-0.svn1198704.1mdv2011.0
+ Revision: 599199
- new snapshot 4.5.77

* Fri Oct 29 2010 Funda Wang <fwang@mandriva.org> 1:4.5.74-0.svn1190490.1mdv2011.0
+ Revision: 589893
- new snapshot 4.5.74

* Fri Oct 08 2010 Funda Wang <fwang@mandriva.org> 1:4.5.71-0.svn1183776.1mdv2011.0
+ Revision: 584220
- New snapshot 4.5.71

* Wed Sep 15 2010 Funda Wang <fwang@mandriva.org> 1:4.5.68-2mdv2011.0
+ Revision: 578671
- obsoletes old arch package

* Wed Sep 15 2010 Funda Wang <fwang@mandriva.org> 1:4.5.68-1mdv2011.0
+ Revision: 578564
- New snapshot 4.5.68

* Tue Sep 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.67-1mdv2011.0
+ Revision: 576448
- New version 4.5.67

* Fri Aug 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.0-1mdv2011.0
+ Revision: 566565
- New upstream tarball
- Update to version 4.5.0

* Wed Jul 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.95-1mdv2011.0
+ Revision: 562712
- KDE 4.5 RC3

* Tue May 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-1mdv2010.1
+ Revision: 542097
- Update to version 4.4.3

* Sun Mar 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.2-1mdv2010.1
+ Revision: 528310
- Update to version 4.4.2

* Tue Mar 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.1-1mdv2010.1
+ Revision: 513405
- Update to version 4.4.1

* Tue Feb 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.0-1mdv2010.1
+ Revision: 502606
- Update to version 4.4.0

* Mon Feb 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.98-1mdv2010.1
+ Revision: 498939
- Update to version 4.3.98 aka "kde 4.4 RC3"
- Update to version 4.3.98 aka "kde 4.4 RC3"

* Mon Jan 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.95-1mdv2010.1
+ Revision: 495975
- Update to version 4.3.95 aka "kde 4.4 RC2"

* Sun Jan 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.90-1mdv2010.1
+ Revision: 488226
- Update to kde 4.4 rc1

* Mon Dec 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.85-1mdv2010.1
+ Revision: 480703
- Update to kde 4.4 beta2

* Fri Dec 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.80-1mdv2010.1
+ Revision: 473204
- Update to kde 4.4 beta1

* Sat Nov 28 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.77-1mdv2010.1
+ Revision: 470734
- Update to kde 4.3.77

* Mon Nov 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.75-1mdv2010.1
+ Revision: 466602
- Update to kde 4.3.75

* Wed Nov 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.73-2mdv2010.1
+ Revision: 465063
- Rebuild against new qt

* Sun Nov 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.73-1mdv2010.1
+ Revision: 462974
- Update to kde 4.3.73

* Tue Oct 06 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.2-1mdv2010.0
+ Revision: 454431
- New upstream release 4.3.2.

* Sat Sep 19 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.1-3mdv2010.0
+ Revision: 444665
- Add eigen2 as BuildRequires ( tks MIB )

* Fri Sep 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.1-2mdv2010.0
+ Revision: 444213
- Add obsolete for kde3 upgrade

* Tue Sep 01 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.1-1mdv2010.0
+ Revision: 423209
- New upstream release 4.3.1.

* Sat Aug 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.0-2mdv2010.0
+ Revision: 416481
- Obsolete kde3 packages

* Tue Aug 04 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.0-1mdv2010.0
+ Revision: 409411
- New upstream release 4.3.0.

* Thu Jul 23 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.98-1mdv2010.0
+ Revision: 398845
- Update to KDE 4.3 RC3

* Sat Jul 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.96-1mdv2010.0
+ Revision: 394886
- Update to Rc2

* Thu Jun 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.95-1mdv2010.0
+ Revision: 389228
- Update to kde 4.3Rc1

* Thu Jun 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.90-1mdv2010.0
+ Revision: 382827
- Update to beta2

* Fri May 29 2009 Funda Wang <fwang@mandriva.org> 1:4.2.88-1mdv2010.0
+ Revision: 380764
- New version 4.2.88

* Fri May 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.87-1mdv2010.0
+ Revision: 378798
- Update to kde   4.2.87

* Fri May 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.85-1mdv2010.0
+ Revision: 373532
- Update to kde 4.2.85

* Sun May 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.71-0.svn961800.1mdv2010.0
+ Revision: 371232
- Update to kde 4.2.71
- Update to kde 4.2.70
- Update to kde 4.2.70

* Thu Apr 02 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.2-2mdv2009.1
+ Revision: 363557
- Removed inavlid requires pulling down unecessary large amount of packages

* Fri Mar 27 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.2-1mdv2009.1
+ Revision: 361731
- Update with 4.2.2 try#1 packages

* Sat Feb 28 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.1-1mdv2009.1
+ Revision: 346211
- KDE 4.2.1 try#1 upstream release

* Mon Feb 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.0-2mdv2009.1
+ Revision: 340865
- Rebuild against qt4.5

* Tue Jan 27 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.0-1mdv2009.1
+ Revision: 334355
- Update with official 4.2.0 upstream tarball

* Sun Jan 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.96-2mdv2009.1
+ Revision: 328173
- Add back kscreensaver now that kdebase4-workspace is found

* Fri Jan 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.96-1mdv2009.1
+ Revision: 327456
- Remove kscreensaver for now
- Fix file list

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Release Candidate 1 - 4.1.96

* Sun Dec 14 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.85-2mdv2009.1
+ Revision: 314206
- Rebuild because of BS failure
- New version KDE 4.2 Beta2

* Thu Dec 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.82-1mdv2009.1
+ Revision: 313357
- Update to kde 4.1.82

* Sun Nov 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.81-1mdv2009.1
+ Revision: 308647
- Update to kde 4.1.81

* Wed Nov 19 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.80-1mdv2009.1
+ Revision: 304565
- Update with Beta 1 - 4.1.80

* Fri Nov 14 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.73-1mdv2009.1
+ Revision: 303171
- Update to kde 4.1.73

* Sun Nov 09 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.71-2mdv2009.1
+ Revision: 301655
- Bump release
- More obsoletes
- Obsoletes kdeartwork-screensavers
- Remove wrong obsolete on core package
- change Requires into Suggests in the metapackage
- Provide additionnal icons set
  Obsolete kde3 kdeartwork icons set

* Sat Oct 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.71-1mdv2009.1
+ Revision: 297064
- New version 4.1.71

* Mon Oct 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.70-1mdv2009.1
+ Revision: 295843
- Fix Build
- Update to kde 4.1.70

* Tue Sep 30 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:4.1.2-2mdv2009.0
+ Revision: 290198
- Remove unused patches
- Fix the crossfade effect by processing it offscreen before drawing onscreen

* Sat Sep 27 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.2-1mdv2009.0
+ Revision: 288842
- KDE 4.1.2 arriving.

* Sun Aug 31 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.1-1mdv2009.0
+ Revision: 277844
- Upgrade to forthcoming 4.1.1 packages

* Tue Aug 26 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 1:4.1.0-4mdv2009.0
+ Revision: 276238
- Added some pre-effects to kscreensaver

* Wed Aug 13 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 1:4.1.0-3mdv2009.0
+ Revision: 271431
- Added "Use crossfade effect" option to slideshow screensaver setup.

* Mon Aug 11 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 1:4.1.0-2mdv2009.0
+ Revision: 270772
- Added crossfade transiction effect

* Fri Jul 25 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.0-1mdv2009.0
+ Revision: 247602
- Update with Release Candidate 1 - 4.1.0

* Thu Jul 10 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.98-1mdv2009.0
+ Revision: 233194
- Update with Release Candidate 1 - 4.0.98

* Mon Jul 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.85-1mdv2009.0
+ Revision: 232433
- New version kde 4.0.85

* Sun Jun 29 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.84-1mdv2009.0
+ Revision: 230059
- Fix BuildRequires

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with new snapshot tarballs 4.0.84
    - Screensavers are back

* Thu Jun 19 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.83-1mdv2009.0
+ Revision: 226098
- Update with new snapshot tarballs 4.0.83
- Update with new snapshot tarballs 4.0.82
- Update with new snapshot tarballs 4.0.81

* Sun May 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.80-2mdv2009.0
+ Revision: 211069
- Versionnate BuildRequires

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 beta1

* Fri May 16 2008 Funda Wang <fwang@mandriva.org> 1:4.0.74-1mdv2009.0
+ Revision: 208071
- New version 4.0.74

* Thu May 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.73-1mdv2009.0
+ Revision: 204751
- Update to kde 4.0.73

* Wed May 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.72-1mdv2009.0
+ Revision: 202767
- Fix File list
- Update to kde 4.0.72
- New snapshot 4.0.70
- New snapshot 4.0.69

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 alpha 1

* Fri Mar 28 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.3-1mdv2008.1
+ Revision: 191015
- Update for last stable release 4.0.3

* Sat Mar 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-2mdv2008.1
+ Revision: 182259
- Rebuild against new qt4 changes

* Sat Mar 01 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.2-1mdv2008.1
+ Revision: 177462
- New upstream bugfix release 4.0.2

* Mon Feb 11 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.1-1mdv2008.1
+ Revision: 165438
- Update for 4.0.1

* Sun Jan 13 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.0-3mdv2008.1
+ Revision: 151033
+ rebuild (emptylog)

* Sun Jan 13 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.0-2mdv2008.1
+ Revision: 151023
- Update for final stable 4.0.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Funda Wang <fwang@mandriva.org>
    - should require with epoch

* Mon Dec 24 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.97.1-0.751522.1mdv2008.1
+ Revision: 137446
- New snapshot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 11 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.97.1-0.746274.1mdv2008.1
+ Revision: 117167
- New snapshot

* Sat Dec 01 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.743525.2mdv2008.1
+ Revision: 114250
- New snapshot

* Fri Nov 23 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.739275.2mdv2008.1
+ Revision: 111564
- New snapshot
- KDE4 RC1

* Thu Oct 25 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.1-0.728852.2mdv2008.1
+ Revision: 102184
- Fix BuildRequires
- New snapshot
- New snapshot for Beta2
  [BUGFIX] Fix Requires (Bug #32991)

* Tue Aug 07 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.92.0-0.697235.1mdv2008.0
+ Revision: 59881
- Updating to revision 697235
- Update for revision 694291

  + Laurent Montel <lmontel@mandriva.org>
    - new snapshot
    - it compiles with enable-final
    - new snapshot


* Thu Jan 25 2007 Laurent Montel <lmontel@mandriva.com> 3.80.2-0.20070123.1mdv2007.0
+ Revision: 113088
- new snapshot

* Thu Jan 18 2007 Laurent Montel <lmontel@mandriva.com> 3.80.2-0.20070117.1mdv2007.1
+ Revision: 110238
- Update

* Wed Jan 10 2007 Laurent Montel <lmontel@mandriva.com> 3.80.2-0.20070109.1mdv2007.1
+ Revision: 106997
- Update
- Fix file list

* Thu Jan 04 2007 Laurent Montel <lmontel@mandriva.com> 3.80.2-0.20070103.1mdv2007.1
+ Revision: 104119
- Update
- Import kdeartwork4

* Wed Dec 27 2006 Laurent Montel <lmontel@mandriva.com> 3.5.5-1mdv2007.0
- First package

