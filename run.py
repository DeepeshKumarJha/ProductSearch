from scrapy.crawler import CrawlerProcess
from product_search.spiders.findproducts import FindproductsSpider



if __name__ == "__main__":
    
    process = CrawlerProcess(
        settings = {
            'FEEDS' : { 
                'result.csv' : { 
                    'format' : 'csv'
                },
            }
        })

    links = [
        'https://www.amazon.in/',
        'https://www.amazon.in/b/?node=1389401031',
        'https://www.amazon.in/dp/B07WDKLZPN'
        ]

    process.crawl(FindproductsSpider, links = links)

    process.start()