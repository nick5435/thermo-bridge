import setuptools
from setuptools import find_packages, setup


def readme():
    """Where the README file is."""
    with open('README.md') as f:
        return f.read()


setup(
    name='ThermoPyle',
    version='0.7.0',
    description='Creation of Thermodynamic Surfaces using CoolProp',
    # long_description=readme(),
    url='https://github.com/nick5435/thermo-bridge',
    author='Nick Meyer',
    author_email='nmeyer5435@gmail.com',
    license='GPLv3+',
    packages=find_packages(),
    zip_safe=False,
    setup_requires=[],
    install_requires=[
        'CoolProp>=6.0.0', 'matplotlib>=2.0.0', 'numpy>=1.12.0',
        'pandas>=0.19.2',
        'pyrsistent>=0.12.0', 'arrow>=0.10.0', 'toolz>=0.8.2',
        'mpld3>=0.3',
    ],
    extra_require={
        'dev': [
            'sphinx>=1.5.1', 'sphinx_bootstrap_theme>=0.4.13',
            'sphinx-autobuild>=0.6.0', 'sphinx-autodoc-typehints>=1.1.0',
            'recommonmark>=0.4.0', 'pypandoc>=1.3.3',
        ],
    },
    python_requires='>=3.5.0',
    include_package_data=True,
    keywords="physics mathematics thermodynamics engineering science chemistry state pandas numpy matplotlib",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3',
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
