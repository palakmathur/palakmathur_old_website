#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

GITHUB_URL = 'https://github.com/palakmathur/palakmathur.github.com'
DISQUS_SITENAME = 'palakmathur-github'

SITEURL = 'http://palakmathur.github.com'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
#RELATIVE_URLS = False

DISQUS_SITENAME = "palakmathur-github"
#GOOGLE_ANALYTICS = ""

ARTICLE_SAVE_AS = '/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = '/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
AUTHOR = u'Palak Mathur'
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
DEFAULT_CATEGORY = 'Blog'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10



#GOOGLE_ANALYTICS = 'UA-34988446-1'
#SOCIAL = (
 #   ('aclark4life', 'http://twitter.com/aclark4life'),
 #   ('ACLARKNET', 'http://twitter.com/ACLARKNET'),
 #   ('GitHub', 'http://github.com/aclark4life'),
 #   ('Gittip', 'https://www.gittip.com/aclark4life'),
 #   ('PythonPackages', 'https://pythonpackages.com/user/aclark4life'),
 #   ('atom feed (Django)', 'http://blog.aclark.net/feeds/Django.atom.xml'),
 #   ('atom feed (Mozilla)', 'http://blog.aclark.net/feeds/Mozilla.atom.xml'),
 #   ('atom feed (Plone)', 'http://blog.aclark.net/feeds/Plone.atom.xml'),
 #   ('atom feed (Python)', 'http://blog.aclark.net/feeds/Python.atom.xml'),
#)
#TAG_FEED_ATOM = 'feeds/%s.atom.xml'
#TAG_FEED_RSS = None
#THEME = 'notmyidea_solarized'
TWITTER_USERNAME = 'palak'
