project = "procurement-tools"
copyright = "2023, V. David Zvenyach"
author = "V. David Zvenyach"
release = "0.1.1"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinxcontrib.autodoc_pydantic",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]


autodoc_pydantic_model_show_json = True
autodoc_pydantic_model_show_config_summary = False
