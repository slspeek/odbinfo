# -*- coding: utf-8 -*-


def console(*args, **kwargs):
    '''
    Launch the "python interpreter" gui.

    Positional arguments are only intended for arguments automatically
    passed by the program gui.

    Keyword arguments are:
    - 'loc': for passing caller's locales and/or globals to the console context
    - any constructor constant (BACKGROUND, FOREGROUND...) to tweak the console aspect.

    Examples:
    - console()  # defaut constructor)
    - console(loc=locals())
    - console(BACKGROUND=0x0, FOREGROUND=0xFFFFFF)

    More infos: https://extensions.libreoffice.org/en/extensions/show/apso-alternative-script-organizer-for-python.
    '''

    # we need to load apso before import statement
    ctx = XSCRIPTCONTEXT.getComponentContext()
    ctx.ServiceManager.createInstance("apso.python.script.organizer.impl")
    # now we can use apso_utils library
    from apso_utils import console
    kwargs.setdefault('loc', {})
    kwargs['loc'].setdefault('XSCRIPTCONTEXT', XSCRIPTCONTEXT)
    return console(**kwargs)


g_exportedScripts = console,
