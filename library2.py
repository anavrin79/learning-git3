import random


class LibraryItem:
    def __init__(self, title):
        self.title = title

    # variables
        self.howmanytaken = 0

    def play(self, step=1):
        self.howmanytaken += step

    def search(titlesearch, items):
        matches = [p for p in items if titlesearch in p.title]

        for searchtitle in matches:
            print(f'{searchtitle.title}')

    def tentimes(items):
        for i in range(10):
            LibraryItem.generate_views(items)

    def generate_views(items):
        chosen = random.randint(0, len(items) - 1)
        chosenstep = random.randint(1, 100)
        print(f'losowo: {items[chosen].title} ')
        LibraryItem.play(items[chosen], step=chosenstep)
        print(f'{items[chosen].title} {items[chosen].howmanytaken}')

    def top_titles(items, title_type):
        newlist = sorted(items, key=lambda x: x.howmanytaken, reverse=True)
        for i in range(len(newlist)):
            if isinstance(newlist[i], title_type):
                print(newlist[i])


class Movie(LibraryItem):
    def __init__(self, pubyear, gendre, *args, **kwargs):
        self.pubyear = pubyear
        self.gendre = gendre
        super().__init__(*args, **kwargs)

    def get_movies(items):
        counter = 0
        print('Movies: ')

        for i in items:
            if isinstance(items[counter], Movie):
                print(items[counter].title)
            counter += 1

    def printdata(self, title):
        self.title = title
        return(f'{self.title} ({self.pubyear})')

    # @property
    def printdata(self, title):
        self.title = title
        return(f'{self.title} ({self.pubyear})')

    def __str__(self):
        return f'{self.title} {self.pubyear} {self.gendre} {self.howmanytaken}'


class Series(LibraryItem):
    def __init__(self, episode, season, *args, **kwargs):
        self.episode = episode
        self.season = season
        super().__init__(*args, **kwargs)

    def get_series(items):
        counter = 0
        print('Series: ')
        for i in items:
            if isinstance(items[counter], Series):
                print(
                    items[counter].title,
                    items[counter].season,
                    items[counter].episode)
            counter += 1

    def printdata(self, episode, season):
        self.episode = episode
        self.season = season
        return(f'{self.title} S0{self.season} E0{self.episode}')

    def __str__(self):
        return f'{self.title} {self.season} {self.episode} {self.howmanytaken}'

    # @property
    def printdata(self, episode, season):
        self.episode = episode
        self.season = season
        return(f'{self.title} S0{self.season} E0{self.episode}')


items = list()

items.append(
    Movie(
        title='Don\'t look up',
        pubyear='2021',
        gendre='catastrophic'))
items.append(Movie(title='Frozen', pubyear='2012', gendre='comedy'))
items.append(Movie(title='Blow up', pubyear='2001', gendre='drama'))


items.append(Series(title='Breaking Up', episode=1, season=1))
items.append(Series(title='Korean series', episode=2, season=1))
items.append(Series(title='Whatever', episode=3, season=1))

Movie.play(items[0])
Movie.play(items[0])
Movie.play(items[0])
Movie.play(items[0])
Movie.play(items[0])

Movie.get_movies(items)
Series.get_series(items)

LibraryItem.search('ore', items)

LibraryItem.generate_views(items)

LibraryItem.tentimes(items)

LibraryItem.top_titles(items, Series)  # albo Movie
