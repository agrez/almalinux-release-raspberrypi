Summary: Raspberry Pi support packages from the AlmaLinux Core SIG repository
Name:    almalinux-release-raspberrypi
Version: 9
Release: 1%{?dist}
License: GPLv2
URL:     https://wiki.almalinux.org/sigs/Core
Source0: almalinux-raspberrypi.repo
Source1: rootfs-expand

Provides: almalinux-release-raspberrypi = 9

%description
yum configuration for Raspberry Pi support packages from the AlmaLinux Core SIG.

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/almalinux-raspberrypi.repo
install -D -m 750 %{SOURCE1} %{buildroot}%{_bindir}/rootfs-expand

%files
%defattr(-,root,root)
%{_bindir}/rootfs-expand
%config(noreplace) %{_sysconfdir}/yum.repos.d/almalinux-raspberrypi.repo

%changelog
* Fri May 27 2022 Eduard Abdullin <eabdullin@almalinux.org> - 9-1
- Initial version
