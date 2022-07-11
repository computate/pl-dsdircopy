##########
pl-dsdircopy
##########


Abstract
********

A ChRIS *DS* (Data Synthesis) plugin app that copies files/dirs data from one or more input sources in obj storage to an output sink.


Pre-conditions
**************

When running this plugin from a client perspective to CUBE, note that the *input directories* are actually assumed to exist within obj storage, thus the value of the *input directories* are the prefixes within obj storage. See the wiki pages of CUBE for more information.

Run
***

As a simple Python Application
==============================

Make sure your current working directory is ``dsdircopy`` which contains the file ``dsdircopy.py``. 

The ``--dir`` argument is a string of paths separated by commas.

.. code-block:: bash

        python3 dsdircopy.py <inputDir> <outputDir> --dir <path1, path2>

   
Using ``docker run``
====================

Build the docker image using the ``docker build`` command

.. code-block:: bash

        docker build -t fnndsc/pl-dsdircopy .

Now, use the ``docker run`` command to run the docker image we created above.

Assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``.

You also need to assign a string of paths separated by commas to the ``--dir`` argument.

.. code-block:: bash

    docker run -v $(pwd):/incoming -v $(pwd)/out:/outgoing   \
            fnndsc/pl-dsdircopy dsdircopy.py            \
            --dir "chris/dir1, chris/dir2" /incoming /outgoing

The above command will do nothing as this is a sort of a ChRIS topological plugin that is not meant to be run from the command line.

Make sure that the host ``$(pwd)/out`` directory is world writable!

Running pl-dsdircopy in Podman on RHEL
======================================

.. code-block:: bash

    install -d ~/.local/src/pl-dsdircopy
    # Copy an files to the incoming directory to copy: 
    rsync ~/Pictures/* ~/.local/src/pl-dsdircopy/incoming/
    git clone git@github.com:computate/pl-dsdircopy.git ~/.local/src/pl-dsdircopy
    cd ~/.local/src/pl-dsdircopy
    install -d incoming
    install -d outgoing
    podman build -t computate/pl-dsdircopy .
    podman run --privileged -v ~/.local/src/pl-dsdircopy/in
    coming:/incoming -v ~/.local/src/pl-dsdircopy/outgoing:/outgoing computate/pl-dsdircopy dsdir
    copy.py /incoming /outgoing
    ls incoming/
    ls outgoing/
    # Check that the outgoing directory contains what you were expecting to copy. 





