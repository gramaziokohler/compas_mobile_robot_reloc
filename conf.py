# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sphinx_compas_theme

from compas_mobile_robot_reloc import __version__

pkg_name = "compas_mobile_robot_reloc"
project = "COMPAS Mobile Robot Relocalization"
copyright = "Gramazio Kohler Research"
author = "Anton T Johansson"
version = release = __version__

source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
templates_path = ["_templates"]


extensions = [
    "m2r2",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

# Extension conf

# autodoc options
autodoc_default_options = {
    "member-order": "bysource",
    "special-members": "__init__",
    "exclude-members": "__weakref__",
    "undoc-members": True,
    "show-inheritance": True,
}

autodoc_mock_imports = ["Rhino"]
autodoc_member_order = "alphabetical"

autoclass_content = "class"  # don't include __init__ docstring

# intersphinx
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", "https://docs.python.org/3/objects.inv"),
    "compas": (
        "https://compas.dev/compas/latest",
        "https://compas.dev/compas/latest/objects.inv",
    ),
}

# HTML output conf
html_theme = "compaspkg"
html_theme_path = sphinx_compas_theme.get_html_theme_path()

html_theme_options = {
    "package_name": pkg_name,
    "package_title": project,
    "package_version": version,
    "package_repo": f"https://github.com/gramaziokohler/{pkg_name}",
    "package_docs": f"https://gramaziokohler.github.io/{pkg_name}",
}

html_add_permalinks = ""
html_copy_source = True
html_experimental_html5_writer = True
