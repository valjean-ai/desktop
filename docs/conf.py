import os
import sys

sys.path.insert(0, os.path.abspath('.'))

# Project info
project = 'New Gold Desktop'
author = 'Adele Collins'
release = '1.0'

# General config
extensions = []

templates_path = ['_templates']
exclude_patterns = []

# HTML settings
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# ✅ Google Verification (WORKING METHOD)
html_context = {
    "metatags": '<meta name="google-site-verification" content="xMvhEb7ayr2oSB67CmQJ-XqQ7Pati-Stu9KHRdN-J6c" />'
}
