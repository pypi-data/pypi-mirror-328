from setuptools import setup

name = "types-psutil"
description = "Typing stubs for psutil"
long_description = '''
## Typing stubs for psutil

This is a [PEP 561](https://peps.python.org/pep-0561/)
type stub package for the [`psutil`](https://github.com/giampaolo/psutil) package.
It can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
[Pyre](https://pyre-check.org/),
PyCharm, etc. to check code that uses `psutil`. This version of
`types-psutil` aims to provide accurate annotations for
`psutil==7.0.*`.

This package is part of the [typeshed project](https://github.com/python/typeshed).
All fixes for types and metadata should be contributed there.
See [the README](https://github.com/python/typeshed/blob/main/README.md)
for more details. The source for this package can be found in the
[`stubs/psutil`](https://github.com/python/typeshed/tree/main/stubs/psutil)
directory.

This package was tested with
mypy 1.15.0,
pyright 1.1.389,
and pytype 2024.10.11.
It was generated from typeshed commit
[`4050dd42ef7ef3311bfd86cfd2d74dd8d809d47e`](https://github.com/python/typeshed/commit/4050dd42ef7ef3311bfd86cfd2d74dd8d809d47e).
'''.lstrip()

setup(name=name,
      version="7.0.0.20250218",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/psutil.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['psutil-stubs'],
      package_data={'psutil-stubs': ['__init__.pyi', '_common.pyi', '_psaix.pyi', '_psbsd.pyi', '_pslinux.pyi', '_psosx.pyi', '_psposix.pyi', '_pssunos.pyi', '_psutil_linux.pyi', '_psutil_osx.pyi', '_psutil_posix.pyi', '_psutil_windows.pyi', '_pswindows.pyi', 'METADATA.toml', 'py.typed']},
      license="Apache-2.0",
      python_requires=">=3.9",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
