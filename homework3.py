
class Person :
    def __init__(self, name):
        self.name = name
        self.contacts = []

    def __repr__(self) :
        return self.name

    def printContacts(self):
        print(self.name + " has been in contact with " + " ".join(self.contacts))


## Task 1: Given a filename, read in the list of contacts and construct a list of Person objects.
## Each Person object should contain:
##    A name
##    A list of strings that represent their contacts.
## So, if a line contains "Carol,Mark,Leanne", you should create a Person with name='Carol' and
##     contacts=['Mark','Leanne']


def load_persons(filename) :
    list_of_people = []
    with open(filename) as f:
       ## you do this part.
    return list_of_people

## Task 2: Given a list of Persons, print out each Person's name and contacts using the printContacts method.

def print_all_contacts(people_list) :
    pass

## Task 3: Given a list of Persons, find all the 'patient zeros' - that is, those Persons who are not in anyone's contact list.
# They're possibly the the people who started this!
    
def find_patient_zeros(list_of_people) :
    zeros = []
    ## you do this part.
    return zeros
    
## Task 4: Given a list of Persons, find the potential zombies. We should isolate them immediately!
## a potential zombie is someone who has been listed as a contact, but doesn't show up as a zombie.

def find_potential_zombies(list_of_people) :
    potentialZombies = []
    ## you do this part.
    return potentialZombies

## Task 5. Given a list of Persons, find the most viral Persons. We should get them to stay home!
## the most viral people are those who have the most contacts.
def most_viral(list_of_people) :
    ## you do this part.


    return longest

## Task 6. Given a list of Persons, find the most contacted Person. They could be the next to spread the infection!
# The most contacted is the person who appears in the most lists.

def most_contacted(list_of_people) :
    ## you do this part
    pass

## Task 7. Given a list of Persons and a name, determine whether the person with that name should get treated.
# They should get treated if they are in any of the close contact lists.

def should_get_treated(people_list, name) :
    ## you do this part
    pass

## Task 8. Write a main that demonstrates each of your tasks.

if __name__=='__main__' :
    fname = input("Please enter the name of the zombie file: ")
    people_list = load_persons(fname)
    ## you do the rest.



