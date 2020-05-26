##########
pl-dsdircopy
##########


Abstract
********

A ChRIS *DS* (Data Synthesis) plugin app that copies file/dir data from an input source to an output sink. If called directly, i.e. from the command line, the *input directory* is an actual specification on an actual filesystem. If called from a client that is talking to CUBE, this *input directory* is interpreted to mean a location within swift storage, and is *not* a file system location.


Pre-conditions
**************

When running this plugin from a client perspective to CUBE, note that the *input directory* is actually assumed to exist within swift storage, thus the value of the *input directory* is the prefix within swift storage. See the wiki pages of CUBE for more information.

Run
***

As a simple Python Application
==============================

Make sure your current working directory is ``dsdircopy`` which contains the file ``dsdircopy.py``. 

The directory passed to the ``--dir`` argument should be within the specified ``inputDir``.

.. code-block:: bash

        python3 dsdircopy.py <inputDir> <outputDir> --dir <directory>

   
Using ``docker run``
====================

Build the docker image using the ``docker build`` command

.. code-block:: bash

        docker build -t fnndsc/pl-dsdircopy .

Now, use the ``docker run`` command to run the docker image we created above.

Assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``.

You also need to assign a directory within the ``inputDir`` to the ``--dir`` argument.

.. code-block:: bash

    docker run -v $(pwd):/incoming -v $(pwd)/out:/outgoing   \
            fnndsc/pl-dsdircopy dsdircopy.py            \
            --dir /incoming /outgoing

The above command will recursively copy the directory passed to the ``--dir`` argument to the container's ``/outgoing``
which in turn has been volume mapped to the host ``$(pwd)/out`` directory.

Make sure that the host ``$(pwd)/out`` directory is world writable!







