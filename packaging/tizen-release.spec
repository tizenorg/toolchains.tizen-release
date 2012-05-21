%define release_name Tizen
%define dist_version 1.2.0.90

Summary:	Tizen release files
Name:		tizen-release
Version:	1.2.0.90
Release:	1
License:	GPLv2
Group:		System/Base
URL:		http://www.tizen.com
Provides:	system-release = %{version}-%{release}
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

# Install the Tizen GPG RPM pubkey
mkdir -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg
cp %{SOURCE0} $RPM_BUILD_ROOT/etc/pki/rpm-gpg
pushd $RPM_BUILD_ROOT/etc/pki/rpm-gpg
ln -sf RPM-GPG-KEY-tizen02 RPM-GPG-KEY-tizen-2-primary
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%config %attr(0644,root,root) /etc/tizen-release
/etc/system-release
/etc/pki/rpm-gpg
