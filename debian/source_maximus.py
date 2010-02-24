def add_info(report):
    from apport.hookutils import attach_gconf
    attach_gconf(report, 'maximus')
