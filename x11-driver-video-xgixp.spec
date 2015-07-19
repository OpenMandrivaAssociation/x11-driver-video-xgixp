%define debug_package	%{nil}
%define _disable_ld_no_undefined 1

Name: x11-driver-video-xgixp
Version: 1.8.1
Release: 11
Summary: X.org driver for XGIxp Cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-xgixp-%{version}.tar.bz2
Patch1:	xf86-video-xgixp-1.8.1-mibstore.patch

BuildRequires: x11-util-macros		>= 1.1.5
BuildRequires: pkgconfig(libdrm)	>= 2.3.0
BuildRequires: pkgconfig(pixman-1)	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: pkgconfig(gl)		>= 7.0.2
BuildRequires: x11-server-devel		>= 1.12
Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-xgixp is the X.org driver for Generic XGIxp Cards.

%prep
%setup -qn xf86-video-xgixp-%{version}
%patch1 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/xgixp_drv.so
%{_mandir}/man4/xgixp.*



%changelog
* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.8.0-5
+ Revision: 787300
- Rebuild for x11-server 1.12
- Update build dependencies

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.8.0-4
+ Revision: 748347
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8.0-3
+ Revision: 703724
- rebuild for new x11-server

* Thu Dec 16 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.8.0-2mdv2011.0
+ Revision: 622334
- Add patch to allow loading the driver without unresolved symbols.

* Tue Aug 17 2010 Thierry Vignaud <tv@mandriva.org> 1.8.0-1mdv2011.0
+ Revision: 570788
- new release

* Thu Feb 18 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.7.99.4-1mdv2010.1
+ Revision: 507726
- This driver was sent to /old because it was never submitted to cooker, but it
  sill compiles and maybe works (I don't have the hardware to test). Let's keep it
  in cooker for now.
- New release: 1.7.99.4

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - old directory, without matching package

  + Thierry Vignaud <tv@mandriva.org>
    - improved description
    - fix group
    - add missing dot at end of description
    - improved summary

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Update to upstream release 1.7.99.3.
      Still unbuildable because of lack of Mesa and kernel update to suport
      xgixp modules.
    - Modify documentation to show how to properly checkout the sources.
      Rename spec file to match package name.
      Package still unbuildable in cooker.
    - Added "guessed" BuildRequires to when kernel/mesa/drm bits be updated as
      this hardware is quite new and there is no official version of either
      (kernel/mesa/drm) with support, i.e. code still in "git master".
    - Remove -devel package as it isn't really required as it provides only 2 files
      that aren't even header files; still don't install the .la files.
      All dependency files should be stored in the x11-util-modular package as they
      are only required for the "modular" build.
    - Move .la files to new -devel package, and also add .deps files to -devel package.
      This package is still unbuildable because it requires bits in git master
      (i.e. not yet available on released versions) of mesa/drm/kernel.
    - This package doesn't have a single tag in git. Making this commit, without
      adding a tag to "document" that the a review was done, before starting a
      "new review pass" to make sure everything is correct.
    - Add x11-driver-video-xgi to cooker.
      Note that the package is broken at the current moment due to 2 problems:
    --disable-dri isn't correct, because XF86DRI is defined in
      /usr/include/xorg/xorg-server.h and this is the value the --disable-dri
      defines, or not in config.h. So trying to patch to disable-dri is pointless
      as the XF86DRI define is implicit if X Server was compiled with DRI extension.
      Driver is also broken at the current moment due to also needing to
      update/patch libdrm and kernel.
    - Add x11-driver-video-xgixp to cooker.

