# Scrapy settings for Yooxs project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from fake_useragent import UserAgent
ua = UserAgent()

BOT_NAME = "Yooxs"

SPIDER_MODULES = ["Yooxs.spiders"]
NEWSPIDER_MODULE = "Yooxs.spiders"

RETRY_HTTP_CODES = [403, 302,521,404,464]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "Yooxs (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
# PROXY='http://0cef38a862c4b13874e9:ce0155efd5511907@gw.dataimpulse.com:823'
PROXY='http://jyothish_1822:32ed0d-6f9325-3326e6-6e50f3-d7ebe5@residential.proxyomega.com:10001'
# PLAYWRIGHT_MAX_PAGES_PER_CONTEXT = 8

# DOWNLOAD_HANDLERS = {
#     "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
#     "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
# }

# PLAYWRIGHT_LAUNCH_OPTIONS = {
#     # "headless": True,
#     "timeout": 30 * 1000,  # 30 seconds
# }

# PLAYWRIGHT_CONTEXTS = {
#     "persistent": {
#         "headless":False,
#         "viewport": {"width": 1920, "height": 1080},
#         "user_data_dir": "/mnt/g/NST/YOOX/ScrapyPlaywrightYoox/Yooxs/Yooxs/cache",  # will be a persistent context  },
#         "proxy": {
#             "server": "http://c21ef1f997344299918d07075f26c5e0:@api.zyte.com:8011",  # Only the host and port here
#             "username": "c21ef1f997344299918d07075f26c5e0",  # Your Zyte API key as username
#             "password":""
#         }
#         # "user_agent": ua.random,  # Optional: set custom user agent
#     }, 
# }

# PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT = 600 * 1000  # 600 seconds
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "Yooxs.middlewares.YooxsSpiderMiddleware": 543,
#}

# PROXY = "http://aimleap:VKOGGUP-VDW11QX-GJHM5VF-DLBJIMH-HJVFAIM-DVOA1GG-MMHC46T@usa.rotating.proxyrack.net:333"

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': None,
    "Yooxs.middlewares.CustomProxyMiddleware": 543,
   "Yooxs.middlewares.CustomResponseMiddleware": 544,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "Yooxs.pipelines.YooxsPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"




