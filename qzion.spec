Name: qzion
Version: 0.4.0
Release: 7
License: GPL
Group: Development/KDE and Qt 
Summary: QZion is an canvas abstraction used by and made for QEdje
Source: %name-%version.tar.gz
Patch0: qzion-0.4.0-gcc44.patch
Patch1: qzion-0.4.0-fix-install.patch
Url: http://code.openbossa.org//qedje/
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: qt4-devel
BuildRequires: kde4-macros
BuildRequires: python-qt4
BuildRequires: pkgconfig(python)
#%py_requires -d

%description
QZion is an canvas abstraction used by and made for QEdje

#------------------------------------------------

%define libqzion_major 0
%define libqzion %mklibname qzion %{libqzion_major}

%package -n %libqzion
Summary: Qzionlibrary
Group: System/Libraries

%description -n %libqzion
Qzion library.


%files -n %libqzion
%defattr(-,root,root)
%_kde_libdir/libqzion.so.%{libqzion_major}*

#-----------------------------------------------

%package -n python-qzion
Summary: Qzion python bindings
Group:     Development/KDE and Qt
Requires: python-qt4

%description -n python-qzion
Qzion python bindings.

%files -n python-qzion
%py_sitedir/qzion
%_datadir/sip/qzion

#-----------------------------------------------

%package   devel
Summary:   Devel stuff for kdebase 4
Group:     Development/KDE and Qt
Requires:  %libqzion = %version
%description  devel
Devel packages needed to build QZion apps

%files devel
%defattr(-,root,root)
%_kde_includedir/*.h
%_kde_libdir/pkgconfig/qzion.pc
%_kde_libdir/libqzion.so

#------------------------------------------------

%prep
%setup -q -n qzion-mainline 
%patch0 -p1 -b .gcc44
%patch1 -p0
%build
%cmake_qt4
%make

%install
rm -rf %{buildroot}
cd build
make DESTDIR=%buildroot install

%clean
rm -rf %buildroot


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-4mdv2011.0
+ Revision: 669394
- mass rebuild

* Wed Mar 17 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.4.0-3mdv2011.0
+ Revision: 524158
- Fix install with new cmake

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.4.0-2mdv2010.0
+ Revision: 426845
- rebuild
- fix gcc 4.4 compilation

* Sat Feb 28 2009 Helio Chissini de Castro <helio@mandriva.com> 0.4.0-1mdv2009.1
+ Revision: 345905
- Update with new upstream final 0.4.0 package with python-bindings

* Fri Oct 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.4.0-0.20081023.2mdv2009.1
+ Revision: 296854
- Fix Requires on the devel package

* Thu Oct 23 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.4.0-0.20081023.1mdv2009.1
+ Revision: 296841
- Udpate to git snapshot
- Add kde4-macros as BuildRequire
- import qzion


