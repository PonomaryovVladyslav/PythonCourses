# Configuration file for the Sphinx documentation generator

import datetime
import os
import sys

# Paths setup
# ===========
sys.path.insert(0, os.path.abspath("problem-sets/src"))

# Project information
# ===================
project = "Python Training Course"
now = datetime.datetime.now()
project_copyright = f"{now:%Y}, {project}"
authors = [
    "Vladyslav Ponomaryov",
    "Serhii Horodilov"
]
authors = ", ".join(authors)

# General configuration
# =====================
master_doc = "index"
extensions = [
    "sphinx.ext.imgconverter",
    "myst_parser",
    "sphinx_rtd_theme",
    "sphinxcontrib.mermaid",
]
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "restructuredtext",
    ".md": "markdown",
}
needs_sphinx = "4.0"
add_module_names = False

# Options for internationalization
# ================================
language = "en"
locale_dirs = ["_locales"]
gettext_compact = True

# Options for HTML output
# =======================
html_theme = "sphinx_rtd_theme"
html_favicon = "assets/favicon.ico"

# Options for LaTeX output
# ========================
latex_master_doc = master_doc
latex_output = "PythonTrainingCourse.tex"
latex_engine = "xelatex"
latex_documents = [
    (latex_master_doc, latex_output, project, authors, "manual", False),
]
