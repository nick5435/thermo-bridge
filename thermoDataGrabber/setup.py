from distutils.core import setup


def readme():
    """Where the README file is."""
    with open('README.md') as f:
        return f.read()


setup(
    name='thermoDataGrabber',
    version='0.4',
    description='Creation of Thermodynamic Surfaces using CoolProp',
    long_description=readme(),
    url='https://github.com/nick5435/thermo-bridge',
    author='Nick Meyer',
    author_email='nmeyer14@winona.edu',
    license='MIT',
    packages=['thermoDataGrabber'],
    zip_safe=False,
    install_requires=[
        'CoolProp',
        'matplotlib',
        'numpy',
        'pandas',
        'sphinx',
        'sphinx_bootstrap_theme',
        'sphinx-autobuild',
        'sphinx-autodoc-typehints',
        'recommonmark',
        'pypandoc',
        'typing',
        'pyrsistent',
        'arrow',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Console',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Scientific/Engineering',
        'Operating System :: OS Independent',
        'Framework :: Sphinx',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ], )
