from setuptools import setup, find_packages


setup(
    name='pyglottolog',
    version='1.2.2.dev0',
    author='Robert Forkel',
    author_email='forkel@shh.mpg.de',
    description='python package for glottolog data curation',
    keywords='data linguistics',
    license='',
    url='https://github.com/clld/glottolog',
    packages=find_packages(),
    platforms='any',
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['glottolog=pyglottolog.__main__:main'],
    },
    install_requires=[
        'six>=1.9',
        'clldutils>=2.5.2',
        'sqlalchemy',
        'tqdm',
        'pybtex>=0.22',
        'latexcodec',
        'unidecode',
        'whoosh',
        'attrs>=18.1',
        'pycountry>=18.12.8',
        'termcolor',
        'newick',
        'markdown',
        'bs4',
        'requests',
    ],
    extras_require={
        'dev': ['tox>=2.9', 'flake8', 'pep8-naming', 'wheel', 'twine'],
        'test': ['mock>=2', 'pytest>=3.6', 'pytest-mock', 'pytest-cov'],
    },
    long_description='',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
