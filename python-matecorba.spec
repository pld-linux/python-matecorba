# NOTE: it's deprecated package, a binding for MATE <= 1.4 APIs
Summary:	Python binding for the MateCORBA2 CORBA implementation
Summary(pl.UTF-8):	Wiązanie Pythona do implementacji CORBA MateCORBA2
Name:		python-matecorba
Version:	1.4.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	http://pub.mate-desktop.org/releases/1.4/python-corba-%{version}.tar.xz
# Source0-md5:	bad4a0d28b006f1c4179c89ba266540e
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	mate-corba-devel >= 1.2.0
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Python language binding for the MateCORBA2 CORBA
implementation.

%description -l pl.UTF-8
Ten pakiet to wiązanie Pythona do implementacji CORBA o nazwie
MateCORBA2.

%package devel
Summary:	Development files for PyMateCORBA package
Summary(pl.UTF-8):	Pliki programistyczne pakietu PyMateCORBA
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mate-corba-devel >= 1.2.0

%description devel
Development files for PyMateCORBA package.

%description devel -l pl.UTF-8
Pliki programistyczne pakietu PyMateCORBA.

%prep
%setup -q -n python-corba-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/*.la
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{py_sitedir}/MateCORBA.so
%{py_sitedir}/MATECORBA.py[co]
%{py_sitedir}/MatePortableServer.py[co]

%files devel
%defattr(644,root,root,755)
%{_includedir}/pymatecorba-2
%{_pkgconfigdir}/pymatecorba-2.pc
