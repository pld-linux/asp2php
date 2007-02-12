Summary:	An ASP to PHP converter
Summary(cs.UTF-8):   Konvertor z ASP do PHP
Summary(da.UTF-8):   ASP til PHP konvertering
Summary(de.UTF-8):   Ein Konverter für die Umwandlung von ASP in PHP
Summary(es.UTF-8):   Convertidor de ASP en PHP
Summary(fr.UTF-8):   Convertisseur ASP-PHP
Summary(id.UTF-8):   Konverter ASP ke PHP
Summary(it.UTF-8):   Convertitore di ASP in PHP
Summary(ja.UTF-8):   ASP から PHP へのコンバータ
Summary(nb.UTF-8):   Konverterer ASP til PHP
Summary(pl.UTF-8):   Konwerter ASP do PHP
Summary(pt.UTF-8):   Um conversor de ASP para PHP
Summary(ru.UTF-8):   Преобразователь программ ASP в PHP
Summary(sl.UTF-8):   Pretvornik iz ASP v PHP
Summary(sv.UTF-8):   En konverterare från ASP till PHP
Summary(uk.UTF-8):   Конвертує сторінки WWW Active Server (Windoze IIS) у сторінки на PHP
Name:		asp2php
Version:	0.76.18
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://www.mikekohn.com/asp2php/%{name}-%{version}.tar.gz
# Source0-md5:	dd3c21e7d305b978ca49bee73e0e44f3
URL:		http://asp2php.naken.cc/
BuildRequires:	gtk+-devel
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
asp2php converts WWW Active Server Pages (ASP) files that run on the
Microsoft IIS Web Server into PHP pages to run on Apache.

%description -l cs.UTF-8
Balíček obsahuje nástroj, který konvertuje ASP (Active Server Pages)
soubory (které je možné spustit na Microsoft IIS Web serveru) do PHP
stránek, které je možné spustit na Apache Web serveru.

%description -l da.UTF-8
asp2php-værktøjet konverterer \"Active Server Pages\" (ASP) filer, som
kører på Microsoft IIS webtjener, til PHP, som kører på webtjeneren
Apache.

%description -l de.UTF-8
Das asp2php Dienstprogramm wandelt Active Server Pages (ASP) Dateien,
die auf dem Microsoft IIS Web Server ausgelegt sind, in PHP Seiten um,
die mit Apache laufen.

%description -l es.UTF-8
La utilidad asp2php convierte los ficheros Active Server Pages (ASP),
que se ejecutan en el servidor web Microsoft IIS, en páginas PHP, que
se ejecutan en el servidor web Apache.

%description -l fr.UTF-8
L'utilitaire asp2php convertit les fichiers ASP (Active Server Pages)
fonctionnant sur le serveur Web Microsoft IIS en pages PHP
fonctionnant sur le serveur Web Apache.

%description -l it.UTF-8
L'utility asp2php converte i file ASP (Active Server Pages), che sono
in esecuzione sul web server Microsoft IIS, in pagine PHP, eseguite
sul web server Apache.

%description -l ja.UTF-8
asp2php ユーティリティは、Microsoft IIS Web Server 上で動作する ASP
(Active Server Pages) ファイルを、Apache 上で動作する PHP ページに
変換します。

%description -l nb.UTF-8
Et verktøy for å konvertere \"Active Server Pages\" (ASP) som kjører
på Microsoft IIS webtjener til PHP, som kjører på webtjeneren Apache.

%description -l pl.UTF-8
asp2php konwertuje pliki stron WWW Active Server (ASP) działającego w
ramach Microsoft IIS Web Server na strony PHP działające na Apache.

%description -l pt.UTF-8
O utilitário asp2php converte os ficheiros de WWW Active Server Pages
(ASP), que correm no servidor Web IIS da Microsoft, em páginas de PHP
que correm no servidor Web Apache.

%description -l ru.UTF-8
asp2php конвертирует файлы WWW Active Server Pages (ASP), исполняемые
на Micro$oft IIS Web Server, в web-страницы на PHP для работы с
Apache.

