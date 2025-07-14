# TODO: plugins, bindings?
Summary:	ASAP - Another Slight Atari Player
Summary(pl.UTF-8):	ASAP (Another Slight Atari Player) - jeszcze jeden odtwarzacz plików z Atari
Name:		asap
Version:	3.1.3
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/asap/%{name}-%{version}.tar.gz
# Source0-md5:	ce136b58933a67154e43902fcf239d58
Patch0:		%{name}-make.patch
URL:		http://asap.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ASAP is a player of Atari 8-bit music for modern computers and mobile
devices. It emulates the POKEY sound chip and the 6502 processor.

ASAP supports the following file formats: SAP, CMC, CM3, CMR, CMS,
DMC, DLT, MPT, MPD, RMT, TMC, TM8, TM2, FC.

The main package contains ASAP shared library and converter.

%description -l pl.UTF-8
ASAP to odtwarzacz muzyki z 8-bitowego Atari dla współczesnych
komputerów i urządzeń przenośnych. Emuluje układ dźwiękowy POKEY i
procesor 6502.

ASAP obsługuje następujące formaty plików: SAP, CMC, CM3, CMR, CMS,
DMC, DLT, MPT, MPD, RMT, TMC, TM8, TM2, FC.

Główny pakiet zawiera bibliotekę współdzieloną i konwerter.

%package devel
Summary:	Header file for ASAP library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki ASAP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for ASAP library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki ASAP.

%package static
Summary:	Static ASAP library
Summary(pl.UTF-8):	Statyczna biblioteka ASAP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ASAP library.

%description static -l pl.UTF-8
Statyczna biblioteka ASAP.

%package sdl
Summary:	SDL-based ASAP player
Summary(pl.UTF-8):	Odtwarzacz ASAP oparty na SDL
Group:		Applications/Sound

%description sdl
SDL-based ASAP player.

%description sdl -l pl.UTF-8
Odtwarzacz ASAP oparty na SDL.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} asapconv lib asap-sdl \
	V=1 \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install-asapconv install-lib install-sdl \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	libdir=%{_libdir}

# no dependencies
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libasap.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS NEWS README.html USAGE-WEB sap-format.txt
%attr(755,root,root) %{_bindir}/asapconv
%attr(755,root,root) %{_libdir}/libasap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libasap.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libasap.so
%{_includedir}/asap.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libasap.a

%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/asap-sdl
