import scrapy
from scrapy.http import headers

"""
Way to determine the page is product page is not :

//*[normalize-space() = 'Buy Now']
//*[normalize-space() = 'BUY NOW']
//*[normalize-space() = 'ADD TO BAG']
//*[normalize-space() = 'Add to Bag']
//*[normalize-space() = 'Add to bag']
//*[normalize-space() = 'Add to Basket']
//*[normalize-space() = 'Add to cart']
"""



class FindproductsSpider(scrapy.Spider):

    name = "find"
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    } 

    headers = {
        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding' : 'gzip, deflate, br',
        'accept-language' : 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control' : 'no-cache',
        'pragma' : 'no-cache',
        'sec-fetch-dest' : 'document',
        'sec-fetch-mode' : 'navigate',
        'sec-fetch-site' : 'none',
        'sec-fetch-user' : '?1',
        'sec-gpc' : '1',
        'upgrade-insecure-requests' : '1'
    }

    def __init__(self, links):
        
        self.links = links

    def start_requests(self):
        
        for link in self.links:
            yield scrapy.Request(
                    url = link,
                    callback = self.parse,
                    headers = self.headers
                )
        
    def parse(self, response):
        """
        To determin if the current page is product page we need to find the,
        buy button on the page, to find those buttons we will search for text
        inside those buttons which can be "buy now", "add to cart", "add to basket", etc.
        """

        buttons = [
            'buy now',
            'Buy Now',
            'BUY NOW',
            'Add to cart',
            'Add To Cart',
            'ADD TO CART',
            'Add to basket',
            'Add To Basket',
            'ADD TO BASKET'
        ]

        flag = False

        for button in buttons:
            
            val = response.xpath(f'//*[normalize-space() = "{button}"]')

            if val:
                flag = True
                break
        
        yield {
            'link' : response.url,
            'True/False' : flag
        }
        