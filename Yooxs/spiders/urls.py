import scrapy
from bs4 import BeautifulSoup
import pandas as pd

class YooxUrlSpider(scrapy.Spider):
    name = 'yoox_url'
    # allowed_domains = ['yoox.com']
    # proxy= "http://aimleap:VKOGGUP-VDW11QX-GJHM5VF-DLBJIMH-HJVFAIM-DVOA1GG-MMHC46T@usa.rotating.proxyrack.net:333"
    proxy = "http://c21ef1f997344299918d07075f26c5e0:@api.zyte.com:8011"
    def start_requests(self):
        category_dict = {"woment_clothing":"https://www.yoox.com/us/women/clothing/shoponline?area=women&page=2&dept%5B0%5D=clothingwomen&sortBy=",
        "women_shoes":"https://www.yoox.com/us/women/shoes/shoponline?area=women&dept%5B0%5D=shoeswomen&sortBy=",
        "women_accessories":"https://www.yoox.com/us/women/accessories%20&%20bags/shoponline?area=women&dept%5B0%5D=bagsaccwomen&sortBy=",       
        "men_clothing":"https://www.yoox.com/us/men/clothing/shoponline?area=men&dept%5B0%5D=clothingmen&sortBy=",
        "men_shoes":"https://www.yoox.com/us/men/shoes/shoponline?area=men&dept%5B0%5D=shoesmen&sortBy=",
        "men_accessories":"https://www.yoox.com/us/men/accessories/shoponline?area=men&dept%5B0%5D=accessoriesmen&sortBy="}
        for category in list(category_dict.keys())[:1]:
            category_url = category_dict[category]
            yield scrapy.Request(url=category_url,  callback=self.collect_category_data,
            dont_filter = True,meta={'proxy':self.proxy,'category':category ,'category_url':category_url})

    def collect_category_data(self, response):
        category = response.meta.get('category')
        category_url = response.meta.get('category_url')
        soup = BeautifulSoup(response.text, 'html.parser')
        pagination_list = [i.text for i in soup.find(class_='pagination').find_all("li")]
        total_pages = pagination_list[-1].strip()
        print(total_pages)

        next_page_url = soup.find(class_='pagination').find_all("li")[-1].find("a")['href']
        # for page in range(1,int(total_pages)+1):
        for page in range(1,total_pages+1):
            page_url = next_page_url.replace(total_pages,str(page))
            print("**************************")
            print(page,page_url)
            print("pending_pages :",int(total_pages)-int(page))
            print("**************************")
            yield scrapy.Request(url=page_url,  callback=self.collect_product_urls,
            dont_filter = True,meta={'proxy':self.proxy,'category': category,'page_url':page_url,"total_pages":total_pages,"page":page})

    def collect_product_urls(self,response):
        category = response.meta.get('category')
        total_pages = response.meta.get('total_pages')
        page = response.meta.get('page')
        soup = BeautifulSoup(response.text, 'html.parser')
        container = response.css('.itemContainer')

        for link_tag in container:
            try:
                link = "https://www.yoox.com"+link_tag.css(".itemlink::attr(href)").extract()[0]
            except:
                link = "-"
                print("no url")
            if link != '-':
                data_dict = {"category":category,"product_url":link,"total_pages":total_pages,"page":page}
                product_df = pd.DataFrame(data_dict,index=[0],columns=['category','product_url','total_pages','page'])
                with open('yoox_urls.csv','a',newline='',encoding='utf-8') as f:
                    product_df.to_csv(f, mode='a',header=f.tell()==0)

