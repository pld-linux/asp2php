Summary:	An ASP to PHP converter
Summary(cs):	Konvertor z ASP do PHP
Summary(da):	ASP til PHP konvertering
Summary(de):	Ein Konverter für die Umwandlung von ASP in PHP
Summary(es):	Convertidor de ASP en PHP
Summary(fr):	Convertisseur ASP-PHP
Summary(id):	Konverter ASP ke PHP
Summary(it):	Convertitore di ASP in PHP
Summary(ja):	ASP ¤«¤é PHP ¤Ø¤Î¥³¥ó¥Ğ¡¼¥¿
Summary(no):	Konverterer ASP til PHP
Summary(pl):	Konwerter ASP do PHP
Summary(pt):	Um conversor de ASP para PHP
Summary(ru):	ğÒÅÏÂÒÁÚÏ×ÁÔÅÌØ ĞÒÏÇÒÁÍÍ ASP × PHP
Summary(sl):	Pretvornik iz ASP v PHP
Summary(sv):	En konverterare från ASP till PHP
Summary(uk):	ëÏÎ×ÅÒÔÕ¤ ÓÔÏÒ¦ÎËÉ WWW Active Server (Windoze IIS) Õ ÓÔÏÒ¦ÎËÉ ÎÁ PHP
Name:		asp2php
Version:	0.75.25
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://home.swbell.net/mikekohn/%{name}/%{name}-%{version}.tar.gz
URL:		http://asp2php.naken.cc/
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define doc_dir	/usr/share/doc/%{name}-%{version}

%description
asp2php converts WWW Active Server Pages (ASP) files that run on the
Microsoft IIS Web Server into PHP pages to run on Apache.

%description -l cs
Balíèek obsahuje nástroj, kterı konvertuje ASP (Active Server Pages)
soubory (které je mo¾né spustit na Microsoft IIS Web serveru) do PHP
stránek, které je mo¾né spustit na Apache Web serveru.

%description -l da
asp2php-værktøjet konverterer \"Active Server Pages\" (ASP) filer, som
kører på Microsoft IIS webtjener, til PHP, som kører på webtjeneren
Apache.

%description -l de
Das asp2php Dienstprogramm wandelt Active Server Pages (ASP) Dateien,
die auf dem Microsoft IIS Web Server ausgelegt sind, in PHP Seiten um,
die mit Apache laufen.

%description -l es
La utilidad asp2php convierte los ficheros Active Server Pages (ASP),
que se ejecutan en el servidor web Microsoft IIS, en páginas PHP, que
se ejecutan en el servidor web Apache.

%description -l fr
L'utilitaire asp2php convertit les fichiers ASP (Active Server Pages)
fonctionnant sur le serveur Web Microsoft IIS en pages PHP
fonctionnant sur le serveur Web Apache.

%description -l it
L'utility asp2php converte i file ASP (Active Server Pages), che sono
in esecuzione sul web server Microsoft IIS, in pagine PHP, eseguite
sul web server Apache.

%description -l ja
asp2php ¥æ¡¼¥Æ¥£¥ê¥Æ¥£¤Ï¡¢Microsoft IIS Web Server ¾å¤ÇÆ°ºî¤¹¤ë ASP
(Active Server Pages) ¥Õ¥¡¥¤¥ë¤ò¡¢Apache ¾å¤ÇÆ°ºî¤¹¤ë PHP ¥Ú¡¼¥¸¤Ë
ÊÑ´¹¤·¤Ş¤¹¡£

%description -l no
Et verktøy for å konvertere \"Active Server Pages\" (ASP) som kjører
på Microsoft IIS webtjener til PHP, som kjører på webtjeneren Apache.

%description -l pl
asp2php konwertuje pliki stron WWW Active Server (ASP) dzia³aj±cego w
ramach Microsoft IIS Web Server na strony PHP dzia³aj±ce na Apache.

%description -l pt
O utilitário asp2php converte os ficheiros de WWW Active Server Pages
(ASP), que correm no servidor Web IIS da Microsoft, em páginas de PHP
que correm no servidor Web Apache.

%description -l ru
asp2php ËÏÎ×ÅÒÔÉÒÕÅÔ ÆÁÊÌÙ WWW Active Server Pages (ASP), ÉÓĞÏÌÎÑÅÍÙÅ
ÎÁ Micro$oft IIS Web Server, × web-ÓÔÒÁÎÉÃÙ ÎÁ PHP ÄÌÑ ÒÁÂÏÔÙ Ó
Apache.

%description -l sv
Verktyget asp2php konverterar filer med Active Server Pages (ASP), som
används i Microsofts webbserver IIS, till PHP-sidor, som körs i
webbservern Apache.

