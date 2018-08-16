import os
import sys
from setuptools import setup, find_packages

__version__ = "0.7.5"

if sys.argv[-1] == 'publish':
    os.system("python3 setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    os.system("rm -r dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a {0} -m 'version {0}'".format(__version__))
    print("  git push --tags")
    sys.exit()

setup(
    name="mkdocs-alabaster",
    version=__version__,
    author="Alexander Pushkov",
    author_email="alexander@notpushk.in",
    description="Alabaster port for MkDocs",
    url="https://github.com/notpushkin/mkdocs-alabaster",
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "mkdocs.themes": [
            "alabaster = mkdocs_alabaster",
        ]
    },
    zip_safe=False
)
