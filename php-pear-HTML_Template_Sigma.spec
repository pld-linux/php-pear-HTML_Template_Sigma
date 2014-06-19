%define		_class		HTML
%define		_subclass	Template
%define		_status		stable
%define		_pearname	HTML_Template_Sigma
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - Integrated Templates API implemetation with template 'compilation'
Summary(pl.UTF-8):	%{_pearname} - Implementacja API Integrated Templates z "kompilacją" szablonów
Name:		php-pear-%{_pearname}
Version:	1.3.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d1c7614c181ffc708c922d6600207b4c
URL:		http://pear.php.net/package/HTML_Template_Sigma/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(ctype)
Requires:	php-pear
Obsoletes:	php-pear-HTML_Template_Sigma-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# included in tests
%define		_noautoreq pear(Sigma_api_testcase.php)

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

%description -l pl.UTF-8
HTML_Template_Sigma jest implementacją API Integrated Templates
zaprojektowanego przez Ulfa Wendla.

Możliwości:
- zagnieżdżone bloki, kontrolowane przez silnik
- możliwość dołączania plików z szablonu: <!-- INCLUDE -->
- automatyczne usuwanie pustych bloków i nieznanych zmiennych
  (dostępne są metody do ręcznego obejścia tego)
- metody do dodawania i podmieniania bloków z szablonów w czasie pracy
- możliwość wstawiania do szablonów wywołań prostych funkcji:
  func_uppercase('Hello world!') oraz definiowanie do tego funkcji
  callback
- "kompilowane" szablony: Silnik musi przeanalizować plik szablonu
  przy użyciu wyrażeń regularnych, aby znaleźć wszystkie bloki i
  zmienne; jest to "droga" operacja i nie jest konieczne wykonywanie jej
  przy każdym żądaniu strony - szablony rzadko zmieniają się na stronach
  produkcyjnych. Stąd ta możliwość: wewnętrzna reprezentacja struktury
  szablonu jest zapisywana do pliku i ten plik jest wczytywany zamiast
  źródłowego przy następnych żądaniach (o ile nie zmieniło się źródło)
- testy oparte na PHPUnit do definiowania prawidłowego zachowania
- dostępne przykłady użycia do większości możliwości, wystarczy
  zajrzeć do katalogu docs/.

Ta klasa ma w PEAR status: %{_status}.

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
%{php_pear_dir}/HTML/Template/*.php
