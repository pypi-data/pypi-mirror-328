
Installation
============

This assumes you already have a :doc:`WuttJamaican app
<wuttjamaican:narr/install/index>` setup and working.

Install the Wutta-COREPOS package to your virtual environment:

.. code-block:: sh

   pip install Wutta-COREPOS

Edit your :term:`config file` to add CORE-POS DB connection info, and
related settings.

.. code-block:: ini

   [corepos]
   office.url = http://localhost/fannie/

   [corepos.db.office_op]
   default.url = mysql+mysqlconnector://localhost/core_op

   [corepos.db.office_trans]
   default.url = mysql+mysqlconnector://localhost/core_trans

   [corepos.db.office_arch]
   default.url = mysql+mysqlconnector://localhost/trans_archive

   [corepos.db.lane_op]
   keys = 01, 02
   01.url = mysql+mysqlconnector://lane01/opdata
   02.url = mysql+mysqlconnector://lane02/opdata

   [corepos.db.lane_trans]
   keys = 01, 02
   01.url = mysql+mysqlconnector://lane01/translog
   02.url = mysql+mysqlconnector://lane02/translog

And that's it, the CORE-POS integration is configured.


Schema Extension
----------------

As of writing the only reason to add the schema extension is if you
need to map Wutta Users to CORE Employees, for auth (login) purposes.
So this section can be skipped if you do not need that.

This will effectively add the
:attr:`~wutta_corepos.db.model.CoreUser.corepos_employee_number`
attribute on the
:class:`~wuttjamaican:wuttjamaican.db.model.auth.User` model.

First you must override the :term:`app model` with your own.  To do
this, create your own module (e.g. ``poser.db.model``) to contain::

   from wuttjamaican.db.model import *
   from wutta_corepos.db.model import *

Then configure your app model to override the default:

.. code-block:: ini

   [wutta]
   model_spec = poser.db.model

Then configure the Alembic section for schema migrations:

.. code-block:: ini

   [alembic]
   script_location = wuttjamaican.db:alembic
   version_locations = wutta_corepos.db:alembic/versions wuttjamaican.db:alembic/versions

And finally run the Alembic command to migrate:

.. code-block:: sh

   cd /path/to/env
   bin/alembic -c app/wutta.conf upgrade heads

That should do it, from then on any changes will be migrated
automatically during upgrade.
