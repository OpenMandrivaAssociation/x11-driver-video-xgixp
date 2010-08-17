%define debug_package	%{nil}

Name: x11-driver-video-xgixp
Version: 1.8.0
Release: %mkrel 1
Summary: X.org driver for XGIxp Cards
Group: System/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-xgixp-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-util-macros		>= 1.1.5
BuildRequires: libdrm-devel		>= 2.3.0
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: libmesagl-devel		>= 7.0.2
BuildRequires: x11-server-devel		>= 1.4
Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-xgixp is the X.org driver for Generic XGIxp Cards.

%prep
%setup -q -n xf86-video-xgixp-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/xgixp_drv.la
%{_libdir}/xorg/modules/drivers/xgixp_drv.so
%{_mandir}/man4/xgixp.*
