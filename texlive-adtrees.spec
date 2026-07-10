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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a means to write adpositional trees, a formalism
devoted to representing natural language expressions. The package relies
on epic and cancel.

