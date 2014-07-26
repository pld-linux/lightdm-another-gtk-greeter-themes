Summary:	Themes for lightdm-another-gtk-greeter
Name:		lightdm-another-gtk-greeter-themes
Version:	1.0.6.3
Release:	1
License:	GPL v3
Group:		Themes
Source0:	http://github.com/kalgasnik/lightdm-another-gtk-greeter-themes/archive/%{version}.tar.gz?/%{name}-%{version}.tar.gz
# Source0-md5:	d415d5d42933f3838c8369fe10900c3a
URL:		http://github.com/kalgasnik/lightdm-another-gtk-greeter-themes/
Requires:	lightdm-another-gtk-greeter
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themesdir	%{_datadir}/lightdm-another-gtk-greeter/themes

%description
Themes for lightdm-another-gtk-greeter.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themesdir}
cp -pr data/themes/* $RPM_BUILD_ROOT%{_themesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_themesdir}/gtk-greeter-160
%{_themesdir}/panel
