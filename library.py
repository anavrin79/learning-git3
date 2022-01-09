#spytac czemu nie dziala mi zeby wyswietlil tylko liste filmow albo tylko liste seriali ... (ostatni punkt zadania - dodatkowe)
#from typing import Counter
from pprint import pprint
import random
#pprint(the_list)

class LibraryItem:
    def __init__(self, title):
        self.title = title
        #self.howmanytaken = howmanytaken

    #variables
        self.howmanytaken = 0

    def play(self, step=1):
        self.howmanytaken += step

    def search(titlesearch, items):
        #print (titlesearch)
        matches = [p for p in items if titlesearch in p.title]

        for searchtitle in matches:
            print(f'{searchtitle.title}')
    
    def tentimes(items):
        for i in range(10):
            LibraryItem.generate_views(items)
        #LibraryItem.generate_views(items)
        #return

    def generate_views(items):
        chosen = random.randint(0,len(items)-1)
        chosenstep = random.randint(1,100)
        print (f'losowo: {items[chosen].title} ' )
        LibraryItem.play(items[chosen], step=chosenstep)
        print (f'{items[chosen].title} {items[chosen].howmanytaken}')

    def top_titles(items):

        newlist = sorted(items, key=lambda x: x.howmanytaken, reverse=True)

        #def switchfun(category):
        #    return {
        #        'Movie': print(f'{newlist[i].title} {newlist[i].pubyear} {newlist[i].gendre} {newlist[i].howmanytaken}'),
        #        'Series': print(f'{newlist[i].title} {newlist[i].season} {newlist[i].episode} {newlist[i].howmanytaken}')
        #    }[category]

        for i in range(len(newlist)):
            #print (items[i].title)

            #switchfun(category)

            if isinstance(newlist[i], Movie):
                #switchfun(category)
                print(f'{newlist[i].title} {newlist[i].pubyear} {newlist[i].gendre} {newlist[i].howmanytaken}')
            
            if isinstance(newlist[i], Series):
                print(f'{newlist[i].title} {newlist[i].season} {newlist[i].episode} {newlist[i].howmanytaken}')




class Movie(LibraryItem):
    def __init__(self, pubyear, gendre, *args, **kwargs):
        self.pubyear = pubyear
        self.gendre = gendre
        super().__init__(*args, **kwargs)
    
    def get_movies(items):
        counter = 0
        print ('Movies: ')
        
        for i in items:
            if isinstance(items[counter], Movie):
                print (items[counter].title)
            counter += 1
    
    def printdata(self, title):
        self.title = title
        return(f'{self.title} ({self.pubyear})')
    
    #@property
    def printdata(self, title):
        self.title = title
        return(f'{self.title} ({self.pubyear})')

class Series(LibraryItem):
    def __init__(self, episode, season, *args, **kwargs):
        self.episode = episode
        self.season = season
        super().__init__(*args, **kwargs)
    
    def get_series(items):
        counter = 0 
        print ('Series: ')
        for i in items:
            if isinstance(items[counter], Series):
                print (items[counter].title, items[counter].season, items[counter].episode)
            counter += 1

    def printdata(self, episode, season):
        self.episode = episode
        self.season = season
        return(f'{self.title} S0{self.season} E0{self.episode}')    

    #@property
    def printdata(self, episode, season):
        self.episode = episode
        self.season = season
        return(f'{self.title} S0{self.season} E0{self.episode}')   

items = list()

items.append (Movie(title='Don\'t look up', pubyear='2021', gendre='catastrophic'))
items.append (Movie(title='Frozen', pubyear='2012', gendre='comedy'))
items.append (Movie(title='Blow up', pubyear='2001', gendre='drama'))


items.append (Series(title='Breaking Up', episode=1,season=1))
items.append (Series(title='Korean series', episode=2,season=1))
items.append (Series(title='Whatever', episode=3,season=1))

#def myFunc(e):
#  return e['title']
#
#items.sort(key=myFunc)

#print (movies[0].title)
Movie.play(items[0])
Movie.play(items[0])
Movie.play(items[0])
#print (items[0].howmanytaken)

#print (series1.title)
Movie.play(items[0])
Movie.play(items[0])

#print (Movie.printdata(items[0], title='Don\'t look up'))
#print (Movie.printdata(items[1], title='Frozen'))
#print (Movie.printdata(items[2], title='Blow up'))
#print (Series.printdata(items[0], 1, 1))


#Movie.get_movies(Movie.movies, movies)
Movie.get_movies(items)
Series.get_series(items)

#pprint (items)
#print(list(items))

LibraryItem.search('ore', items)

LibraryItem.generate_views(items)

LibraryItem.tentimes(items)

LibraryItem.top_titles(items)