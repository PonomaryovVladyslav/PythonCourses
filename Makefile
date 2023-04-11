# Python training course makefile for builds automation

# Sphinx settings
SPHINX_SRC = src
SPHINX_CONFIG = $(SPHINX_SRC)/conf.py

# Internationalization
SPHINXINTL_LANGUAGE ?= ua
LANGUAGE            ?= en

# Sphinx build directories
_SPHINX_OUT_BASE = _build
GETTEXT_DIR = $(_SPHINX_OUT_BASE)/gettext
LATEX_DIR = $(_SPHINX_OUT_BASE)/latex/$(LANGUAGE)
HTML_DIR = $(_SPHINX_OUT_BASE)/html/$(LANGUAGE)

# Sphinx builders
SPHINX_BUILD = sphinx-build -q -D language=$(LANGUAGE)

# Makefile targets
all : clean
	@make LANGUAGE=en html
	@make LANGUAGE=ua html

clean :
	@echo "Cleaning existing builds at $(_SPHINX_OUT_BASE)"
	@rm -rf $(_SPHINX_OUT_BASE)

html :
	@echo "LANGUAGE=$(LANGUAGE): generating HTML output at $(HTML_DIR)"
	@$(SPHINX_BUILD) -b html $(SPHINX_SRC) $(HTML_DIR)

latex :
	@echo "LANGUAGE=$(LANGUAGE): generating LaTeX output at $(LATEX_DIR)"
	@$(SPHINX_BUILD) -b latex $(SPHINX_SRC) $(LATEX_DIR)

pdf : latex
	@make -C "$(LATEX_DIR)"

gettext :
	@$(SPHINX_BUILD) -b gettext $(SPHINX_SRC) $(GETTEXT_DIR)

locales : gettext
	@sphinx-intl -c $(SPHINX_CONFIG) update -p $(GETTEXT_DIR)
