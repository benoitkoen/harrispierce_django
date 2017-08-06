

WSJUrls = {
    "World": "https://www.wsj.com/news/world",
    "Economy": "https://www.wsj.com/news/economy",
    "Companies": "https://www.wsj.com/news/business",
    "Politics": "https://www.wsj.com/news/politics",
    "Tech": "https://www.wsj.com/news/technology",
    "Opinion": "https://www.wsj.com/news/opinion"
}

NYTUrls = {
    "World": "https://www.nytimes.com/section/world",
    "Economy": "http://www.nytimes.com/pages/business/economy/index.html?src=busfn",
    "Dealbook": "http://www.nytimes.com/pages/business/dealbook/index.html?src=busfn",
    "Politics": "https://www.nytimes.com/pages/politics/index.html",
    "Tech": "https://www.nytimes.com/section/technology",
    "Energy": "http://www.nytimes.com/pages/business/energy-environment/index.html?src=busfn"
}

FTUrls = {
    "World": "http://ft.com/world",
    "Companies": "http://ft.com/companies",
    "Markets": "http://ft.com/markets",
    "Opinion": "https://www.ft.com/opinion",
    "Careers": "https://www.ft.com/work-careers"
}

lesEchosUrls = {
    "World": "http://www.lesechos.fr/monde/index.php",
    "Economy": "http://www.lesechos.fr/economie-france/index.php",
    "Markets": "http://www.lesechos.fr/finance-marches/index.php",
    "Politics": "http://www.lesechos.fr/politique-societe/index.php",
    "Tech": "http://www.lesechos.fr/tech-medias/index.php",
}


journals = {'Wall Street Journal': WSJUrls,
            'New York Times': NYTUrls,
            'Financial Times': FTUrls,
            'Les Echos': lesEchosUrls}


journalPrimaryKeys = {
    'Wall Street Journal': 1,
    'New York Times': 3,
    'Financial Times': 2,
    'Les Echos': 4
}

"""
j1 = Journal(name = 'Wall Street Journal', country = 'US')
j1.save()
s1 = j1.sections.create(name = 'World')
s2 = j1.sections.create(name = 'Economy')
s3 = j1.sections.create(name = 'Dealbook')
s4 = j1.sections.create(name = 'Politics')
s5 = j1.sections.create(name = 'Tech')
s6 = j1.sections.create(name = 'Opinion')

j2 = Journal(name = 'New York Times', country = 'US')
j2.save()
s7 = j2.sections.create(name = 'World')
s8 = j2.sections.create(name = 'Economy')
s9 = j2.sections.create(name = 'Companies')
s10 = j2.sections.create(name = 'Politics')
s11 = j2.sections.create(name = 'Tech')
s12 = j2.sections.create(name = 'Energy')

j3 = Journal(name = 'Financial Times', country = 'US')
j3.save()
s13 = j3.sections.create(name = 'World')
s14 = j3.sections.create(name = 'Comapnies')
s15 = j3.sections.create(name = 'Markets')
s16 = j3.sections.create(name = 'Opinion')
s17 = j3.sections.create(name = 'Careers')

j4 = Journal(name = 'Les Echos', country = 'France')
j4.save()
s18 = j4.sections.create(name = 'World')
s19 = j4.sections.create(name = 'Economy')
s20 = j4.sections.create(name = 'Markets')
s21 = j4.sections.create(name = 'Politics')
s22 = j4.sections.create(name = 'Tech')
"""