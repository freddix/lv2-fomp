Summary:	LV2 port of MCP, VCO, FIL and WAH plugins
Name:		lv2-fomp
Version:	1.0.0
Release:	1
License:	GPL v3
Group:		Libraries
Source0:	http://download.drobilla.net/fomp-%{version}.tar.bz2
# Source0-md5:	0bb3d8331326d2c3485a9c538436cb56
BuildRequires:	libstdc++-devel
BuildRequires:	lv2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A port of the MCP, VCO, FIL, and WAH plugins by Fons Adriaensen.

%prep
%setup -qn fomp-%{version}

%build
export CC="%{__cc}"
export CXX="%{__cxx}"
export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcxxflags}"
export LDFLAGS="%{rpmldflags}"
./waf configure \
	--prefix=%{_prefix}	\
	--libdir=%{_libdir}	\
	--mandir=%{_mandir}	\
	--nocache
./waf -v build

%install
rm -rf $RPM_BUILD_ROOT

./waf -v install	\
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}/lv2/fomp.lv2
%attr(755,root,root) %{_libdir}/lv2/fomp.lv2/*.so
%{_libdir}/lv2/fomp.lv2/*.ttl

