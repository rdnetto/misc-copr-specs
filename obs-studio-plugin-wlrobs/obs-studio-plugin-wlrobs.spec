Name:           obs-studio-plugin-wlrobs
Version:        1.1
Release:        1%{?dist}
Summary:        wlrobs is an obs-studio plugin that allows you to screen capture on wlroots based wayland compositors

License:        GPL-3.0
URL:            https://hg.sr.ht/~scoopta/wlrobs
Source0:        https://hg.sr.ht/~scoopta/wlrobs/archive/v%{version}.tar.gz

BuildRequires:  ninja-build meson wayland-devel obs-studio-devel clang
Requires:       obs-studio

%description
wlrobs is an obs-studio plugin that allows you to screen capture on wlroots based wayland compositors


# Ignore absence of debug files
%global debug_package %{nil}

%prep
%autosetup -n wlrobs-v%{version}
meson setup build


%build
ninja -C build


%install
rm -rf %{buildroot}
%{__install} -d %{buildroot}/%{_libdir}/obs-plugins/
%{__install} build/libwlrobs.so %{buildroot}/%{_libdir}/obs-plugins/


%files
%license COPYING.md
%{_libdir}/obs-plugins/libwlrobs.so
