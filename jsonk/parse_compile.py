import json
import contextlib
import os


@contextlib.contextmanager
def chdir(dirname=None):
    curdir = os.getcwd()
    try:
        if dirname is not None:
            os.chdir(dirname)
        yield
    finally:
        os.chdir(curdir)


def loads(f, dir='.', **kwargs):
    obj = json.loads(f, **kwargs)

    with chdir(dir):
        return resolve_links(obj)


def load(f, dir=None, **kwargs):
    if dir is None:
        dir = os.path.dirname(os.path.realpath(f.name))

    obj = json.load(f, **kwargs)
    with chdir(dir):
        return resolve_links(obj)


def resolve_links(obj):
    t = type(obj)

    if t is str:
        if obj.startswith("@@"):  # escapes @ at start of string
            return obj[1:]
        elif obj.startswith("@"):
            return load(open(obj[1:]))
    elif t is list:
        for i, v in enumerate(obj):
            obj[i] = resolve_links(v)
    elif t is dict:
        for k, v in obj.items():
            obj[k] = resolve_links(v)

    return obj
