# Python Training Course project makefile

# base sphinx settings
DOCS_SOURCE    = docs
DOCS_BUILDS    = _build
SPHINX_CONFIG  = ./conf.py
GETTEXT_BUILDS = $(DOCS_BUILDS)/gettext/$(LANGUAGE)
HTML_BUILDS    = $(DOCS_BUILDS)/html/$(LANGUAGE)
LATEX_BUILDS   = $(DOCS_BUILDS)/latex/$(LANGUAGE)

# default internationalization settings
SPHINXINTL_LANGUAGE ?= ua
LANGUAGE            ?= en

# sphinx build settings
BASE_BUILDER    = sphinx-build -c . -q -D language=$(LANGUAGE)
GETTEXT_BUILDER = $(BASE_BUILDER) -b gettext
HTML_BUILDER    = $(BASE_BUILDER) -b html
LATEX_BUILDER   = $(BASE_BUILDER) -b latex

# documentation builds
gettext :
	@$(GETTEXT_BUILDER) "$(DOCS_SOURCE)" "$(GETTEXT_BUILDS)"
html :
	@$(HTML_BUILDER) "$(DOCS_SOURCE)" "$(HTML_BUILDS)"
latex :
	@$(LATEX_BUILDER) "$(DOCS_SOURCE)" "$(LATEX_BUILD)"
pdf : latex
	@make -C "$(LATEX_BUILDS)"

# internationalization
locales : gettext
	@sphinx-intl --config="$(SPHINX_CONFIG)" update -p "$(GETTEXT_BUILDS)"

# clean up builds
clean :
	@rm -rf $(DOCS_BUILDS)

# export variables used by targets
.EXPORT_ALL_VARIABLES :
	export SPHINXINTL_LANGUAGE = $(SPHINXINTL_LANGUAGE)
