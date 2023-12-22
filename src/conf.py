# Sphinx documentation generator configuration

import sys
from datetime import datetime
from pathlib import Path

import toml

# set up paths
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "problem-sets" / "src"))

# read project data from toml file
with open(BASE_DIR / "pyproject.toml") as io_buff:
    project_data = toml.load(io_buff)["tool"]["poetry"]

# project information
project = "Python Training Course"
project_copyright = \
    f"{datetime.now().year}, Python training course authors and contributors"
authors = " \\and ".join(project_data["authors"])
version = project_data["version"]

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
    "sphinx_reredirects",
]
source_suffix = {
    ".txt": "restructuredtext",
    ".rst": "restructuredtext",
    ".md": "markdown",
}
needs_sphinx = "4.0"
exclude_patterns = [
    "**/legacy/**",
    "**/_legacy/**",
    "**/README.*",
]
suppress_warnings = []

# options for reredirects
redirects = {
     "appx/blog/spec": "../../spec/blog/index.html",
     "appx/libms/spec": "../../spec/libms/index.html",
}

# options for bibliography
bibtex_bibfiles = ["refs.bib"]
bibtex_reference_style = "label"

# TODO: configure options for mermaid output for pdf
#       mermaid-js/mermaid-cli is added to project's dependencies

# options for internationalization
gettext_compact = False
language = "en"
locale_dirs = ["_locales"]

# options for HTML output
html_favicon = str(BASE_DIR / "assets" / "favicon.ico")
html_theme = "sphinx_material"
html_theme_options = {
    "nav_title": project,

    "repo_url": project_data["repository"],
    "repo_name": project,
    "repo_type": "github",

    "base_url": project_data["homepage"],

    "globaltoc_depth": 2,

    "css_minify": True,
}

# options for LaTeX output
latex_doc = project.title().replace(" ", "") + ".tex"
latex_engine = "xelatex"
latex_documents = [
    (master_doc, latex_doc, project, authors, "manual", False),
    ("appx/software_list", "Software.tex", project, authors, "howto", False),
    ("appx/code_edit", "IDE.tex", project, authors, "howto", False),
    ("appx/blog/spec", "DjangoBlog.tex", project, authors, "howto", False),
    ("appx/assignments", "CreatingPullRequest.tex",
     "Creating the Pull Request", authors, "howto", False),
]
latex_appendices = [
    # TODO: review appendices list
]
