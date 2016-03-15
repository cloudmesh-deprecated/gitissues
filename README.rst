Cloudmesh Github Issues
========================

Github does not provide natively the support of priorities for issues.
Cloudmesh Github Issues introduces a simple way to do so while not using
labels, but by augmenting the issue boddy.

We provide a simple django bootstrap based portal interface that looks
into the github issues and finds in the first line of an isse the
priority defined with::

  P:10

where 10 is the priority. If no priority is given we use 999.

Install
--------

::

    mkdir -p ~/github/cloudmesh
    cd ~/github/cloudmesh
    git clone https://github.com/cloudmesh/gitissues.git
    pip install -r requirements.txt
    python setup.py install

Customization
-------------

To add other repositories, simple change the links in::

  cloudmesh_gitissues/templates/layout/index.jinja

Run portal
-----------

make run

View portal 
-------------

make view

Bugs and enhancement suggestion
--------------------------------

* We should provide a way to define the repositories to viw with a
  configuration file

* We should be able to modify the priorities in the table, and have
  a save button that than updates all issues (anyone wants to help?)