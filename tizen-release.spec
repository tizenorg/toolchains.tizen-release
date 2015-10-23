%define release_name Magnolia
%define dist_version 2.2.0

# TO enable cumulative installation
%define suse_version 1234
%define tizen_version 0220

Summary:	Tizen release files
Name:		tizen-release
Version:	%{dist_version}
Release:	%{?release_prefix:%{release_prefix}.}1.46.%{?dist}%{!?dist:tizen}
VCS:     toolchains/tizen-release#Z910F_PROTEX_0512-1-g3d903ec99ec2b223e955107cf5ff6111c6daa3fc
License:	GPLv2
Group:		System/Base
URL:		http://www.tizen.com
Provides:	system-release = %{version}-%{release}
Provides:	tizen-release = %{version}-%{release}
Provides:	os-release = %{version}-%{release}
BuildArch:	noarch
Source0:    RPM-GPG-KEY-tizen02

%description
Tizen release files such as various /etc/ files that define the release.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc
echo "Tizen release %{dist_version} (%{release_name})" > $RPM_BUILD_ROOT/etc/tizen-release

ln -s tizen-release $RPM_BUILD_ROOT/etc/system-release

echo "NAME=\"Tizen\"" > $RPM_BUILD_ROOT/etc/os-release
echo "VERSION=\"%{dist_version}, %{release_name}\"" >> $RPM_BUILD_ROOT/etc/os-release
echo "ID=tizen" >> $RPM_BUILD_ROOT/etc/os-release
echo "PRETTY_NAME=\"Tizen %{release_name} (%{dist_version})\"" >> $RPM_BUILD_ROOT/etc/os-release
echo "VERSION_ID=\"%{dist_version}\"" >> $RPM_BUILD_ROOT/etc/os-release

mkdir -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg
cp %{SOURCE0} $RPM_BUILD_ROOT/etc/pki/rpm-gpg
pushd $RPM_BUILD_ROOT/etc/pki/rpm-gpg
ln -sf RPM-GPG-KEY-tizen02 RPM-GPG-KEY-tizen-2-primary
popd

mkdir -p $RPM_BUILD_ROOT/etc/rpm/
echo "%%suse_version %{suse_version}" > $RPM_BUILD_ROOT/etc/rpm/macros.tizen-release
echo "%%tizen_version %{tizen_version}" >> $RPM_BUILD_ROOT/etc/rpm/macros.tizen-release

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config %attr(0644,root,root) /etc/tizen-release
/etc/system-release
/etc/os-release
/etc/pki/rpm-gpg
/etc/rpm/macros.tizen-release
%changelog
* Thu Jun 19 2014 UkJung Kim <ujkim@samsung.com> - None 
- PROJECT: toolchains/tizen-release
- COMMIT_ID: 3d903ec99ec2b223e955107cf5ff6111c6daa3fc
- BRANCH: master
- PATCHSET_REVISION: 3d903ec99ec2b223e955107cf5ff6111c6daa3fc
- CHANGE_OWNER: \"UkJung Kim\" <ujkim@samsung.com>
- PATCHSET_UPLOADER: \"UkJung Kim\" <ujkim@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/520537
- PATCHSET_REVISION: 3d903ec99ec2b223e955107cf5ff6111c6daa3fc
- TAGGER: UkJung Kim <ujkim@samsung.com>
- Gerrit patchset approval info:
- Newton Lee <newton.lee@samsung.com> Code-Review : 2
- UkJung Kim <ujkim@samsung.com> Verified : 1
- CHANGE_SUBJECT: Added macros.tizen-release to enable cumulative installation
- Added macros.tizen-release to enable cumulative installation
