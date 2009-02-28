Name: qzion
Version: 0.4.0
Release: %mkrel 1
License: GPL
Group: Development/KDE and Qt 
Summary: QZion is an canvas abstraction used by and made for QEdje
Source: %name-%version.tar.gz
Url: http://code.openbossa.org//qedje/
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: qt4-devel
BuildRequires: kde4-macros
BuildRequires: python-qt4

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

%build
%cmake_qt4
%make

%install
rm -rf %{buildroot}
cd build
make DESTDIR=%buildroot install

%clean
rm -rf %buildroot
