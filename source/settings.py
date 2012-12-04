# ===============
# Basic settings
# ===============
AUTHOR = 'Palak Mathur'
DEFAULT_CATEGORY = 'Blog'
SITENAME = 'Palak Mathur'
SITEURL = 'http://palakmathur.github.com'
SITE_URL = SITEURL
STATIC_PATHS = ['images', ]
TIMEZONE = 'Asia/Delhi'


# =============
# URL settings
# =============
ARTICLE_SAVE_AS = '/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = '/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
PERMALINK_STRUCTURE = '{date:%Y}/{date:%m}/'
#ARTICLE_URL = '%s{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_LANG_URL = '%s{slug}-{lang}.html' % PERMALINK_STRUCTURE
PAGE_URL = '%spages/{slug}.html' % PERMALINK_STRUCTURE
PAGE_LANG_URL = '%spages/{slug}-{lang}.html' % PERMALINK_STRUCTURE
#ARTICLE_SAVE_AS = '%s{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_LANG_SAVE_AS = '%s{slug}-{lang}.html' % PERMALINK_STRUCTURE
PAGE_SAVE_AS = '%spages/{slug}.html' % PERMALINK_STRUCTURE
PAGE_LANG_SAVE_AS = '%spages/{slug}-{lang}.html' % PERMALINK_STRUCTURE



# ===========
# Pagination
# ===========
WITH_PAGINATION = True
DEFAULT_PAGINATION = 10


# =================
# Ordering content
# =================
REVERSE_ARCHIVE_ORDER = True


# =================
# Theming
# =================
#THEME = 'notmyidea'

DISQUS_SITENAME = 'palakmathur-github'
FLATTR = True
GITHUB_URL = 'http://github.com/palakmathur/palakmathur.github.com'
#GOOGLE_ANALYTICS = 'UA-1147761-33'
MENUITEMS = (
    ('Archives', '{0}/archives.html'.format(SITEURL)),
)
TWITTER_USERNAME = 'palak'
