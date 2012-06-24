Summary:	Converts WWW Active Server (Windoze IIS) Pages to PHP pages
Summary(pl):	Konwertuje strony WWW Active Server (Windoze IIS) na strony PHP
Summary(ru):	������������ �������� WWW Active Server (Windoze IIS) � �������� �� PHP
Summary(uk):	�������դ ���Ҧ��� WWW Active Server (Windoze IIS) � ���Ҧ��� �� PHP
%define doc_dir /usr/share/doc/%{name}-%{version}
Name:		asp2php
Version:	0.75.25
Release:	1
License:	GPL
Group:		Development/Tools
Group(cs):	V�vojov� prost�edky/N�stroje
Group(da):	Udvikling/V�rkt�j
Group(de):	Entwicklung/Tools
Group(es):	Desarrollo/Herramientas
Group(fr):	Development/Outils
Group(is):	�r�unart�l/T�l
Group(it):	Sviluppo/Tool
Group(ja):	��ȯ/�ġ���
Group(no):	Utvikling/Verkt�y
Group(pl):	Programowanie/Narz�dzia
Group(pt):	Desenvolvimento/Ferramentas
Group(ru):	����������/�����������
Group(sl):	Razvoj/Orodja
Group(sv):	Utveckling/Verktyg
Group(uk):	��������/�����������
Source0:	http://home.swbell.net/mikekohn/%{name}/%{name}-%{version}.tar.gz
URL:		http://asp2php.naken.cc/
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
asp2php converts WWW Active Server Pages (ASP) files that run on the
Microsoft IIS Web Server into PHP pages to run on Apache.

%description -l pl
asp2php konwertuje pliki stron WWW Active Server (ASP) dzia�aj�cego w
ramach Microsoft IIS Web Server na strony PHP dzia�aj�ce na Apache.

%description -l ru
asp2php ������������ ����� WWW Active Server Pages (ASP), �����������
�� Micro$oft IIS Web Server, � web-�������� �� PHP ��� ������ �
Apache.

%description -l uk
asp2php �������դ ����� WWW Active Server Pages (ASP), ��������Φ ��
Micro$oft IIS Web Server, � web-���Ҧ��� �� PHP ��� ������ � Apache.

%package gtk
Summary:	gtk+ frontend for asp2php
Summary(pl):	Nak�adka gtk+ na asp2php
Summary(ru):	�������� �� gtk+ ��� asp2php
Summary(uk):	�������� �� gtk+ ��� asp2php
Group:		Development/Tools
Group(cs):	V�vojov� prost�edky/N�stroje
Group(da):	Udvikling/V�rkt�j
Group(de):	Entwicklung/Tools
Group(es):	Desarrollo/Herramientas
Group(fr):	Development/Outils
Group(is):	�r�unart�l/T�l
Group(it):	Sviluppo/Tool
Group(ja):	��ȯ/�ġ���
Group(no):	Utvikling/Verkt�y
Group(pl):	Programowanie/Narz�dzia
Group(pt):	Desenvolvimento/Ferramentas
Group(ru):	����������/�����������
Group(sl):	Razvoj/Orodja
Group(sv):	Utveckling/Verktyg
Group(uk):	��������/�����������
Requires:	%{name} = %{version}

%description gtk
gtk+ frontend to asp2php.

%description gtk -l pl
Nak�adka gtk+ na asp2php.

%description gtk -l ru
�������� �� gtk+ ��� asp2php.

%description gtk -l uk
�������� �� gtk+ ��� asp2php.

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
