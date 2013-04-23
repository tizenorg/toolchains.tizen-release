%define release_name Tizen
%define dist_version 1.0.90

Summary:	Tizen release files
Name:		tizen-release
Version:	2.0.0
Release:	1
License:	GPLv2
Group:		System/Base
URL:		http://www.tizen.com
Provides:	system-release = %{version}-%{release}
Provides:	tizen-release = %{version}-%{release}
BuildArch:	noarch
Source0:    RPM-GPG-KEY-tizen02
Source1001: packaging/tizen-release.manifest 

%description
Tizen release files such as various /etc/ files that define the release.

%prep

%build
cp %{SOURCE1001} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc
echo "Tizen release %{dist_version} (%{release_name})" > $RPM_BUILD_ROOT/etc/tizen-release

ln -s tizen-release $RPM_BUILD_ROOT/etc/system-release

cat > $RPM_BUILD_ROOT/etc/os-release <<EOF
NAME=Tizen
VERSION="%{dist_version} (%{release_name})"
ID=tizen
VERSION_ID=%{dist_version}
PRETTY_NAME="Tizen %{dist_version} (%{release_name})"
ANSI_COLOR="0;36"
CPE_NAME="cpe:/o:tizen:tizen:%{dist_version}"
EOF

mkdir -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg
cp %{SOURCE0} $RPM_BUILD_ROOT/etc/pki/rpm-gpg
pushd $RPM_BUILD_ROOT/etc/pki/rpm-gpg
ln -sf RPM-GPG-KEY-tizen02 RPM-GPG-KEY-tizen-2-primary
popd

%files
%manifest tizen-release.manifest
%config %attr(0644,root,root) /etc/tizen-release
%config %attr(0644,root,root) /etc/os-release
/etc/system-release
/etc/pki/rpm-gpg
