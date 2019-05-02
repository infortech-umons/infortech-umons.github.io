#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'inforTech'
SITENAME = 'inforTech'
SITESUBTITLE = 'University of Mons'
SITEURL = 'https://infortech.github.io'
TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = ('%A %d %B %Y')

PATH = 'content'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu
# MENUITEMS = (
#     ('texte', '#'),
#)

# Blogroll
LINKS = (
    ('Infortech Website', 'https://web.umons.ac.be/infortech/fr/'),
    ('University of Mons', 'https://www.umons.ac.be/'),
    ('Sources', 'https://github.com/infortech-umons/infortech.github.io'),
)

# Social widget
SOCIAL = (
    ('facebook', '#'),
    ('envelope', 'mailto:infortech@umons.ac.be'),
)

# Pagination
DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Override
DEFAULT_CATEGORY = 'misc'
TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 50  # Set to None to use full content when "Summary" is not specified
DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = ['static']  # Relative to /content/

THEME = 'themes/infortech'  # You should provide static/css/theme.min.js

PLUGIN_PATHS = ['plugins']
PLUGINS = []