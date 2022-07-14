#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-effects
Version  : 4.2.2
Release  : 46
URL      : https://cran.r-project.org/src/contrib/effects_4.2-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/effects_4.2-2.tar.gz
Summary  : Effect Displays for Linear, Generalized Linear, and Other Models
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-carData
Requires: R-colorspace
Requires: R-estimability
Requires: R-insight
Requires: R-lme4
Requires: R-survey
BuildRequires : R-car
BuildRequires : R-carData
BuildRequires : R-colorspace
BuildRequires : R-estimability
BuildRequires : R-insight
BuildRequires : R-lme4
BuildRequires : R-survey
BuildRequires : buildreq-R
BuildRequires : texlive

%description
Graphical and tabular effect displays, e.g., of interactions, for 
  various statistical models with linear predictors.

%prep
%setup -q -c -n effects
cd %{_builddir}/effects

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657757447

%install
export SOURCE_DATE_EPOCH=1657757447
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library effects
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library effects
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library effects
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc effects || :


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
/usr/lib64/R/library/effects/doc/effects-hex.pdf
/usr/lib64/R/library/effects/doc/functions-supported-by-effects.R
/usr/lib64/R/library/effects/doc/functions-supported-by-effects.Rnw
/usr/lib64/R/library/effects/doc/functions-supported-by-effects.pdf
/usr/lib64/R/library/effects/doc/index.html
/usr/lib64/R/library/effects/doc/partial-residuals.R
/usr/lib64/R/library/effects/doc/partial-residuals.Rnw
/usr/lib64/R/library/effects/doc/partial-residuals.pdf
/usr/lib64/R/library/effects/doc/predictor-effects-gallery.R
/usr/lib64/R/library/effects/doc/predictor-effects-gallery.Rnw
/usr/lib64/R/library/effects/doc/predictor-effects-gallery.pdf
/usr/lib64/R/library/effects/help/AnIndex
/usr/lib64/R/library/effects/help/aliases.rds
/usr/lib64/R/library/effects/help/effects.rdb
/usr/lib64/R/library/effects/help/effects.rdx
/usr/lib64/R/library/effects/help/paths.rds
/usr/lib64/R/library/effects/html/00Index.html
/usr/lib64/R/library/effects/html/R.css
/usr/lib64/R/library/effects/tests/effect-tests-1.R
/usr/lib64/R/library/effects/tests/effect-tests-2.R
/usr/lib64/R/library/effects/tests/regression-tests.R
/usr/lib64/R/library/effects/tests/regression-tests.RData
