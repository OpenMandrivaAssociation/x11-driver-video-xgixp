%define debug_package	%{nil}

Name: x11-driver-video-xgixp
Version: 1.8.0
Release: 5
Summary: X.org driver for XGIxp Cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-xgixp-%{version}.tar.bz2
Patch0: 0001-Remove-xf86-LoaderRe-q-f-Sym-bols-Lists-and-their-sy.patch

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
%apply_patches

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

