%define major	2
%define minor	31
%define micro	1

%define libname %mklibname %{name} %{version}
%define devname %mklibname %{name} -d

#
# FIXME: a better soversion may be '0' (see angelscript/projects/meson/meson.build)
# FIXME: install samples and tutorial
#

Summary:	A library that allow applications to extend through external scripts
Name:		angelscript
Version:	%{major}.%{minor}.%{micro}
Release:	1
License:	BSD
Group:		System/Libraries
URL:		http://www.angelcode.com/angelscript/
Source0:	http://www.angelcode.com/%{name}/sdk/files/%{name}_%{version}.zip

BuildRequires:	cmake

%description
The AngelCode Scripting Library, or AngelScript as it is also known, is an
extremely flexible cross-platform scripting library designed to allow
applications to extend their functionality through external scripts. It has
been designed from the beginning to be an easy to use component, both for
the application programmer and the script writer.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	A library that allow applications to extend through external scripts

%description -n %{libname}
The AngelCode Scripting Library, or AngelScript as it is also known, is an
extremely flexible cross-platform scripting library designed to allow
applications to extend their functionality through external scripts. It has
been designed from the beginning to be an easy to use component, both for
the application programmer and the script writer.

%files -n %{libname}
%{_libdir}/lib%{name}.so.*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	 Development files for %{name}
Group:		 Development/C++
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Headers and development files for %{name}.

%files -n %{devname}
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%doc docs/

#----------------------------------------------------------------------------

%prep
%setup -q -n sdk

%build
pushd angelscript/projects/cmake/
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DBUILD_STATIC_LIBS:BOOL=OFF
%make
popd

%install
# lib
install -dm 0755 %{buildroot}%{_libdir}/
install -pm 0644 %{name}/lib/lib%{name}.so.%{major}.%{minor}.%{micro} %{buildroot}%{_libdir}/
pushd %{buildroot}%{_libdir}/
 	ln -s lib%{name}.so.%{major}.%{minor}.%{micro} lib%{name}.so
	ln -s lib%{name}.so.%{major}.%{minor}.%{micro} lib%{name}.so.%{major}
	ln -s lib%{name}.so.%{major}.%{minor}.%{micro} lib%{name}.so.%{major}.%{minor}
popd

# header file
install -dm 0755 %{buildroot}%{_includedir}/
install -pm 0644 %{name}/include/%{name}.h %{buildroot}%{_includedir}/

