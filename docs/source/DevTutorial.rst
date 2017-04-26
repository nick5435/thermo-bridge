.. highlight:: shell-session

####################
Development Tutorial
####################

Required Tools
==============

* `Git <https://git-scm.com/downloads>`_
* `Git-LFS <https://git-lfs.github.com/>`_
* `Anaconda Python 3.6+ <https://www.continuum.io/downloads>`_
* Text Editor or IDE

  * `Atom <https://atom.io>`_ is recommended
  * However, VSCode, SublimeText3, PyCharm, Emacs, and Komodo Edit are all good options as well.

* `Pandoc <http://pandoc.org/installing.html>`_ for Documentation
* `wkhtmltopdf <http://wkhtmltopdf.org/downloads.html>`_ Stable
* A working C/C++ Compiler (MinGW recommended)

Setup Process
=============

#. Install your C/C++ Compiler, making sure that its tools end up in your path.
#. Install Git using its default settings.
#. Install Git-LFS using its default settings.
#. Install Anaconda using its default options.
#. Install Pandoc and wkhtmltopdf with their default options.
#. Restart Computer at this point.
#. Open up a command prompt and run the following commands::

    git lfs install
    conda update --all
    cd ~
    git clone https://github.com/nick5435/thermo-bridge.git
    cd thermo-bridge
    pip install -U -e ThermoPyle[dev]
    conda update --all

#. For a runtime example, open :code:`notebooks/thermo_generic_library_runner.ipynb` using :code:`jupyter notebook`

Atom Setup
==========

#. Install `Atom <https://atom.io>`_ using its default settings
#. Open up a terminal and run the following commands::

    pip install isort autopep8 pep8  linter mypy pygments mypy-lang -U
    apm install fonts advanced-open-file autocomplete-paths multi-cursor-plus magicpython atom-beautify autocomplete-python file-icons fonts
    apm install language-markdown language-restructuredtext linter minimap minimap-linter minimap-find-and-replace
    apm install language-openscad sublime-style-column-selection python-isort python-snippets python-tools script swackets tabs-to-spaces
    apm install todo-show tool-bar tool-bar-basic atom-material-ui atom-material-syntax-dark

#. Open Atom, then go to **File > Settings > Send Telemetry to Atom Team > Do not send any telemetry data**.
#. **Settings > Themes > UI Theme > Atom Material** and **Themes > Syntax Theme > Atom Material Dark**
#. **Settings > Packages** Disable the following packages: :code:`language-python language-gfm background-tips wrap-guide deprecation-cop exception-reporting metrics open-on-github package-generator styleguide welcome` and whatever language packages you feel that you won't need.
