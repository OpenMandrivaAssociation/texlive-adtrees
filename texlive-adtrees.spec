Name:		texlive-adtrees
Version:	51618
Release:	2
Summary:	Macros for drawing adpositional trees
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/adtrees
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adtrees.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/adtrees.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a means to write adpositional trees, a
formalism devoted to representing natural language expressions.
The package relies on epic and cancel.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/adtrees
%doc %{_texmfdistdir}/doc/latex/adtrees

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
