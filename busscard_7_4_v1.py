
from faker import Faker
fake = Faker("pl_PL")
 
class BaseContact:
    def __init__(self, first_name, last_name, email_address,tel_priv):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.tel_priv = tel_priv
         
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email_address}"
 
    def __repr__(self):
        return f"Card(first_name={self.first_name} last_name={self.last_name}, adres email={self.email_address})"
 
    def contact(self):
        return f"Choose home phone: {self.tel_priv} and call to {self.first_name} {self.last_name} "
     
     
    @property
    def label_lenght(self):
        return sum([len(self.first_name), len(self.last_name),+1])     
     
 
class BusinessContact(BaseContact):
    def __init__(self, tel_work, company, occupation, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tel_work = tel_work
        self.company = company
        self.occupation = occupation
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email_address}, {self.occupation}, {self.company}, {self.tel_work}"
 
    def __repr__(self):
        return f"Card(first_name={self.first_name} last_name={self.last_name}, adres email={self.email_address})"

    def workcontact(self):
        return f"Choose work phone: {self.tel_work} and call to {self.first_name} {self.last_name}"

def create_contacts(kind, how_many):

    contacts = []
    for i in range(how_many):
        if kind == 'b':
            contacts.append(BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), occupation=fake.job(),email_address=fake.email(), tel_priv=fake.phone_number(), tel_work=fake.phone_number()))
        elif kind == 'h':
            contacts.append(BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), email_address=fake.email(), tel_priv=fake.phone_number()))
    return contacts


#human_1 = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), occupation=fake.job(),email_address=fake.email(), tel_priv=fake.phone_number(), tel_work=fake.phone_number())
#print(human_1)
#print(human_1.contact())
#print(human_1.workcontact())
#print(human_1.label_lenght)
#print()


kind = input("select the type of business card: b - business, h - home: ")
how_many = int(input('please select number of cards '))
contacts = create_contacts(kind, how_many)

print (contacts)
card1 = create_contacts(kind, how_many)
BusinessContact.workcontact(card1)

