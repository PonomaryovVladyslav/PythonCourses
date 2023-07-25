# Sphinx documentation generator configuration

import sys
from datetime import datetime
from pathlib import Path

# set up paths
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "problem-sets" / "src"))

# project information
project = "Python Training Course"
project_copyright = \
    f"{datetime.now().year}, Python training course authors and contributors"
authors = "Vladyslav Ponomaryov \\and " \
          "Serhii Horodilov"
version = "2023.06.dev"

# general configuration
master_doc = root_doc = "index"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.imgconverter",

    "sphinxcontrib.bibtex",
    "sphinxcontrib.mermaid",
    "sphinx_rtd_theme",
    "myst_parser",
    "sphinx_copybutton",
]
source_suffix = {
    ".txt": "restructuredtext",
    ".rst": "restructuredtext",
    ".md": "markdown",
}
needs_sphinx = "4.0"
exclude_patterns = []
suppress_warnings = []

# options for bibliography
bibtex_bibfiles = ["refs.bib"]
bibtex_reference_style = "label"

# TODO: configure options for mermaid output for pdf
#       mermaid-js/mermaid-cli is added to project's dependencies

# options for internationalization
language = "en"
locale_dirs = ["_locales"]

# options for HTML output
html_theme = "sphinx_rtd_theme"
html_favicon = str(BASE_DIR / "assets" / "favicon.ico")

# options for LaTeX output
latex_doc = project.title().replace(" ", "") + ".tex"
latex_engine = "xelatex"
latex_documents = [
    (master_doc, latex_doc, project, authors, "manual", False),
    ("appx/software_list", "Software.tex", project, authors, "howto", False),
    ("appx/code_edit", "IDE.tex", project, authors, "howto", False),
    ("appx/blog", "DjangoBlog.tex", project, authors, "howto", False),
    ("appx/create_pr", "CreatingPullRequest.tex", "Creating the Pull Request",
     authors, "howto", False),
]
latex_appendices = [
    "appx/software_list",
    "appx/code_edit",
    "appx/env_path",
    "appx/precedence",
    "appx/printf",
    "appx/create_pr",
    "appx/conv_store",
    "appx/wtk",
    "appx/blog",
]