%description -l sv.UTF-8
Verktyget asp2php konverterar filer med Active Server Pages (ASP), som
används i Microsofts webbserver IIS, till PHP-sidor, som körs i
webbservern Apache.

%description -l uk.UTF-8
asp2php конвертує файли WWW Active Server Pages (ASP), виконувані на
Micro$oft IIS Web Server, у web-сторінки на PHP для роботи з Apache.

%package gtk
Summary:	GTK+ frontend for asp2php
Summary(cs.UTF-8):   Grafické rozhraní pro asp2php konvertor v GTK+ verzi
Summary(da.UTF-8):   En GTK+ grafisk grænseflade for asp2php
Summary(de.UTF-8):   Ein GUI GTK+ Frontend für  asp2php
Summary(es.UTF-8):   Interfaz GTK+ para asp2php
Summary(fr.UTF-8):   Frontal GTK+ pour le convertisseur asp2php
Summary(id.UTF-8):   GTK+ front-end untuk asp2php
Summary(it.UTF-8):   Front-end GTK+ per asp2php
Summary(ja.UTF-8):   asp2php コンバータの GTK+ フロントエンド
Summary(nb.UTF-8):   Et grafisk grensesnitt for asp2php
Summary(pl.UTF-8):   Nakładka GTK+ na asp2php
Summary(pt.UTF-8):   Uma interface de GTK+ para o asp2php
Summary(ru.UTF-8):   Интерфейс для asp2php под GTK+
Summary(sl.UTF-8):   Vmesnik GTK+ za asp2php
Summary(sv.UTF-8):   En GTK+-framända till asp2php
Summary(uk.UTF-8):   Оболонка на GTK+ для asp2php
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description gtk
GTK+ frontend to asp2php.

%description gtk -l cs.UTF-8
Balíček obsahuje grafické rozhraní pro asp2php konvertor v GTK+ verzi.

%description gtk -l da.UTF-8
Denne pakke indeholder en grafisk grænseflade i GTK+ for
asp2php-konverteringsprogrammet.

%description gtk -l de.UTF-8
Dieses Paket enthält ein GUI GTK+ Interface für den asp2php
Dateiformat-Konverter.

%description gtk -l es.UTF-8
Este paquete contiene una interfaz GUI GTK+ para el convertidor de
formato de fichero asp2php.

%description gtk -l fr.UTF-8
Ce paquetage contient une IUG GTK+ pour le convertisseur de fichiers
asp2php.

%description gtk -l it.UTF-8
Questo pacchetto contiene un'interfaccia GUI GTK+ per il convertitore
di formato asp2php.

%description gtk -l ja.UTF-8
このパッケージには asp2php ファイルフォーマットコンバータ用の GTK+ GUI
インターフェイスが含まれています。

%description gtk -l nb.UTF-8
Denne pakken inneholder et grafisk grensesnitt for
asp2php-konverteringsprogrammet.

%description gtk -l pl.UTF-8
Nakładka GTK+ na asp2php.

%description gtk -l pt.UTF-8
Este pacote contém uma interface gráfica de GTK+ para o conversor de
formato de ficheiros asp2php.

%description gtk -l ru.UTF-8
Этот пакет содержит интерфейс на GTK+, для преобразователя asp2php

%description gtk -l sl.UTF-8
Ta paket vsebuje grafični vmesnik za GTK+ za pretvornik datotečnih
formatov asp2php.

%description gtk -l sv.UTF-8
Detta paket innehåller ett grafiskt GTK+-gränssnitt till
filformatkonverteraren asp2php.

%description gtk -l uk.UTF-8
Оболонка на GTK+ для asp2php.

%prep
%setup -q
%{__perl} -pi -e "s/gcc/%{__cc} %{rpmcflags}/g" Makefile */Makefile */*/Makefile

%build
%{__make}
%{__make} gui

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install asp2php gtkasp2php $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE
%attr(755,root,root) %{_bindir}/asp2php

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtkasp2php
