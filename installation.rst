*****************************************************************************
Installation
*****************************************************************************

Install
=======

#.  Create a virtual environment using your tool of choice
    (e.g. ``virtualenv`` or ``conda``) and install.

    -  Using `Anaconda <https://www.anaconda.com/>`__

    .. code:: bash

       conda config --add channels conda-forge
       conda config --set channel_priority strict
       conda create -n env_name python=3.8 compas_mobile_robot_reloc
       conda activate env_name

    -  Using `virtualenv <https://github.com/pypa/virtualenv>`__

    .. code:: bash

       virtualenv --python=python3.8 {{path/to/venv}}
       source {{path/to/venv}}/bin/activate
       pip install compas_mobile_robot_reloc

#.  Make package accessible in Rhino and Grasshopper

    .. code:: bash

       python -m compas_rhino.install

Update
======

To update the repository run:

.. code:: bash

   # conda
   conda update compas_mobile_robot_reloc
   # pip
   pip install -U compas_mobile_robot_reloc
