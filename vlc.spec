Name: vlc
Version: 0.2.71
Release: 1
Copyright: GPL
Url: http://www.videolan.org/
Group: X11/Applications/Graphics
Source0: http://www.videolan.org/packages/0.2.71/vlc-0.2.71.tar.gz
Packager: Samuel Hocevar <sam@zoy.org>

Buildroot: /tmp/vlc-build
Summary: VideoLAN Client.

%changelog
* Fri Apr 13 2001 Samuel Hocevar <sam@zoy.org>
New upstream release (0.2.71)

* Sun Apr 8 2001 Christophe Massiot <massiot@via.ecp.fr>
New upstream release (0.2.70)

* Fri Feb 16 2001 Samuel Hocevar <sam@via.ecp.fr>
New upstream release

* Tue Aug  8 2000 Samuel Hocevar <sam@via.ecp.fr>
Added framebuffer support

* Sun Jun 18 2000 Samuel Hocevar <sam@via.ecp.fr>
Took over the package

* Thu Jun 15 2000 Eric Doutreleau <Eric.Doutreleau@int-evry.fr>
Initial package

%description
a free network-aware MPEG and DVD player
 VideoLAN is a free MPEG1/2 software solution.
 .
 The VideoLAN Client allows to play MPEG2 Transport Streams from the
 network or from a file, as well as direct DVD playback.

%prep
%setup 

%build
./configure --prefix=/usr --with-sdl --enable-esd --enable-gnome --enable-qt
make
%install
mkdir -p $RPM_BUILD_ROOT/usr/lib
mkdir -p $RPM_BUILD_ROOT/usr/bin
make install prefix=$RPM_BUILD_ROOT/usr

%files
%attr(-, root, root) /usr/bin/vlc
%attr(-, root, root) /usr/share/videolan
%attr(-, root, root) /usr/lib/videolan
%attr(-, root, root) %doc ChangeLog AUTHORS COPYING INSTALL README TODO doc
%clean
rm -rf $RPM_BUILD_ROOT

