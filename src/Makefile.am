bin_PROGRAMS=maximus

PKGDATADIR = $(datadir)/maximus
DATADIR = $(datadir)
SYSCONFDIR = $(sysconfdir)
AM_CFLAGS = \
	$(DEPS_CFLAGS) 				\
	$(GCC_FLAGS) 				\
	-I$(top_builddir)			\
	-I$(top_srcdir)				\
	-I$(top_srcdir)/tidy \
	-D_GNU_SOURCE 				\
	-DPKGDATADIR=\"$(PKGDATADIR)\" \
	-DDATADIR=\"$(DATADIR)\" \
	-DSYSCONFDIR=\"$(SYSCONFDIR)\" \
	-DWNCK_I_KNOW_THIS_IS_UNSTABLE=1

maximus_LDADD  = \
	$(DEPS_LIBS)

maximus_SOURCES = \
	main.c \
	eggaccelerators.c \
	eggaccelerators.h \
	maximus-app.c \
	maximus-app.h \
	maximus-bind.c \
	maximus-bind.h \
	tomboykeybinder.c \
	tomboykeybinder.h \
	xutils.c \
	xutils.h 
