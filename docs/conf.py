# Configuration file for the Sphinx documentation generator

import datetime

# Paths setup
...

# Project information
project = "Python Training Course"
now = datetime.datetime.now()
project_copyright = f"{now:%Y}, {project}"

# General configuration
extensions = [
]
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "restructuredtext",
    ".md": "markdown",
}
needs_sphinx = "4.0"
add_module_names = False

# Options for internationalization
locale_dirs = ["locales"]
gettext_compact = True

# Options for HTML output
html_favicon = "../assets/favicon.ico"
