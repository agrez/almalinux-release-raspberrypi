Summary: Raspberry Pi support packages from the AlmaLinux Core SIG repository
Name:    almalinux-release-raspberrypi
Version: 8
Release: 2%{?dist}
License: GPLv2
URL:     https://wiki.almalinux.org/sigs/Core
Source0: almalinux-raspberrypi.repo
Source1: rootfs-expand

Provides: almalinux-release-raspberrypi = 8

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
* Wed Oct 06 2021 Andrew Lukoshko <alukoshko@almalinux.org> - 8-2
- Use mirrors for raspberrypi repo

* Tue Sep 28 2021 Andrew Lukoshko <alukoshko@almalinux.org> - 8-1
- Initial version
