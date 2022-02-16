""" Helper to call a macro in LibreOffice """


def invoke_macro(ctx, macro_uri):
    """ Invokes macro from `macro_uri` """
    mspf = ctx.ServiceManager.createInstanceWithContext(
        "com.sun.star.script.provider.MasterScriptProviderFactory", ctx)
    script_provider = mspf.createScriptProvider("")
    macro = script_provider.getScript(macro_uri)
    return macro.invoke((), (), ())
