AC_PREREQ(2.53)
AC_INIT(maximus, 0.4.11, [])
AM_INIT_AUTOMAKE()
m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])
AC_CONFIG_SRCDIR(src/main.c)
AM_CONFIG_HEADER(config.h)
AM_MAINTAINER_MODE

AC_ISC_POSIX
AC_PROG_CC
AC_STDC_HEADERS
AC_PROG_LIBTOOL

if test "x$GCC" = "xyes"; then
        GCC_FLAGS="-g -Wall -Werror"
fi

AC_SUBST(GCC_FLAGS)


PKG_CHECK_MODULES(DEPS, 
                  gtk+-2.0
                  gconf-2.0 
                  libwnck-1.0
                  libgnomeui-2.0
                  xtst
                  libfakekey
                  )
AC_SUBST(DEPS_CFLAGS)
AC_SUBST(DEPS_LIBS)

AC_PATH_PROG(GCONFTOOL, gconftool-2)
AM_GCONF_SOURCE_2

AC_OUTPUT([
Makefile
data/Makefile
src/Makefile
])
