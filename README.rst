=======
 Vault
=======

A simple password management tool for the command line internface. This
tool uses Python and mcrypt to provide a secure password storage on your
local filesystem.

Requirements
============

You need at least:

    * Python 2.5+ with sqlite3, http://www.python.org/
    * libmcrypt, http://mcrypt.sourceforge.net/
    * python-mcrypt, http://labix.org/python-mcrypt

Optional:

    * sqlite3, http://www.sqlite.org/

Installation
============

Firstly install the required dependencies::

    shell% sudo easy_install -U http://labix.org/download/python-mcrypt/python-mcrypt-1.1.tar.gz
    Downloading http://labix.org/download/python-mcrypt/python-mcrypt-1.1.tar.gz
    Processing python-mcrypt-1.1.tar.gz
    Running python-mcrypt-1.1/setup.py -q bdist_egg --dist-dir /tmp/easy_install-oxt4h4/python-mcrypt-1.1/egg-dist-tmp-vqnQI9
    zip_safe flag not set; analyzing archive contents...
    python-mcrypt 1.1 is already the active version in easy-install.pth

    Installed /usr/local/lib/python2.6/dist-packages/python_mcrypt-1.1-py2.6-linux-i686.egg
    Processing dependencies for python-mcrypt==1.1
    Finished processing dependencies for python-mcrypt==1.1

You can use the ``Makefile`` to make ``vault`` globally available on your
system::

    shell% sudo make install
    install -m755 vault /usr/local/bin/vault

Usage
=====

For an overview of all available ``vault`` commands, use::

    shell% vault help
    Usage: /usr/local/bin/vault help [<command>]

    Shows help on the given command, its syntax and its purpose.

    Available commands:

            del
            get
            help
            list
            set

