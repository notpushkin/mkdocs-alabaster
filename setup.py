from setuptools import setup, find_packages

setup(
    name='mkdocs-alabaster',
    version='0.7.1',
    author='Ale',
    author_email='ale@songbee.net',
    description='Alabaster port for MkDocs',
    url='https://github.com/iamale/mkdocs-alabaster',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'alabaster = mkdocs_alabaster',
        ]
    },
    zip_safe=False
)
