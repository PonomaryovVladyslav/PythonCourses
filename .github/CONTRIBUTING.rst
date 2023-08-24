.. _Sphinx: https://www.sphinx-doc.org/
.. _sphinxcontrib-mermaid: https://pypi.org/project/sphinxcontrib-mermaid/

###############################################################################
                              CONTRIBUTING GUIDES
###############################################################################

Welcome and thank you for considering contributing to our project! Here we have
an ecosystem of documentation tools, what helps us to deliver valuable
knowledge about Python programming language to the public.

Collaborating with us means delving into this, which this guide will help you
navigate. From the intricacies of Sphinx to the fluidity of Mermaid diagrams,
we aim to provide you with all the insights you need.

Let's dive in!

*******************
Documentation tools
*******************

`Sphinx`_ makes it easy to create intelligent and beautiful documentation.
This is the main documentation generator used on this project. There are also
some 3rd-party dependencies, like ``sphinxcontrib-mermaid`` or
``MyST markdown`` installed, that makes it possible to use some extended
syntax. Just install all project dependencies (including development).

.. code-block:: shell

    poetry install --with dev

**requirements.txt** file does not split general and development deps, just do:

.. code-block:: shell

    pip install -r requirements.txt

Other useful tools
==================

We found ``poedit`` software very useful for working with translations.

.. todo

********************
Repository structure
********************

::

    /
    |-- assets/
    |-- src/
    |-- index.txt
    |-- <topic>/
    |---- index.txt
    |-- problem-sets/

**src** directory is the main documentation source, and it's considered to be
a *content-root*. It means you may refer this directory as ``/`` for the Sphinx
documentation builder.

The **src/index.txt** is the master document. It combines all the content
together. All topics are described in their own "topic" directories, each with
its own *index.txt*. Topic index file is the :abbr:`TOC (Table of Content)` for
the topic, and it should be added to the master TOC.

**assets** directory contains various static content for the documentation,
like CSS, images etc.

**problem-sets** is a sub-module, that contains various challenges and demos.
It's already included to the documentation generator config, so any materials
from this repo can be referred in the documents.

***************************
Documentation markup syntax
***************************

The documentation build system supports:

-   `reStructuredText <https://docutils.sourceforge.io/rst.html>`_
-   `MarkDown <https://daringfireball.net/projects/markdown/>`_
-   `mermaid <https://mermaid.js.org/>`_

The main documentation syntax is "reST", since it provides more flexibility
while working with docs.

reStructuredText syntax
=======================

Headings
--------

Here we use structure "part > chapter > section > subsection".

::

    ####
    Part
    ####

    *******
    Chapter
    *******

    Section
    =======

    Subsection
    ----------

All of these above will be added to :abbr:`TOC (Table of Content)`.
In case you want to avoid this use ``rubric`` directive to mark a heading
without adding it to the TOC.

::

    .. rubric:: Rubric heading

    And the content goes here.

Mermaid diagrams
----------------

The build system supports ``mermaid`` syntax via ``.. mermaid::`` directive.
This is done using `sphinxcontrib-mermaid`_ extension.

There are two main approaches to include mermaid diagrams to the documentation:

-   integrate a file containing the diagram

    ::

        .. mermaid:: /../assets/mermaid/<path>/<file.mmd>

-   integrate the mermaid block itself

    ::

        .. mermaid::

            flowchart LR
                id

MarkDown
========

MarkDown is not the main markup language, but it is supported as well.

Headings
--------

Just place a hash symbol before the heading. The number of hashes controls
the heading's level.

::

    # Part
    ## Chapter
    ### Section
    #### Subsection

Mermaid diagrams
----------------

Mermaid support for MarkDown source is limited with just including mermaid
blocks:

::

    ```mermaid
    flowchart LR
        id
    ```

*********
Branching
*********

Branches explanation
====================

This repo comes with two main branches: ``master`` and ``devel``.
``master`` branch contains some stable releases of the documentation, while
``devel`` aggregates works for the future releases.

Working with topic branch(es)
=============================

We use GitFlow approach on this project. This means you would not commit to
``master`` or ``devel`` branches directly. Instead you are to create a topic
branch to work with.

For example, if you want to describe "Django middleware", you will create
a new branch ``[topic/]django-middleware``, and you will commit all your work
to this branch.

Once you consider the work is done - just open a pull request from your topic
branch to ``devel``.

**********************
Working with documents
**********************

Do not make changes in **src** directory directly, except changes to "conf.py"
and "index.txt" files. Keep your documents in dedicated topic directories
instead. This project has some predefined topics already, so you can work
inside of an existing topic directory.

How to add new document(s)
==========================

.. todo

How to add new topic(s)
=======================

.. todo

How to translate
================

.. todo
