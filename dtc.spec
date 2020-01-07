Name:         dtc
Version:      1.4.7
Release:      3
Summary:      Device tree compiler
License:      GPLv2+
URL:          https://devicetree.org/
Source0:      https://ftp.kernel.org/pub/software/utils/%{name}/%{name}-%{version}.tar.xz

BuildRequires: gcc make git flex bison swig
BuildRequires: python2-devel python2-setuptools
Provides:      libfdt
Obsoletes:     libfdt


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

%package      -n python2-libfdt
Summary:      Python 2 bindings for device tree library
%{?python_provide:%python_provide python2-libfdt}
Requires:     %{name} = %{version}-%{release}

%description  -n python2-libfdt
This package provides python2 bindings for libfdt

%package_help

%prep
%autosetup -n %{name}-%{version} -p1 -Sgit

%build
%make_build

%install
%make_install SETUP_PREFIX=$RPM_BUILD_ROOT/usr LIBDIR=%{_libdir} PREFIX=/usr

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

%files -n python2-libfdt
%{python2_sitearch}/*

%files help
%doc Documentation/manual.txt

%changelog
* Tue Jan  7 2020 JeanLeo<liujianliu.liu@huawei.com> - 1.4.7-3
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:update software package

* Thu Sep 19 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.4.7-2
- Package init
