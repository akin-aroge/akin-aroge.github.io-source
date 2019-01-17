#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Fabusuyi Akindele Aroge'
SITENAME = 'Playground'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Africa/Johannesburg'
DEFAULT_LANG = 'en'

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

THEME = './themes/pelican-alchemy/alchemy'

SITEIMAGE = '/images/akin_aroge.jpg'

DESCRIPTION = 'My exploration as a Data Scientist and beyond'

ICONS = (
    ('github', 'https://github.com/nairobilug/pelican-alchemy'),
	('linkedin', 'https://www.linkedin.com/in/akindele-aroge/'),
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

IGNORE_FILES = ['.ipynb_checkpoints']

# for liquid tags
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'favicon.ico']

# Footer info
LICENSE_URL = "https://github.com/jakevdp/jakevdp.github.io-source/blob/master/LICENSE"
LICENSE = "MIT"