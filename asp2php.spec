Summary:	Converts WWW Active Server (Windoze IIS) Pages to PHP pages
Summary(pl):	Konwertuje strony WWW Active Server (Windoze IIS) na strony PHP
Summary(ru):	Конвертирует страницы WWW Active Server (Windoze IIS) в страницы на PHP
Summary(uk):	Конверту╓ стор╕нки WWW Active Server (Windoze IIS) у стор╕нки на PHP
%define doc_dir /usr/share/doc/%{name}-%{version}
Name:		asp2php
Version:	0.75.25
Release:	1
License:	GPL
Group:		Development/Tools
Group(cs):	VЩvojovИ prostЬedky/NАstroje
Group(da):	Udvikling/VФrktЬj
Group(de):	Entwicklung/Tools
Group(es):	Desarrollo/Herramientas
Group(fr):	Development/Outils
Group(is):	чrСunartСl/TСl
Group(it):	Sviluppo/Tool
Group(ja):	Ё╚х╞/╔д║╪╔К
Group(no):	Utvikling/VerktЬy
Group(pl):	Programowanie/NarzЙdzia
Group(pt):	Desenvolvimento/Ferramentas
Group(ru):	Разработка/Инструменты
Group(sl):	Razvoj/Orodja
Group(sv):	Utveckling/Verktyg
Group(uk):	Розробка/╤нструменти
Source0:	http://home.swbell.net/mikekohn/%{name}/%{name}-%{version}.tar.gz
URL:		http://asp2php.naken.cc/
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
asp2php converts WWW Active Server Pages (ASP) files that run on the
Microsoft IIS Web Server into PHP pages to run on Apache.

%description -l pl
asp2php konwertuje pliki stron WWW Active Server (ASP) dziaЁaj╠cego w
ramach Microsoft IIS Web Server na strony PHP dziaЁaj╠ce na Apache.

%description -l ru
asp2php конвертирует файлы WWW Active Server Pages (ASP), исполняемые
на Micro$oft IIS Web Server, в web-страницы на PHP для работы с
Apache.

%description -l uk
asp2php конверту╓ файли WWW Active Server Pages (ASP), виконуван╕ на
Micro$oft IIS Web Server, у web-стор╕нки на PHP для роботи з Apache.

%package gtk
Summary:	gtk+ frontend for asp2php
Summary(pl):	NakЁadka gtk+ na asp2php
Summary(ru):	Оболочка на gtk+ для asp2php
Summary(uk):	Оболонка на gtk+ для asp2php
Group:		Development/Tools
Group(cs):	VЩvojovИ prostЬedky/NАstroje
Group(da):	Udvikling/VФrktЬj
Group(de):	Entwicklung/Tools
Group(es):	Desarrollo/Herramientas
Group(fr):	Development/Outils
Group(is):	чrСunartСl/TСl
Group(it):	Sviluppo/Tool
Group(ja):	Ё╚х╞/╔д║╪╔К
Group(no):	Utvikling/VerktЬy
Group(pl):	Programowanie/NarzЙdzia
Group(pt):	Desenvolvimento/Ferramentas
Group(ru):	Разработка/Инструменты
Group(sl):	Razvoj/Orodja
Group(sv):	Utveckling/Verktyg
Group(uk):	Розробка/╤нструменти
Requires:	%{name} = %{version}

%description gtk
gtk+ frontend to asp2php.

%description gtk -l pl
NakЁadka gtk+ na asp2php.

%description gtk -l ru
Оболочка на gtk+ для asp2php.

%description gtk -l uk
Оболонка на gtk+ для asp2php.

%prep
%setup -q -n %{name}
perl -pi -e "s/gcc/gcc %{optflags}/g" Makefile

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
