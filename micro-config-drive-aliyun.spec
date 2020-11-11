Name     : micro-config-drive-aliyun
Version  : 1
Release  : 4
Summary  : Start Aliyun cloud-config user data helper at boot time
Group    : Development/Tools
License  : GPL-3.0
Requires: micro-config-drive

%description
A config-drive handler for Aliyun.

%prep
%build
%check

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -sf ../ucd-aliyun.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/ucd-aliyun.service

%files
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/ucd-aliyun.service

