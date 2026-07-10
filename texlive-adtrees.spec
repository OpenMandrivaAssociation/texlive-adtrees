%global tl_name adtrees
%global tl_revision 51618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Macros for drawing adpositional trees
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/adtrees
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adtrees.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/adtrees.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a means to write adpositional trees, a formalism
devoted to representing natural language expressions. The package relies
on epic and cancel.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/adtrees
%dir %{_datadir}/texmf-dist/tex/latex/adtrees
%doc %{_datadir}/texmf-dist/doc/latex/adtrees/README
%doc %{_datadir}/texmf-dist/doc/latex/adtrees/adtreesdoc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/adtrees/adtreesdoc.tex
%{_datadir}/texmf-dist/tex/latex/adtrees/adtrees.sty
