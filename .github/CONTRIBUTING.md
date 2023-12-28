# CONTRIBUTING GUIDES

Welcome and thank you for considering contributing to our project! Here
we have an ecosystem of documentation tools, what helps us to deliver
valuable knowledge about Python programming language to the public.

Collaborating with us means delving into this, which this guide will
help you navigate. From the intricacies of Sphinx to the fluidity of
Mermaid diagrams, we aim to provide you with all the insights you need.

Let\'s dive in!

## Documentation tools

[Sphinx](https://www.sphinx-doc.org/) makes it easy to create
intelligent and beautiful documentation. This is the main documentation
generator used on this project. There are also some 3rd-party
dependencies, like `sphinxcontrib-mermaid` or `MyST markdown` installed,
that makes it possible to use some extended syntax. Just install all
project dependencies (including development).

``` shell
poetry install --with dev
```

**requirements.txt** file does not split general and development deps,
just do:

``` shell
pip install -r requirements.txt
```

### Other useful tools

We found [poedit](https://poedit.net/) software very useful for working
with translations. It can be used for documents automatic translation,
storing translation memories, proofreading etc.

## Repository structure

    /
    |-- assets/
    |-- src/
    |-- index.txt
    |---- index.txt
    |---- <topic>/

**assets** directory contains various static content for the
documentation, like CSS, images etc.

**src** directory is the main documentation source, and it\'s considered
to be a *content-root*. It means you may refer this directory as `/` for
the Sphinx documentation builder.

The **src/index.txt** is the master document. It combines all the
content together. All topics are described in their own \"topic\"
directories, each with its own *index.txt*. Topic index file is the
`TOC (Table of Content)`{.interpreted-text role="abbr"} for the topic,
and it should be added to the master TOC.

### Submodules

There are two major approaches in the code base organization: monorepo
and multirepo.

This repository uses **hybrid poly-as-mono** approach. It includes
several other repositories as its submodules to glue the content from
different repos together.

Make sure submodules are pulled from the `devel` branch.

## Documentation markup syntax

The documentation build system supports:

-   [reStructuredText](https://docutils.sourceforge.io/rst.html)
-   [MarkDown](https://daringfireball.net/projects/markdown/)
-   [mermaid](https://mermaid.js.org/)

The main documentation syntax is \"reST\", since it provides more
flexibility while working with docs.

### reStructuredText syntax

#### Headings

Here we use structure \"part \> chapter \> section \> subsection\".

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

All of these above will be added to
`TOC (Table of Content)`{.interpreted-text role="abbr"}. In case you
want to avoid this use `rubric` directive to mark a heading without
adding it to the TOC.

    .. rubric:: Rubric heading

    And the content goes here.

#### Mermaid diagrams

The build system supports `mermaid` syntax via `.. mermaid::` directive.
This is done using
[sphinxcontrib-mermaid](https://pypi.org/project/sphinxcontrib-mermaid/)
extension.

There are two main approaches to include mermaid diagrams to the
documentation:

-   integrate a file containing the diagram

        .. mermaid:: /../assets/mermaid/<path>/<file.mmd>

-   integrate the mermaid block itself

        .. mermaid::

            flowchart LR
                id

### MarkDown

MarkDown is not the main markup language, but it is supported as well.

#### Headings

Just place a hash symbol before the heading. The number of hashes
controls the heading\'s level.

    # Part
    ## Chapter
    ### Section
    #### Subsection

#### Mermaid diagrams

Mermaid support for MarkDown source is limited with just including
mermaid blocks:

    ```mermaid
    flowchart LR
        id
    ```

## Branching

### Branches explanation

This repo comes with two main branches: `master` and `devel`. `master`
branch contains some stable releases of the documentation, while `devel`
aggregates works for the future releases.

### Working with topic branch(es)

We use GitFlow approach on this project. This means you would not commit
to `master` or `devel` branches directly. Instead you are to create a
topic branch to work with.

For example, if you want to describe \"Django middleware\", you will
create a new branch `[topic/|feature/]django-middleware`, and you will
commit all your work to this branch.

Once you consider the work is done - just open a pull request from your
topic branch to `devel`.

## Working with documents

Do not make changes in **src** directory directly, except changes to
\"conf.py\" and \"index.txt\" files. Keep your documents in dedicated
topic directories instead. This project has some predefined topics
already, so you can work inside of an existing topic directory.

### How to add new document(s)

Locate the corresponding topic and create a new text file. Use `.txt`
extension for the reStructuredText documents, and `.md` for the Markdown
markup. Keep filename meaningful.

To attach the newly created document to the documentation builds, just
add its name to the `toctree` directive content in the **index.txt**
file within the appropriate topic directory. Do not add file extension
while adding file to the `toctree`.

In rare cases, when the new document should not be a part of any
toctree, you are to `:orphan:` mark at its begging.

### How to add new topic(s)

Most of the topics are already present in the documents root. However,
in case of need to add a new topic - you are to create a new directory
inside of *src* folder. Create a file called `index.txt` within a new
directory, and add it to the master doc (toctree): **src/index.txt**.

### How to translate

There is a target defined in Makefile to build and/or update
translations called `locales`. To gather newly added or updated strings
and prepare portable object files, do:

``` shell
make locales
```

This will create/update po files in *src/\_locales* directory. Navigate
to the file and perform translations.

Original strings are marked as `msgid`, and the translated versions are
marked as `msgstr`.

Using software like [poedit](https://poedit.net/) can make the
translation process more efficient.

In case, you don\'t have cmake/make installed on your computer, you may
use the full commands to gather the text, and prepare po file:

``` shell
sphinx-build -b gettext src _build/gettext
sphinx-intl -c src/conf.py update -p _build/gettext
```

Actually, `make locales` is the shortcut to the same set of commands.
