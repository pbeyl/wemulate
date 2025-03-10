.. _install:

Installation of WEmulate
#########################

This part of the documentation covers the installation of WEmulate.


Requirements
*************
In order to use WEmulate to influence traffic at least the following requirements should be fullfilled:

* At least 2 network interfaces for ``LAN-A`` and ``LAN-B``
* Ubuntu installed


Install with bash
**************************
To install WEmulate with bash, simply run this simple command in your terminal of choice::

    $ sh -c "$(curl -fsSL https://raw.githubusercontent.com/wemulate/wemulate/main/install/install.sh)"

There are different arguments available in order to enhance the installation experience:

* ``--verbose`` Enable verbose output for the installer
* ``--force`` or ``--yes`` Skip the confirmation prompt during installation
* ``--configuration-dir`` Override the configuration directory
* ``--release`` Override the release which should be installed
* ``--interface`` Defines a default management interface
* ``--api`` Installs the api module
* ``--frontend`` Installs the frontend module

Install from source
**************************
You can also install WEmulate from source, please follow the instructions below:

* Install all dependencies:

.. code-block:: console

    $ sudo apt install --yes python3 python3-pip 

* Create a new configuration file: ``/etc/wemulate/wemulate.yml``

.. code-block:: console

    ---
    wemulate:
        db_location: /etc/wemulate/wemulate.db

* Clone the repository

.. code-block:: console

    $ git clone https://github.com/wemulate/wemulate

* Install WEmulate

.. code-block:: console

    $ cd wemulate
    $ pip install -r requirements.txt

* Configure the management interfaces

.. code-block:: console

    $ wemulate config set -m ens2