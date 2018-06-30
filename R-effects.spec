#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-effects
Version  : 4.0.2
Release  : 1
URL      : https://cran.r-project.org/src/contrib/effects_4.0-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/effects_4.0-2.tar.gz
Summary  : Effect Displays for Linear, Generalized Linear, and Other Models
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-carData
Requires: R-colorspace
Requires: R-estimability
Requires: R-formatR
Requires: R-lme4
Requires: R-ordinal
Requires: R-survey
BuildRequires : R-carData
BuildRequires : R-colorspace
BuildRequires : R-estimability
BuildRequires : R-formatR
BuildRequires : R-lme4
BuildRequires : R-ordinal
BuildRequires : R-survey
BuildRequires : clr-R-helpers
BuildRequires : texlive

%description
Graphical and tabular effect displays, e.g., of interactions, for 
  various statistical models with linear predictors.

%prep
%setup -q -c -n effects

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530332875

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530332875
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library effects
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library effects
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library effects
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library effects|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/effects/CHANGES
/usr/lib64/R/library/effects/CITATION
/usr/lib64/R/library/effects/DESCRIPTION
/usr/lib64/R/library/effects/INDEX
/usr/lib64/R/library/effects/Meta/Rd.rds
/usr/lib64/R/library/effects/Meta/features.rds
/usr/lib64/R/library/effects/Meta/hsearch.rds
/usr/lib64/R/library/effects/Meta/links.rds
/usr/lib64/R/library/effects/Meta/nsInfo.rds
/usr/lib64/R/library/effects/Meta/package.rds
/usr/lib64/R/library/effects/Meta/vignette.rds
/usr/lib64/R/library/effects/NAMESPACE
/usr/lib64/R/library/effects/NEWS
/usr/lib64/R/library/effects/R/effects
/usr/lib64/R/library/effects/R/effects.rdb
/usr/lib64/R/library/effects/R/effects.rdx
/usr/lib64/R/library/effects/doc/effectsMethods.R
/usr/lib64/R/library/effects/doc/effectsMethods.Rnw
/usr/lib64/R/library/effects/doc/effectsMethods.pdf
/usr/lib64/R/library/effects/doc/index.html
/usr/lib64/R/library/effects/doc/partial-residuals.R
/usr/lib64/R/library/effects/doc/partial-residuals.Rnw
/usr/lib64/R/library/effects/doc/partial-residuals.pdf
/usr/lib64/R/library/effects/help/AnIndex
/usr/lib64/R/library/effects/help/aliases.rds
/usr/lib64/R/library/effects/help/effects.rdb
/usr/lib64/R/library/effects/help/effects.rdx
/usr/lib64/R/library/effects/help/paths.rds
/usr/lib64/R/library/effects/html/00Index.html
/usr/lib64/R/library/effects/html/R.css
