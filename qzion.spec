Name:       qzion
Version:    0.3.0
Release:    %mkrel 1
License:    GPL
Group:      Development/KDE and Qt 
Summary:    QZion is an canvas abstraction used by and made for QEdje
Source:     http://dev.openbossa.org/qedje/downloads/source/qzion/%name-%version.tar.gz
Url:        http://dev.openbossa.org/trac/qedje/
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: qt4-devel

%description
QZion is an canvas abstraction used by and made for QEdje

#-----------------------------------------------
%package   devel
Summary:   Devel stuff for kdebase 4
Group:     Development/KDE and Qt

%description  devel
Devel packages needed to build QZion apps 

%files devel
%defattr(-,root,root)
%_kde_includedir/*.h
%_kde_libdir/pkgconfig/qzion.pc
%_kde_libdir/libqzion.prl
%_kde_libdir/libqzion.so

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


#------------------------------------------------

%prep
%setup -q 

%build
qmake PREFIX=%buildroot%_prefix qzion.pro 
%make

%install
rm -rf %{buildroot}
make DESTDIR=%buildroot install

%clean
rm -rf %buildroot
