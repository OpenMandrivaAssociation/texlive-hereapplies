%global tl_name hereapplies
%global tl_revision 68638

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.2
Release:	%{tl_revision}.1
Summary:	A LaTeX package for referencing groups of pages that share something in common
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hereapplies
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hereapplies.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hereapplies.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Here Applies is a LaTeX package that allows to collect groups of labels
and reference them altogether. It can be used for creating informal
glossaries that cross-link concepts to their applications, or simply
mentioning multiple pages that share something in common.

