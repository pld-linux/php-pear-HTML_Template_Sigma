%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Template
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_Sigma

Summary:	%{_pearname} - Integrated Templates API implemetation with template 'compilation'
Summary(pl):	%{_pearname} - Implementacja API Integrated Templates z "kompilacj±" szablonów
Name:		php-pear-%{_pearname}
Version:	1.1.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5f5df2a377e444b35a1968ee8f0ff8bc
URL:		http://pear.php.net/package/HTML_Template_Sigma/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-ctype
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# included in tests
%define		_noautoreq 'pear(Sigma_api_testcase.php)'

%description
HTML_Template_Sigma implements Integrated Templates API designed by
Ulf Wendel.

Features:
- Nested blocks. Nesting is controlled by the engine.
- Ability to include files from within template: <!-- INCLUDE -->
- Automatic removal of empty blocks and unknown variables (methods to
  manually tweak/override this are also available)
- Methods for runtime addition and replacement of blocks in templates
- Ability to insert simple function calls into templates:
  func_uppercase('Hello world!') and to define callback functions for
  these
- 'Compiled' templates: the engine has to parse a template file using
  regular expressions to find all the blocks and variable placeholders.
  This is a very "expensive" operation and is an overkill to do on every
  page request: templates seldom change on production websites. Thus
  this feature: an internal representation of the template structure is
  saved into a file and this file gets loaded instead of the source one
  on subsequent requests (unless the source changes)
- PHPUnit-based tests to define correct behaviour
- Usage examples for most of the features are available, look in the
  docs/ directory

In PEAR status of this package is: %{_status}.

%description -l pl
HTML_Template_Sigma jest implementacj± API Integrated Templates
zaprojektowanego przez Ulfa Wendla.

Mo¿liwo¶ci:
- zagnie¿d¿one bloki, kontrolowane przez silnik
- mo¿liwo¶æ do³±czania plików z szablonu: <!-- INCLUDE -->
- automatyczne usuwanie pustych bloków i nieznanych zmiennych
  (dostêpne s± metody do rêcznego obej¶cia tego)
- metody do dodawania i podmieniania bloków z szablonów w czasie pracy
- mo¿liwo¶æ wstawiania do szablonów wywo³añ prostych funkcji:
  func_uppercase('Hello world!') oraz definiowanie do tego funkcji
  callback
- "kompilowane" szablony: Silnik musi przeanalizowaæ plik szablonu
  przy u¿yciu wyra¿eñ regularnych, aby znale¼æ wszystkie bloki i
  zmienne; jest to "droga" operacja i nie jest konieczne wykonywanie
  jej przy ka¿dym ¿±daniu strony - szablony rzadko zmieniaj± siê na
  stronach produkcyjnych. St±d ta mo¿liwo¶æ: wewnêtrzna reprezentacja
  struktury szablonu jest zapisywana do pliku i ten plik jest
  wczytywany zamiast ¼ród³owego przy nastêpnych ¿±daniach (o ile nie
  zmieni³o siê ¼ród³o)
- testy oparte na PHPUnit do definiowania prawid³owego zachowania
- dostêpne przyk³ady u¿ycia do wiêkszo¶ci mo¿liwo¶ci, wystarczy
  zajrzeæ do katalogu docs/.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
