# zapyta Mentora czy o to chodzi w cwiczeniu 7.1 ?
# czy zmienna cards ma być obiektem, który ma 5 roznych wartosci?

from faker import Faker
fake = Faker()


class businesscard:
    def __init__(self, name, lastname, email):
        self.name = name
        self.lastname = lastname
        self.email = email

cards = []

for i in range(5):
    cards = (businesscard(name=fake.name(),
             lastname=fake.name(), email=fake.email()))
    print (cards.name.split(sep=" ", maxsplit=1)[0],
           cards.lastname.split(sep=" ", maxsplit=2)[1], cards.email)
