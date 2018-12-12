%global debug_package %{nil}
%global commit0 a6b903fb6d78f1515b2c50ba17ae50ead8cf5b72
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:       dav1d
Version:    0.1.0
Release:    1%{?gver}%{dist}
Summary:    dav1d is an AV1 decoder

Group:      Applications/Multimedia
License:    BSD
URL:        https://code.videolan.org/videolan/dav1d
Source:     https://code.videolan.org/videolan/dav1d/-/archive/%{commit0}/%{name}-%{commit0}.tar.bz2

BuildRequires: gcc >= 5.1.1-2

# Basic tools and libraries
BuildRequires: ninja-build 
BuildRequires: meson 
BuildRequires: nasm 
BuildRequires: git
BuildRequires: doxygen
Requires: %{name}-libs = %{version}-%{release}

%description 
V1 cross-platform Decoder, focused on speed and correctness.

%package        libs
Summary:        Libraries for dav1d

%description    libs
This package contains the libraries for dav1d

%package        devel
Summary:        Development package for dav1d
Requires:       %{name}-libs = %{version}-%{release}

%description    devel
This package contains development files for dav1d

%prep

%autosetup -n %{name}-%{commit0}

%build
meson build --buildtype release --prefix=%{_prefix} --libdir=%{_libdir}

%ninja_build -C build

%install
%ninja_install -C build

%check
%ninja_test -C build

%files
%license COPYING
%doc README.md
%{_bindir}/dav1d

%files  libs  
%license COPYING
%doc README.md
%{_libdir}/libdav1d.so.*

%files devel
%license COPYING
%doc README.md
%{_includedir}/dav1d/common.h
%{_includedir}/dav1d/data.h
%{_includedir}/dav1d/dav1d.h
%{_includedir}/dav1d/headers.h
%{_includedir}/dav1d/picture.h
%{_libdir}/libdav1d.so
%{_libdir}/pkgconfig/dav1d.pc

%changelog

* Tue Dec 11 2018 - David Va <davidva AT tuta DOT io> 0.1.0-7.gita6b903f
- Updated to 0.1.0

* Wed Dec 05 2018 - David Va <davidva AT tuta DOT io> 0.0.1-7.gitc3980e3
- Initial build
