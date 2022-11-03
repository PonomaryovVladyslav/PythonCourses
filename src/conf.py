# Sphinx documentation generator configuration

from datetime import datetime

# project information
project = "Python Training Course"
project_copyright = \
    f"{datetime.now().year}, Python training course authors and contributors"
authors = "Vladyslav Ponomaryov \\and Serhii Horodilov"
version = "2022.11.dev"

# general configuration
master_doc = root_doc = "index"
extensions = [
    "sphinx_rtd_theme",
    "myst_parser",
]
source_suffix = {
    ".txt": "restructuredtext",
    ".rst": "restructuredtext",
    ".md": "markdown",
}
needs_sphinx = "4.0"
exclude_patterns = []
suppress_warnings = []

# options for internationalization
language = "en"
locale_dirs = ["_locales"]

# options for HTML output
html_theme = "sphinx_rtd_theme"
# html_favicon = "relative/path/to/favicon" todo

# options for LaTeX output
latex_doc = project.title().replace(" ", "") + ".tex"
latex_engine = "xelatex"
latex_documents = [
    (master_doc, latex_doc, project, authors, "manual", False),
]
