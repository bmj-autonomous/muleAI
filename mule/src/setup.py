from distutils.core import setup, Extension

setup(
    ext_modules=[Extension("_jsio", ["jsiomodule.c"])]
)
