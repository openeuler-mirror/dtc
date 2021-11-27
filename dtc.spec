%define _wrong_version_format_terminate_build 0

Name:         dtc
Version:      1.6.1
Release:      1
Summary:      Device tree compiler
License:      GPLv2+
URL:          https://devicetree.org/
Source0:      https://www.kernel.org/pub/software/utils/%{name}/%{name}-%{version}.tar.xz

BuildRequires: gcc make git flex bison swig
BuildRequires: python3-devel python3-setuptools
Provides:      libfdt
Obsoletes:     libfdt

Patch1:        openEuler-add-secure-compile-option-in-Makefile.patch


%description
The devicetree is a data structure for describing hardware. Rather than hard coding
every detail of a device into an operating system, many aspects of the hardware can
be described in a data structure that is passed to the operating system at boot time.
The devicetree is used by OpenFirmware, OpenPOWER Abstraction Layer (OPAL), Power
Architecture Platform Requirements (PAPR) and in the standalone Flattened Device
Tree (FDT) form.

%package      devel
Summary:      Development headers for device tree library
Requires:     libfdt = %{version}-%{release}
Provides:     libfdt-static libfdt-devel
Obsoletes:    libfdt-static libfdt-devel

%description  devel
This package provides development files for dtc.

%package      -n python3-libfdt
Summary:      Python 3 bindings for device tree library
%{?python_provide:%python_provide python3-libfdt}
Requires:     %{name} = %{version}-%{release}

%description  -n python3-libfdt
This package provides python3 bindings for libfdt

%package_help

%prep
%autosetup -n %{name}-%{version} -p1 -Sgit

%build
%make_build

%install
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=$RPM_BUILD_ROOT/usr \
             LIBDIR=%{_libdir} BINDIR=%{_bindir} INCLUDEDIR=%{_includedir} V=1

%pre

%preun

%post

%postun

%files
%doc README 
%license GPL README.license
%{_bindir}/*
%{_libdir}/libfdt-%{version}.so
%{_libdir}/libfdt.so.*

%files devel
%{_libdir}/libfdt.so
%{_includedir}/*
%{_libdir}/libfdt.a

%files -n python3-libfdt
%{python3_sitearch}/*

%files help
%doc Documentation/manual.txt

%changelog
* Sat Nov 27 2021 yangzhuangzhuang<yangzhuangzhuang1@huawei.com> - 1.6.1-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:update version to 1.6.1

* Sat Mar 20 2021 shenyangyang<shenyangyang4@huawei.com> - 1.6.0-3
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:Add secure compile option in Makefile

* Wed Sep 9 2020 wangchen<wangchen137@huawei.com> - 1.6.0-2
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:Modify the URL of Source0

* Thu Apr 23 2020 chengquan3<chengquan3@huawei.com> - 1.4.7-3.h1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:Update software to v1.6.0

* Tue Jan  7 2020 JeanLeo<liujianliu.liu@huawei.com> - 1.4.7-3
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:update software package

* Thu Sep 19 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.4.7-2
- Package init
