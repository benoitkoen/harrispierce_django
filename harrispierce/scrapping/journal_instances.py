from harrispierce.scrapping.scrap_urls import journals

journal_list = []


class Journal:
    def __init__(self, name, urls):
        self.name = name
        self.urls = urls


for name, urls in journals.items():
    journal_list.append(Journal(name, urls))

