Name:           ros-indigo-pepper-bringup
Version:        0.1.3
Release:        0%{?dist}
Summary:        ROS pepper_bringup package

Group:          Development/Libraries
License:        Apache 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-naoqi-driver
Requires:       ros-indigo-pepper-description
Requires:       ros-indigo-pepper-sensors
BuildRequires:  ros-indigo-catkin

%description
The pepper_bringup package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Jun 25 2015 Karsten Knese <kknese@aldebaran.com> - 0.1.3-0
- Autogenerated by Bloom

* Fri Apr 10 2015 Karsten Knese <kknese@aldebaran.com> - 0.1.2-0
- Autogenerated by Bloom

* Wed Apr 08 2015 Karsten Knese <kknese@aldebaran.com> - 0.1.1-0
- Autogenerated by Bloom

