schemadir = $(sysconfdir)/gconf/schemas
schema_DATA = maximus.schemas

if GCONF_SCHEMAS_INSTALL
install-data-local:
	-GCONF_CONFIG_SOURCE=$(GCONF_SCHEMA_CONFIG_SOURCE) \
	$(GCONFTOOL) --makefile-install-rule $(schema_DATA)
endif

if GCONF_SCHEMAS_INSTALL
uninstall-local:
	-GCONF_CONFIG_SOURCE=$(GCONF_SCHEMA_CONFIG_SOURCE) \
	$(GCONFTOOL) --makefile-uninstall-rule $(schema_DATA)
endif

desktopdir=$(sysconfdir)/xdg/autostart
dist_desktop_DATA=maximus-autostart.desktop

EXTRA_DIST =  $(schema_DATA)
