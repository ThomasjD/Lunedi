#Write code to
class Person(object):
    def __init__(self, name, email, phone, friends, greetings_count, unique_greetings):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends 
        self.greetings_count = greetings_count
        self.unique_greetings = unique_greetings

    def greet(self, other_person): 
        print (f'Hello {other_person.name}, I am {self.name}!')
        if other_person.name not in self.unique_greetings:
            self.unique_greetings.append(other_person.name)
        else:
            self.greetings_count += 1

    def print_contact_info(self):
        print(f'{self.name}\'s email: {self.email}, {self.name}\'s phone:{self.phone}')

    def add_friends(self, friends):
        self.friends.append(friends)

    def num_friends(self):
        return len(self.friends)

    def __repr__(self):
        return '' % (self.name, self.email, self.phone)

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948', friends = [], greetings_count= 0, unique_greetings= [])
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456', friends = [], greetings_count= 0, unique_greetings= [])

print(f'{sonny.name} email is {sonny.email} and phone # is {sonny.phone}')
print(f'{jordan.name} email is {jordan.email} and phone # is {jordan.phone}')

sonny.print_contact_info()

#jordan.friends.append('sonny')
jordan.add_friends('sonny')

#sonny.friends.append('jordan')
sonny.add_friends('jordan')
sonny.greet(jordan)
jordan.greet(sonny)
jordan.greet(sonny)

print (sonny.friends)
print (jordan.friends)

#print(len(jordan.friends))
print(jordan.num_friends())

print (f'sonny greetings count is {sonny.greetings_count}')
#Make your own class

print (f'Jordan has {jordan.greetings_count} unique greetings')
print (f'Sonny has {sonny.greetings_count} unique greetings')
print (len(jordan.unique_greetings))
print (len(sonny.unique_greetings))



#Create a class Vehicle. A Vehicle object will have 3 attributes:
class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print(f'{self.year} {self.make} {self.model}')
    
car = Vehicle('Nissan', 'Leaf', 2015)
print (car.make)

car.print_info()

