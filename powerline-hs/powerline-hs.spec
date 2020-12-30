# Packaging file for Fedora

# Version of powerline included as a submodule of powerline-hs
%define powerline_version 2.5.2

# Disable debuginfo package as Stack doesn't produce it
%global debug_package %{nil}

Name:           powerline-hs
Version:        0.1.4.1
Release:        1%{?dist}
Summary:        Tool for generating shell prompts

License:        Apache2
URL:            https://github.com/rdnetto/powerline-hs
Source0:        https://github.com/rdnetto/powerline-hs/archive/v%{version}.tar.gz
Source1:        https://github.com/powerline/powerline/archive/%{powerline_version}.tar.gz

BuildRequires:  stack
# Used for configuring GHC
BuildRequires:  perl
Requires:       gmp-c++
Requires:       zlib

%description
Tool for generating shell prompts. Haskell clone of powerline.


%prep
%autosetup
# Extract the tarball and move it to the right location
%setup -T -D -a 1 -q
rmdir powerline
mv powerline-%{powerline_version} powerline

%build
export POWERLINE_VER=%{powerline_version}
export POWERLINE_HS_VER=%{version}

stack build


%install
rm -rf %{buildroot}
stack install --local-bin-path %{buildroot}/%{_bindir}


%files
%license LICENSE
%{_bindir}/powerline-hs

