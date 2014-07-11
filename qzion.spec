Summary:	QZion is an canvas abstraction used by and made for QEdje
Name:		qzion
Version:	0.4.0
Release:	11
License:	GPLv2
Group:		Development/KDE and Qt 
Url:		http://code.openbossa.org//qedje/
Source0:	%{name}-%{version}.tar.gz
Patch0:		qzion-0.4.0-gcc44.patch
Patch1:		qzion-0.4.0-fix-install.patch
BuildRequires:	kde4-macros
BuildRequires:	python-qt4
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(QtWebKit)

%description
QZion is an canvas abstraction used by and made for QEdje

#------------------------------------------------

%define major 0
%define libname %mklibname qzion %{major}

%package -n %{libname}
Summary:	Qzionlibrary
Group:		System/Libraries

%description -n %{libname}
Qzion library.


%files -n %{libname}
%{_kde_libdir}/libqzion.so.%{major}*

#-----------------------------------------------

%package -n python-qzion
Summary:	Qzion python bindings
Group:		Development/KDE and Qt
Requires:	python-qt4

%description -n python-qzion
Qzion python bindings.

%files -n python-qzion
%{py_sitedir}/qzion
%{_datadir}/sip/qzion

#-----------------------------------------------

%package   devel
Summary:	Devel stuff for kdebase 4
Group:		Development/KDE and Qt
Requires:	%{libname} = %{version}-%{release}

%description  devel
Devel packages needed to build QZion apps

%files devel
%{_kde_includedir}/*.h
%{_kde_libdir}/pkgconfig/qzion.pc
%{_kde_libdir}/libqzion.so

#------------------------------------------------

%prep
%setup -qn qzion-mainline 
%apply_patches

%build
%cmake_qt4
%make

%install
cd build
%makeinstall_std

