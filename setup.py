import os
import sys
from setuptools import setup, find_packages

__version__ = "0.7.4"

if sys.argv[-1] == 'publish':
    if os.system("pip3 freeze | grep wheel"):
        print("wheel not installed.\nUse `pip3 install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip3 freeze | grep twine"):
        print("twine not installed.\nUse `pip3 install twine`.\nExiting.")
        sys.exit()
    os.system("rm -r dist/*")
    os.system("python3 setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a {0} -m 'version {0}'".format(__version__))
    print("  git push --tags")
    sys.exit()

setup(
    name="mkdocs-alabaster",
    version=__version__,
    author="Ale",
    author_email="hi@ale.rocks",
    description="Alabaster port for MkDocs",
    url="https://github.com/iamale/mkdocs-alabaster",
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
