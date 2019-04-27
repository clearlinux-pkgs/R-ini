#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ini
Version  : 0.3.1
Release  : 10
URL      : https://cran.r-project.org/src/contrib/ini_0.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ini_0.3.1.tar.gz
Summary  : Read and Write '.ini' Files
Group    : Development/Tools
License  : GPL-3.0
Requires: R-assertthat
Requires: R-cli
BuildRequires : R-assertthat
BuildRequires : R-cli
BuildRequires : R-rlang
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
# ini
[![Travis-CI Build Status](https://travis-ci.org/dvdscripter/ini.svg?branch=master)](https://travis-ci.org/dvdscripter/ini)
[![CRAN version](http://www.r-pkg.org/badges/version/ini)](https://cran.r-project.org/package=ini)
[![CRAN downloads](http://cranlogs.r-pkg.org/badges/ini)](https://cran.r-project.org/package=ini)

%prep
%setup -q -c -n ini

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552892920

%install
export SOURCE_DATE_EPOCH=1552892920
rm -rf %{buildroot}
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ini
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ini
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ini
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  ini || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ini/DESCRIPTION
/usr/lib64/R/library/ini/INDEX
/usr/lib64/R/library/ini/Meta/Rd.rds
/usr/lib64/R/library/ini/Meta/features.rds
/usr/lib64/R/library/ini/Meta/hsearch.rds
/usr/lib64/R/library/ini/Meta/links.rds
/usr/lib64/R/library/ini/Meta/nsInfo.rds
/usr/lib64/R/library/ini/Meta/package.rds
/usr/lib64/R/library/ini/NAMESPACE
/usr/lib64/R/library/ini/NEWS.md
/usr/lib64/R/library/ini/R/ini
/usr/lib64/R/library/ini/R/ini.rdb
/usr/lib64/R/library/ini/R/ini.rdx
/usr/lib64/R/library/ini/help/AnIndex
/usr/lib64/R/library/ini/help/aliases.rds
/usr/lib64/R/library/ini/help/ini.rdb
/usr/lib64/R/library/ini/help/ini.rdx
/usr/lib64/R/library/ini/help/paths.rds
/usr/lib64/R/library/ini/html/00Index.html
/usr/lib64/R/library/ini/html/R.css
/usr/lib64/R/library/ini/tests/testthat.R
/usr/lib64/R/library/ini/tests/testthat/test-read.ini.R
/usr/lib64/R/library/ini/tests/testthat/test-write.ini.R
/usr/lib64/R/library/ini/tests/testthat/writeini.txt