%description -l uk
asp2php ËÏÎ×ÅÒÔÕ¤ ÆÁÊÌÉ WWW Active Server Pages (ASP), ×ÉËÏÎÕ×ÁÎ¦ ÎÁ
Micro$oft IIS Web Server, Õ web-ÓÔÏÒ¦ÎËÉ ÎÁ PHP ÄÌÑ ÒÏÂÏÔÉ Ú Apache.

%package gtk
Summary:	GTK+ frontend for asp2php
Summary(cs):	Grafické rozhraní pro asp2php konvertor v Gtk verzi
Summary(da):	En GTK+ grafisk grænseflade for asp2php
Summary(de):	Ein GUI GTK+ Frontend für  asp2php
Summary(es):	Interfaz GTK+ para asp2php
Summary(fr):	Frontal GTK pour le convertisseur asp2php
Summary(id):	GTK+ front-end untuk asp2php
Summary(it):	Front-end GTK per asp2php
Summary(ja):	asp2php ¥³¥ó¥Ğ¡¼¥¿¤Î GTK+ ¥Õ¥í¥ó¥È¥¨¥ó¥É
Summary(no):	Et grafisk grensesnitt for asp2php
Summary(pl):	Nak³adka GTK+ na asp2php
Summary(pt):	Uma interface de GTK+ para o asp2php
Summary(ru):	éÎÔÅÒÆÅÊÓ ÄÌÑ asp2php ĞÏÄ gtk+
Summary(sl):	Vmesnik GTK+ za asp2php
Summary(sv):	En GTK+-framända till asp2php
Summary(uk):	ïÂÏÌÏÎËÁ ÎÁ gtk+ ÄÌÑ asp2php
Group:		Development/Tools
Requires:	%{name} = %{version}

%description gtk
gtk+ frontend to asp2php.

%description gtk -l cs
Balíèek obsahuje grafické rozhraní pro asp2php konvertor v Gtk verzi.

%description gtk -l da
Denne pakke indeholder en grafisk grænseflade i GTK+ for
asp2php-konverteringsprogrammet.

%description gtk -l de
Dieses Paket enthält ein GUI GTK+ Interface für den asp2php
Dateiformat-Konverter.

%description gtk -l es
Este paquete contiene una interfaz GUI GTK+ para el convertidor de
formato de fichero asp2php.

%description gtk -l fr
Ce paquetage contient une IUG GTK+ pour le convertisseur de fichiers
asp2php.

%description gtk -l it
Questo pacchetto contiene un'interfaccia GUI GTK+ per il convertitore
di formato asp2php.

%description gtk -l ja
¤³¤Î¥Ñ¥Ã¥±¡¼¥¸¤Ë¤Ï asp2php ¥Õ¥¡¥¤¥ë¥Õ¥©¡¼¥Ş¥Ã¥È¥³¥ó¥Ğ¡¼¥¿ÍÑ¤Î GTK+ GUI
¥¤¥ó¥¿¡¼¥Õ¥§¥¤¥¹¤¬´Ş¤Ş¤ì¤Æ¤¤¤Ş¤¹¡£

%description gtk -l no
Denne pakken inneholder et grafisk grensesnitt for
asp2php-konverteringsprogrammet.

%description gtk -l pl
Nak³adka gtk+ na asp2php.

%description gtk -l pt
Este pacote contém uma interface gráfica de GTK+ para o conversor de
formato de ficheiros asp2php.

%description gtk -l ru
üÔÏÔ ĞÁËÅÔ ÓÏÄÅÒÖÉÔ ÉÎÔÅÒÆÅÊÓ ÎÁ GTK+, ÄÌÑ ĞÒÅÏÂÒÁÚÏ×ÁÔÅÌÑ asp2php

%description gtk -l sl
Ta paket vsebuje grafièni vmesnik za GTK+ za pretvornik datoteènih
formatov asp2php.

%description gtk -l sv
Detta paket innehåller ett grafiskt GTK+-gränssnitt till
filformatkonverteraren asp2php.

%description gtk -l uk
ïÂÏÌÏÎËÁ ÎÁ gtk+ ÄÌÑ asp2php.

%prep
%setup -q -n %{name}
perl -pi -e "s/gcc/gcc %{rpmcflags}/g" Makefile

%build
%{__make}
%{__make} gtkasp2php

%install
rm -rf $RPM_BUILD_ROOT
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
cp -f asp2php gtkasp2php %{buildroot}%{_bindir}

# Install documentation by hand
install -d %{buildroot}%{doc_dir}
cp -p README LICENSE %{buildroot}%{doc_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{doc_dir}
%attr(755,root,root) %{_bindir}/asp2php

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtkasp2php
