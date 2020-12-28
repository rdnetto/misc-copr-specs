Name:           fasd
Version:        1.0.1
Release:        1%{?dist}
Summary:        Command-line productivity booster, offers quick access to files and directories, inspired by autojump, z and v.

License:        MIT
URL:            https://github.com/clvv/fasd
Source0:        https://github.com/clvv/fasd/archive/%{version}.tar.gz
BuildArch:      noarch

%description
Command-line productivity booster, offers quick access to files and directories, inspired by autojump, z and v.

%prep
%autosetup


%build
%make_build


%install
rm -rf %{buildroot}
%make_install PREFIX=/usr


%files
%{_bindir}/fasd
%{_mandir}/man1/fasd.1.*
%license LICENSE
