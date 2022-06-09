# Makefile for Sphinx documentation

# General paths configuration
SOURCE = docs
BUILDS ?= $(SOURCE)/_builds
CONFIG = $(SOURCE)/conf.py

# Dependencies installation
install:
	pip install -r requirements.txt

# Internationalization
BUILD_GETTEXT = sphinx-build -b gettext
GETTEXT_DIR   = $(BUILDS)/gettext
BUILD_INTL    = sphinx-intl --config="$(CONFIG)" update -p "$(GETTEXT_DIR)"
LOCALE        ?=

# Create gettext files
gettext:
	@$(BUILD_GETTEXT) "$(SOURCE)" "$(GETTEXT_DIR)"

# Update translation files
intl: gettext
	@$(BUILD_INTL) -l $(LOCALE)

# Documentation builds
HTML_DIR   = $(BUILDS)/html
LANGUAGE   ?= en
BUILD_HTML = sphinx-build -b html -D language=$(LANGUAGE)

# Create html output
html:
	@$(BUILD_HTML) "$(SOURCE)" "$(HTML_DIR)/$(LANGUAGE)"
