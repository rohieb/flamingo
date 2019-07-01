import flamingo

# plugins / hooks
CORE_PLUGINS = [
    'flamingo.core.plugins.MetaDataProcessor',
    'flamingo.core.plugins.Hooks',
    'flamingo.core.plugins.Media',
    'flamingo.core.plugins.Static',
]

DEFAULT_PLUGINS = [
    'flamingo.plugins.HTML',
    'flamingo.plugins.Yaml',
    'flamingo.plugins.reStructuredText',
    'flamingo.plugins.rstInclude',
    'flamingo.plugins.rstImage',
    'flamingo.plugins.rstFile',
]

PLUGINS = []
CACHE_HOOKS = True

# parsing
USE_CHARDET = False
DEDENT_INPUT = False
FOLLOW_LINKS = True
HTML_PARSER_RAW_HTML = False

# templating
TEMPLATING_ENGINE = 'flamingo.core.templating.Jinja2'
PRE_RENDER_CONTENT = True
EXTRA_CONTEXT = {}

CORE_THEME_PATHS = [
    flamingo.THEME_ROOT,
]

THEME_PATHS = []

DEFAULT_TEMPLATE = 'page.html'

DEFAULT_PAGINATION = 25

# content
CONTENT_ROOT = 'content'
CONTENT_PATHS = []

# output
OUTPUT_ROOT = 'output'
MEDIA_ROOT = 'output/media'
STATIC_ROOT = 'output/static'
