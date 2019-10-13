
def __mktempdir__():
    "Create a temp directory and return its path. Remove the directory when the program exits."
    from tempfile import mkdtemp
    from shutil import rmtree
    from atexit import register

    path = mkdtemp(prefix='cheerbot-')
    register(lambda: rmtree(path)) # Remove directory at program exit
    return path

__tempdir__ = __mktempdir__()

def tempdir():
    return __tempdir__
