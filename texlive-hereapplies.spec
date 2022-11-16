Name:		texlive-hereapplies
Version:	64391
Release:	1
Summary:	A LaTeX package for referencing groups of pages that share something in common
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hereapplies
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hereapplies.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hereapplies.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Here Applies is a LaTeX package that allows to collect groups
of labels and reference them altogether. It can be used for
creating informal glossaries that cross-link concepts to their
applications, or simply mentioning multiple pages that share
something in common.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/hereapplies
%doc %{_texmfdistdir}/doc/latex/hereapplies

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
