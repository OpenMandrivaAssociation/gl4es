%define git 20231009

Name:           gl4es
Version:        1.1.4.%{git}
Release:        1
Summary:        OpenGL for GLES Hardware
License:        MIT
URL:            https://github.com/ptitSeb/gl4es/
Source:         https://github.com/ptitSeb/gl4es/archive/refs/heads/gl4es-master.tar.gz

BuildRequires: cmake
BuildRequires: coreutils
BuildRequires: ccache
BuildRequires: pkgconfig(x11)


%description
This is a library provide OpenGL 2.x functionality for GLES2.0 accelerated Hardware (and of course also support OpenGL 1.5 function, sometimes better than when using GLES 1.1 backend).
There is also support for GLES 1.1 Hardware, emulating OpenGL 1.5, and some OpenGL 2.x+ extensions.
GL4ES is known to work on many platform: OpenPandora, ODroid, RaspberryPI (2 and 3 at least), PocketCHIP, "otherfruit"PI (like the OrangePI), Android, iOS, x86 and x86_64 Linux (tested using mesa-egl). 
There is also some WIP support for AmigaOS4, using experimental GLES2 driver for Warp3D.
This library is based on glshim (https://github.com/lunixbochs/glshim) but as now evolved far from it, with different feature set and objectives. 
Go check this lib if you need things like RemoteGL or TinyGLES (for software rendering).

%prep
%autosetup -n gl4es-master -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
