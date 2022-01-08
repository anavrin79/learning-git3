class LibraryItem:
    def __init__(self, title, howmanytaken):
        self.title = title
        self.howmanytaken = howmanytaken

    
    def play(self, step=1):
        self.howmanytaken += step
        

class Movie(LibraryItem):
    def __init__(self, pubyear, gendre, *args, **kwargs):
        self.pubyear = pubyear
        self.gendre = gendre
        super().__init__(*args, **kwargs)
    
    def get_movies(self, title):
        self.title = title        
    
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
    
    def get_series(self, title):
        self.title = title        

    def printdata(self, episode, season):
        self.episode = episode
        self.season = season
        return(f'{self.title} S0{self.season} E0{self.episode}')    

    #@property
    def printdata(self, episode, season):
        self.episode = episode
        self.season = season
        return(f'{self.title} S0{self.season} E0{self.episode}')   

movies = list()

movies.append (Movie(title='Don\'t look up', pubyear='2021', gendre='catastrophic', howmanytaken=1))
movies.append (Movie(title='Frozen', pubyear='2012', gendre='comedy', howmanytaken=2))
movies.append (Movie(title='Blow up', pubyear='2001', gendre='drama', howmanytaken=3))


series1 = Series(title='Breaking Up',howmanytaken=1, episode=1,season=1)
series2 = Series(title='Korean series',howmanytaken=2, episode=2,season=1)
series3 = Series(title='Whatever',howmanytaken=3, episode=3,season=1)


print (movies[0].title)
Movie.play(movies[0])
Movie.play(movies[0])
Movie.play(movies[0])
print (movies[0].howmanytaken)

print (series1.title)
Movie.play(series1)
Movie.play(series1)
print (series1.howmanytaken)

print (Movie.printdata(movies[0], title='Don\'t look up'))
print (Movie.printdata(movies[1], title='Don\'t look up'))
print (Movie.printdata(movies[2], title='Don\'t look up'))
print (Series.printdata(series1, 1, 1))
