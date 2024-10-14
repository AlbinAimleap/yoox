# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import tls_client
import urllib.parse
from curl_cffi import requests as curl_requests
from scrapy.http import HtmlResponse
from scrapy.downloadermiddlewares.retry import get_retry_request
from twisted.internet.defer import Deferred

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class YooxsSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class YooxsDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):



        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class CustomResponseMiddleware:
    def __init__(self):
        self.tls_session = tls_client.Session(client_identifier='chrome_120')
        self.cffi_session = curl_requests.Session(impersonate="chrome124")

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s
    
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Continue if response is OK
        if response.status == 200:
            return response

        # Log that we are switching to the TLS client
        spider.logger.info(f"Retrying {request.url} using custom TLS client")
       
        encoded_url = urllib.parse.quote(request.url, safe=':/?&=')
        # Use tls_client first
        tls_response = self.tls_session.get(encoded_url, headers=request.headers.to_unicode_dict())

        if tls_response.status_code == 200:
            return HtmlResponse(
                url=request.url,
                status=tls_response.status_code,
                headers=tls_response.headers,
                body=tls_response.content,
                encoding='utf-8',
                request=request
            )
        
        # If TLS client fails, fallback to cffi_session
        spider.logger.info(f"Retrying {request.url} using curl_requests session")
        cffi_response = self.cffi_session.get(encoded_url, headers=request.headers.to_unicode_dict())
        
        if cffi_response.status_code == 200:
            return HtmlResponse(
                url=request.url,
                status=cffi_response.status_code,
                headers=cffi_response.headers,
                body=cffi_response.content,
                encoding='utf-8',
                request=request
            )

        # If both fail, return original response
        spider.logger.warning(f"Failed to retrieve {request.url} using custom sessions, returning original response.")
        return response        
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

    def spider_closed(self, spider):
        # self.tls_session.close()
        self.cffi_session.close()


class CustomProxyMiddleware(object):
    def __init__(self, settings):
        self.PROXY = settings.get('PROXY')


    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(settings)

    def process_request(self, request, spider):
        request.meta['proxy'] = self.PROXY