Summary:	An ASP to PHP converter
Summary(cs):	Konvertor z ASP do PHP
Summary(da):	ASP til PHP konvertering
Summary(de):	Ein Konverter f�r die Umwandlung von ASP in PHP
Summary(es):	Convertidor de ASP en PHP
Summary(fr):	Convertisseur ASP-PHP
Summary(id):	Konverter ASP ke PHP
Summary(it):	Convertitore di ASP in PHP
Summary(ja):	ASP ���� PHP �ؤΥ���С���
Summary(no):	Konverterer ASP til PHP
Summary(pl):	Konwerter ASP do PHP
Summary(pt):	Um conversor de ASP para PHP
Summary(ru):	��������������� �������� ASP � PHP
Summary(sl):	Pretvornik iz ASP v PHP
Summary(sv):	En konverterare fr�n ASP till PHP
Summary(uk):	�������դ ���Ҧ��� WWW Active Server (Windoze IIS) � ���Ҧ��� �� PHP
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
Bal��ek obsahuje n�stroj, kter� konvertuje ASP (Active Server Pages)
soubory (kter� je mo�n� spustit na Microsoft IIS Web serveru) do PHP
str�nek, kter� je mo�n� spustit na Apache Web serveru.

%description -l da
asp2php-v�rkt�jet konverterer \"Active Server Pages\" (ASP) filer, som
k�rer p� Microsoft IIS webtjener, til PHP, som k�rer p� webtjeneren
Apache.

%description -l de
Das asp2php Dienstprogramm wandelt Active Server Pages (ASP) Dateien,
die auf dem Microsoft IIS Web Server ausgelegt sind, in PHP Seiten um,
die mit Apache laufen.

%description -l es
La utilidad asp2php convierte los ficheros Active Server Pages (ASP),
que se ejecutan en el servidor web Microsoft IIS, en p�ginas PHP, que
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
asp2php �桼�ƥ���ƥ��ϡ�Microsoft IIS Web Server ���ư��� ASP
(Active Server Pages) �ե������Apache ���ư��� PHP �ڡ�����
�Ѵ����ޤ���

%description -l no
Et verkt�y for � konvertere \"Active Server Pages\" (ASP) som kj�rer
p� Microsoft IIS webtjener til PHP, som kj�rer p� webtjeneren Apache.

%description -l pl
asp2php konwertuje pliki stron WWW Active Server (ASP) dzia�aj�cego w
ramach Microsoft IIS Web Server na strony PHP dzia�aj�ce na Apache.

%description -l pt
O utilit�rio asp2php converte os ficheiros de WWW Active Server Pages
(ASP), que correm no servidor Web IIS da Microsoft, em p�ginas de PHP
que correm no servidor Web Apache.

%description -l ru
asp2php ������������ ����� WWW Active Server Pages (ASP), �����������
�� Micro$oft IIS Web Server, � web-�������� �� PHP ��� ������ �
Apache.

%description -l sv
Verktyget asp2php konverterar filer med Active Server Pages (ASP), som
anv�nds i Microsofts webbserver IIS, till PHP-sidor, som k�rs i
webbservern Apache.

%description -l uk
asp2php �������դ ����� WWW Active Server Pages (ASP), ��������Φ ��
Micro$oft IIS Web Server, � web-���Ҧ��� �� PHP ��� ������ � Apache.

%package gtk
Summary:	GTK+ frontend for asp2php
Summary(cs):	Grafick� rozhran� pro asp2php konvertor v Gtk verzi
Summary(da):	En GTK+ grafisk gr�nseflade for asp2php
Summary(de):	Ein GUI GTK+ Frontend f�r  asp2php
Summary(es):	Interfaz GTK+ para asp2php
Summary(fr):	Frontal GTK pour le convertisseur asp2php
Summary(id):	GTK+ front-end untuk asp2php
Summary(it):	Front-end GTK per asp2php
Summary(ja):	asp2php ����С����� GTK+ �ե��ȥ����
Summary(no):	Et grafisk grensesnitt for asp2php
Summary(pl):	Nak�adka GTK+ na asp2php
Summary(pt):	Uma interface de GTK+ para o asp2php
Summary(ru):	��������� ��� asp2php ��� gtk+
Summary(sl):	Vmesnik GTK+ za asp2php
Summary(sv):	En GTK+-fram�nda till asp2php
Summary(uk):	�������� �� gtk+ ��� asp2php
Group:		Development/Tools
Requires:	%{name} = %{version}

%description gtk
gtk+ frontend to asp2php.

%description gtk -l cs
Bal��ek obsahuje grafick� rozhran� pro asp2php konvertor v Gtk verzi.

%description gtk -l da
Denne pakke indeholder en grafisk gr�nseflade i GTK+ for
asp2php-konverteringsprogrammet.

%description gtk -l de
Dieses Paket enth�lt ein GUI GTK+ Interface f�r den asp2php
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
���Υѥå������ˤ� asp2php �ե�����ե����ޥåȥ���С����Ѥ� GTK+ GUI
���󥿡��ե��������ޤޤ�Ƥ��ޤ���

%description gtk -l no
Denne pakken inneholder et grafisk grensesnitt for
asp2php-konverteringsprogrammet.

%description gtk -l pl
Nak�adka gtk+ na asp2php.

%description gtk -l pt
Este pacote cont�m uma interface gr�fica de GTK+ para o conversor de
formato de ficheiros asp2php.

%description gtk -l ru
���� ����� �������� ��������� �� GTK+, ��� ��������������� asp2php

%description gtk -l sl
Ta paket vsebuje grafi�ni vmesnik za GTK+ za pretvornik datote�nih
formatov asp2php.

%description gtk -l sv
Detta paket inneh�ller ett grafiskt GTK+-gr�nssnitt till
filformatkonverteraren asp2php.

%description gtk -l uk
�������� �� gtk+ ��� asp2php.

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
