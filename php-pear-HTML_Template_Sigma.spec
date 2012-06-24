%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Template
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_Sigma

Summary:	%{_pearname} - Integrated Templates API implemetation with template 'compilation'
Summary(pl):	%{_pearname} - Implementacja API Integrated Templates z "kompilacj�" szablon�w
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	df53f3e8c40cd9540ede83ce021dbe93
URL:		http://pear.php.net/package/HTML_Template_Sigma/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'pear())'

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
HTML_Template_Sigma jest implementacj� API Integrated Templates
zaprojektowanego przez Ulfa Wendla.

Mo�liwo�ci:
- zagnie�d�one bloki, kontrolowane przez silnik
- mo�liwo�� do��czania plik�w z szablonu: <!-- INCLUDE -->
- automatyczne usuwanie pustych blok�w i nieznanych zmiennych
  (dost�pne s� metody do r�cznego obej�cia tego)
- metody do dodawania i podmieniania blok�w z szablon�w w czasie pracy
- mo�liwo�� wstawiania do szablon�w wywo�a� prostych funkcji:
  func_uppercase('Hello world!') oraz definiowanie do tego funkcji
  callback
- "kompilowane" szablony: Silnik musi przeanalizowa� plik szablonu
  przy u�yciu wyra�e� regularnych, aby znale�� wszystkie bloki i
  zmienne; jest to "droga" operacja i nie jest konieczne wykonywanie
  jej przy ka�dym ��daniu strony - szablony rzadko zmieniaj� si� na
  stronach produkcyjnych. St�d ta mo�liwo��: wewn�trzna reprezentacja
  struktury szablonu jest zapisywana do pliku i ten plik jest
  wczytywany zamiast �r�d�owego przy nast�pnych ��daniach (o ile nie
  zmieni�o si� �r�d�o)
- testy oparte na PHPUnit do definiowania prawid�owego zachowania
- dost�pne przyk�ady u�ycia do wi�kszo�ci mo�liwo�ci, wystarczy
  zajrze� do katalogu docs/.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs
%doc %{_pearname}-%{version}/tests
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
