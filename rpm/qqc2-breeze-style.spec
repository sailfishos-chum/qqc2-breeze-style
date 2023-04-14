%global kf5_version_min 5.98

Name:    qqc2-breeze-style
Version: 5.27.4
Release: 1%{?dist}
Summary: QtQuickControls2 breeze style

License: GPLv2+ and LGPLv2+
URL:     https://invent.kde.org/plasma/%{name}

Source0: %{name}-%{version}.tar.bz2

%{?opt_kf5_default_filter}

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: opt-extra-cmake-modules >= %{kf5_version_min}
BuildRequires: opt-kf5-rpm-macros
BuildRequires: opt-kf5-ki18n-devel >= %{kf5_version_min}
BuildRequires: opt-kf5-kirigami2-devel >= %{kf5_version_min}
Requires: opt-kf5-kirigami2%{?_isa} >= %{kf5_version_min}
BuildRequires: opt-kf5-kconfig-devel >= %{kf5_version_min}
BuildRequires: opt-kf5-kguiaddons-devel >= %{kf5_version_min}
BuildRequires: opt-kf5-kiconthemes-devel >= %{kf5_version_min}
BuildRequires: opt-kf5-kconfigwidgets-devel >= %{kf5_version_min}
BuildRequires: opt-kf5-kcoreaddons-devel >= %{kf5_version_min}
BuildRequires: opt-qt5-qtquickcontrols2-devel

BuildRequires: opt-qt5-qtbase-devel
BuildRequires: opt-qt5-qtdeclarative-devel

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: opt-qt5-qtquickcontrols2%{?_isa}
Requires: opt-qt5-qtdeclarative%{?_isa}
Requires: opt-kf5-kconfigwidgets >= %{kf5_version_min}
Requires: opt-kf5-kcoreaddons >= %{kf5_version_min}
Requires: opt-kf5-kguiaddons >= %{kf5_version_min}
Requires: opt-kf5-kiconthemes >= %{kf5_version_min}
Requires: opt-kf5-kirigami2 >= %{kf5_version_min}
Requires: opt-kf5-kconfig >= %{kf5_version_min}

%description
This is a pure Qt Quick/Kirigami Qt Quick Controls style.

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build

export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../ \

%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd


%files 
%doc README.md
%license LICENSES/*.txt
#{_opt_kf5_plugindir}/kirigami/org.kde.breeze.so
%{_opt_qt5_plugindir}/kf5/kirigami/org.kde.breeze.so
%{_opt_qt5_qmldir}/QtQuick/Controls.2/org.kde.breeze
%{_opt_qt5_qmldir}/org/kde/breeze/
%{_opt_qt5_qmldir}/org/kde/kirigami.2/styles/org.kde.breeze/
%{_opt_kf5_libdir}/cmake/KF5QQC2BreezeStyle/

