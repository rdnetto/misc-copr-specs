# Disable debuginfo package as Stack doesn't produce it
%global debug_package %{nil}

Name:           dispatch-merge
Version:        1.2.1.0
Release:        1%{?dist}
Summary:        CLI tool for resolving merge conflicts, inspired by dispatch-conf.

License:        Apache2
URL:            https://bitbucket.org/rdnetto/dispatch-merge
Source0:        https://bitbucket.org/rdnetto/dispatch-merge/get/%{version}.tar.gz

BuildRequires:  stack
# Used for configuring GHC
BuildRequires:  perl
Requires:       gmp-c++
Requires:       zlib

%description
CLI tool for resolving merge conflicts, inspired by dispatch-conf


%prep
%setup -q -n rdnetto-dispatch-merge-af8f98f5c40f

%build
stack build


%install
rm -rf %{buildroot}
stack install --local-bin-path %{buildroot}/%{_bindir}


%files
%license LICENSE
%{_bindir}/dispatch-merge

