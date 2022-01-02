class BussCard:

    def __init__(self, fullname, cnumber, email):
        self.fullname = fullname
        self.cnumber = cnumber
        self.email = email

    def __str__(self):
        return f'{self.fullname}, {self.cnumber}, {self.email}'

    def contact(self, fullname):
        self.fullname = fullname
        return f'Kontaktuje sie z : {self.fullname}'

    @property
    def fullname_lenght(self):
        return len(self.fullname)

card1 = BussCard(fullname="Jan Kowalski", cnumber="+48 660 406 953", email="jkowalski@gmail.com")
card2 = BussCard(fullname="Jan Twardowski", cnumber="+48 661 406 953", email="jtwardowski@gmail.com")
card3 = BussCard(fullname="Marian Topolski", cnumber="+48 662 406 953", email="mtopolski@gmail.com")
card4 = BussCard(fullname="Henryk Bolo", cnumber="+48 663 406 953", email="hbolo@gmail.com")

print (card1.fullname)


BussCard.contact(fullname=card1.fullname)

