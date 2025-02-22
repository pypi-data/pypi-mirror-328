tomwer
======

tomwer is offering tools to automate acquisition and reconstruction processes for Tomography.
It contains:

- a library to access each acquisition process individually
- gui and applications to control main processes (reconstruction, data transfert...) and execute them as a stand alone application.
- an orange add-on to help users defining their own workflow (http://orange.biolab.si)



.. image:: http://www.edna-site.org/pub/doc/tomwer/extra/tomwer_start_short.gif


.. |Gitlab Status| image:: https://gitlab.esrf.fr/tomotools/tomwer/badges/master/pipeline.svg
    :target: https://gitlab.esrf.fr/tomotools/tomwer/pipelines


Documentation
-------------

`Latest documentation <https://tomotools.gitlab-pages.esrf.fr/tomwer/>`_


Installation
------------

Step 1 - tomwer
'''''''''''''''

To install it with all 'features':

.. code-block:: bash

    pip install tomwer[full]

alternatively you can install the master branch from

.. code-block:: bash

    pip install git+https://gitlab.esrf.fr/tomotools/tomwer/#egg=tomwer[full]


Step 2 - update orange-canvas-core and orange-widget-base (Optional)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

To access 'processing' wheels and 'reprocess action' you might want to install forks of update orange-canvas-core and orange-widget-base. This is optional and projects works with native orange projects

.. code-block:: bash

    pip install git+https://github.com/payno/orange-canvas-core --no-deps --upgrade
    pip install git+https://github.com/payno/orange-widget-base --no-deps --upgrade


Launching applications
::::::::::::::::::::::

After the installation tomwer is embedding several applications.

Those applications can be launched by calling:

.. code-block:: bash

   tomwer appName {options}

.. note:: if you only call `tomwer` then the man page will be displayed.

.. note:: You can access each application help using ``

    .. code-block:: bash

       tomwer appName --help


tomwer canvas - orange canvas
'''''''''''''''''''''''''''''

You can launch the canvas to create workflows from the different 'bricks'

.. code-block:: bash

   tomwer canvas

.. note:: you can also use `orange-canvas`

.. note:: if your installed a virtual environment do not forget to active it :

    .. code-block:: bash

       source myvirtualenv/bin/activate


Documentation
:::::::::::::

.. code-block:: bash

   sphinx-build doc build/html

The documentation is build in doc/build/html and the entry point is index.html

.. code-block:: bash

   firefox build/html/index.html

.. note:: the build of the documentation need sphinx to be installed. This is not an hard dependacy. So you might need to install it.
