SUMMARY = "Error - Error/exception handling in an OO-ish way"
DESCRIPTION = "The Error package provides two interfaces. Firstly \
Error provides a procedural interface to exception handling. \
Secondly Error is a base class for errors/exceptions that can \
either be thrown, for subsequent catch, or can simply be recorded."
HOMEPAGE = "https://bitbucket.org/shlomif/perl-error.pm"
SECTION = "libs"
LICENSE = "Artistic-1.0 | GPL-1.0+"

LIC_FILES_CHKSUM = "file://LICENSE;md5=8f3499d09ee74a050c0319391ff9d100"

DEPENDS += "perl"

RDEPENDS_${PN} += " \
    perl-module-carp \
    perl-module-exporter \
    perl-module-scalar-util \
    perl-module-overload \
    perl-module-strict \
    perl-module-vars \
    perl-module-warnings \
"

RDEPENDS_${PN}-ptest += " \
    perl-module-base \
    perl-module-file-spec \
    perl-module-io-handle \
    perl-module-ipc-open3 \
    perl-module-lib \
    perl-module-test-more \
"

SRC_URI = "http://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Error-${PV}.tar.gz"

SRC_URI[md5sum] = "4ef9b2890fb144d804527ba32573dd56"
SRC_URI[sha256sum] = "07b2ac8275dfa04144745a6c1900a596280f862b97d22bab0c5ce02682ebd3be"

S = "${WORKDIR}/Error-${PV}"

inherit cpan ptest-perl

do_install_prepend() {
	# test requires "-T" (taint) command line option
	rm -rf ${B}/t/pod-coverage.t
}

BBCLASSEXTEND = "native"
