Name:           diff-so-fancy
Version:        1.3.0
Release:        1%{?dist}
Summary:        Good-lookin\' diffs. Actually… nah… The best-lookin\' diffs
License:        MIT
URL:            https://github.com/so-fancy/diff-so-fancy
Source0:        https://github.com/so-fancy/diff-so-fancy/archive/v%{version}.tar.gz
Requires:       perl
BuildArch:      noarch

%description
diff-so-fancy strives to make your diffs human readable instead of machine readable. This helps improve code quality and helps you spot defects faster.


%prep
%autosetup
sed -i 's|^use lib .*$|use lib "%{_datadir}/diff-so-fancy";|' diff-so-fancy || die "Sed failed!" 

%build

%install
rm -rf %{buildroot}

%{__install} -d %{buildroot}/%{_datadir}/diff-so-fancy
%{__install} -m 644 lib/* %{buildroot}/%{_datadir}/diff-so-fancy

%{__install} -D -m 755 diff-so-fancy %{buildroot}/%{_bindir}/diff-so-fancy

%files
%license LICENSE
%{_bindir}/diff-so-fancy
%{_datadir}/diff-so-fancy/DiffHighlight.pm

