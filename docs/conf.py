#!/usr/bin/env python3
import os
import sys
from datetime import date

import sphinx_rtd_theme
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
from poetry.poetry import Poetry


project_dir = os.path.abspath("../")
poetry = Poetry.create(project_dir)
sys.path.append(project_dir)
extensions = ["sphinx.ext.autodoc"]

source_parsers = {".md": CommonMarkParser}
source_suffix = [".md"]
master_doc = "index"

project = "opsgenie-logger"
copyright = "{}, Triax Technologies".format(date.today().year)
author = ", ".join(poetry.package.authors)

version = poetry.package.full_pretty_version

language = "en"
exclude_patterns = []

pygments_style = "sphinx"
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    "logo_only": True,
    "display_version": False,
    "style_external_links": True,
    "style_nav_header_background": "#2c3e50",
}


def setup(app):
    config = {
        # 'url_resolver': lambda url: github_doc_root + url,
        "auto_toc_tree_section": "Contents",
        "enable_eval_rst": True,
    }
    app.add_config_value("recommonmark_config", config, True)
    app.add_transform(AutoStructify)
