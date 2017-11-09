from harrispierce.scrapping.scrap_urls import journals
from harrispierce.scrapping.scrap import scrap
from harrispierce.scrapping.scrap_articles import FTScrapingMachine
from harrispierce.util.config import ScrappingConfig

all_scrappers = {}
all_scrappers['Wall Street Journal'] = None
all_scrappers['New York Times'] = None
all_scrappers['Financial Times'] = FTScrapingMachine()
all_scrappers['Les Echos'] = None

ScrappingConfig.scrap_article_boolean = True


for journal, urls in journals.items():
    for section, url in urls.items():
        print(journal, section, url)
        print(scrap(scrapper=all_scrappers[journal], journal=journal, section=section, url=url))
"""
print(scrap(scrapper=None, journal='New York Times', section='Economy', url='http://www.nytimes.com/pages/business/economy/index.html?src=busfn'))
"""