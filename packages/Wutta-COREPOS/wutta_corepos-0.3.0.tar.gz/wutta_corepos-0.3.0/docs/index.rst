
Wutta-COREPOS
=============

This package adds basic integration with `CORE-POS`_, using
`pyCOREPOS`_.

It provides the following:

* standard configuration for CORE Office + Lane databases
* special :term:`handler` for CORE integration
  (:class:`~wutta_corepos.handler.CoreposHandler`)
* readonly web views for primary CORE Office DB tables
* :term:`data model` extension to map
  :class:`~wuttjamaican:wuttjamaican.db.model.auth.User` to CORE
  Employee

.. _CORE-POS: https://www.core-pos.com/

.. _pyCOREPOS: https://pypi.org/project/pyCOREPOS/


.. toctree::
   :maxdepth: 2
   :caption: Documentation

   narr/install

.. toctree::
   :maxdepth: 1
   :caption: API

   api/wutta_corepos
   api/wutta_corepos.app
   api/wutta_corepos.conf
   api/wutta_corepos.db
   api/wutta_corepos.db.model
   api/wutta_corepos.handler
   api/wutta_corepos.web
   api/wutta_corepos.web.db
   api/wutta_corepos.web.views
   api/wutta_corepos.web.views.corepos
   api/wutta_corepos.web.views.corepos.master
   api/wutta_corepos.web.views.corepos.members
   api/wutta_corepos.web.views.corepos.products
