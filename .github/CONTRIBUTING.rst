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

***************************
Documentation markup syntax
***************************

The documentation build system supports:

-   `reStructuredText <https://docutils.sourceforge.io/rst.html>`_
-   `MarkDown <https://daringfireball.net/projects/markdown/>`_

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
