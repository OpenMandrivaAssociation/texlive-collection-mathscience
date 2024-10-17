Name:		texlive-collection-mathscience
Version:	64985
Release:	2
Summary:	Mathematics, natural sciences, computer science packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/collection-mathscience
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-mathscience.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
