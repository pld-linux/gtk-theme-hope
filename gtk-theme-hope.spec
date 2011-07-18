# TODO: how to rename this theme if it contains themes for several enviroments
%define		theme	hope
Summary:	Matching GTK2, GTK3 Gnome-shell & XFCE Hope Themes
Name:		gtk-theme-%{theme}
Version:	0.20110706
Release:	0.1
License:	cc-by-nc-sa-3.0
Group:		Themes/GTK+
Source0:	http://www.deviantart.com/download/206207315/hope_gtk3_by_grvrulz-d3erqkz.7z
# Source0-md5:	c3bbd2c431e85ab684b024468f5a823c
URL:		http://grvrulz.deviantart.com/art/Hope-gtk3-206207315
BuildRequires:	p7zip
Requires:	gtk3-theme-engine-unico
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		themedir	%{_datadir}/themes/%{theme}

%description
Port of Hope Gtk+ theme to Gtk3

This theme is now based on Unico Gtk3 engine

%prep
%setup -qcT
7z x %{SOURCE0}

find -name '*~' | xargs rm -v
rm gnome-shell/LICENSE # GPL v3

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{themedir}
cp -a Hope/* $RPM_BUILD_ROOT%{themedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{themedir}
