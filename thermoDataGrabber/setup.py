from setuptools import setup


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
    include_package_data=True, )
