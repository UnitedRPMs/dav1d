%global commit0 39667c751d427e447cbe8be783cfecd296659e24
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:       dav1d
Version:    0.5.2
Release:    7%{?gver}%{dist}
Summary:    dav1d is an AV1 decoder

Group:      Applications/Multimedia
License:    BSD
URL:        https://code.videolan.org/videolan/dav1d
Source:     https://code.videolan.org/videolan/dav1d/-/archive/%{commit0}/%{name}-%{commit0}.tar.bz2

BuildRequires: gcc >= 5.1.1-2

# Basic tools and libraries
BuildRequires: meson 
BuildRequires: nasm 
BuildRequires: doxygen
Requires: libdav1d = %{version}-%{release}

%description 
V1 cross-platform Decoder, focused on speed and correctness.

%package        -n libdav1d
Summary:        Libraries for dav1d


%description    -n libdav1d
This package contains the libraries for dav1d

%package        -n libdav1d-devel
Summary:        Development package for dav1d
Requires:       libdav1d = %{version}-%{release}

%description    -n libdav1d-devel
This package contains development files for dav1d

%prep

%autosetup -n %{name}-%{commit0}

%build
%meson --buildtype=release

%meson_build
%meson_build doc/html

%install
%meson_install

%check
%meson_test

%clean
rm -rf %{buildroot}

%files
%license COPYING
%doc README.md
%{_bindir}/dav1d

%files  -n libdav1d
%license COPYING
%doc README.md
%{_libdir}/libdav1d.so.*

%files -n libdav1d-devel
%license COPYING 
%doc README.md %{_host_alias}/doc/html
%{_includedir}/dav1d/common.h
%{_includedir}/dav1d/data.h
%{_includedir}/dav1d/dav1d.h
%{_includedir}/dav1d/headers.h
%{_includedir}/dav1d/picture.h
%{_includedir}/dav1d/version.h
%{_libdir}/libdav1d.so
%{_libdir}/pkgconfig/dav1d.pc

%changelog

* Fri Dec 06 2019 - David Va <davidva AT tuta DOT io> 0.5.2-7.git39667c7
- Updated to 0.5.2

* Tue Oct 29 2019 - David Va <davidva AT tuta DOT io> 0.5.1-1.gitbb160f0
- Updated to 0.5.1

* Mon Oct 14 2019 - David Va <davidva AT tuta DOT io> 0.5.0-1.git5f86e71
- Updated to 0.5.0

* Thu Aug 08 2019 - David Va <davidva AT tuta DOT io> 0.4.0-1.git5f63e53
- Updated to 0.4.0

* Mon Aug 05 2019 - David Va <davidva AT tuta DOT io> 0.3.1-3.gitc9427fd
- Fix compatibility 

* Sat Aug 03 2019 - David Va <davidva AT tuta DOT io> 0.3.1-2.gitc9427fd
- Fix compatibility 

* Sat Aug 03 2019 - David Va <davidva AT tuta DOT io> 0.3.1-1.gitc9427fd
- Updated to 0.3.1

* Tue Dec 11 2018 - David Va <davidva AT tuta DOT io> 0.1.0-7.gita6b903f
- Updated to 0.1.0

* Wed Dec 05 2018 - David Va <davidva AT tuta DOT io> 0.0.1-7.gitc3980e3
- Initial build
