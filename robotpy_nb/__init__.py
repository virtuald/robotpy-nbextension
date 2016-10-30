
try:
    import IPython as _IPython
except ImportError:
    print("IPython must be installed!")
    raise

def _jupyter_server_extension_paths():
    return [{
        "module": "robotpy_nb"
    }]


def load_jupyter_server_extension(nbapp):
    nbapp.log.info("my module enabled!")
    nbapp.FOOOOO = True
    
    ipy = _IPython.get_ipython()
    ipy.FOOOOOO = True


class _Test:
    obj = "This is a test"

def load_ipython_extension(shell):
    print("WTF")
    
    # shell.user_ns.keys()
    
    import ipykernel.zmqshell.ZMQInteractiveShell

def unload_ipython_extension(shell):
    pass
