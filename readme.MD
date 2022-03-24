#### Homework #3 Zombie Attack.

#### Due Tuesday, April 5, 2:40 pm

This assignment will be graded using specifications grading.
To get a C, complete tasks 1-4. To get a B, complete tasks 1-7. To get an A, complete all tasks.

To submit your work, please push it back up to your GitHub repo by the deadline. 

In this homework, you'll be implementing a contact tracing tool to help USF manage the latest zombie outbreak. We want to be able to identify students who have become or are at risk of becoming zombies so that we can get them the treatment they need. (luckily, it turns out that becoming a zombie is fully reversible.)


#### Task 1: 
To begin, we need to read in our data. I've provided three sample data files for you.

Our data is in the format:
<pre>
Zombie, Contact1, Contact2, ...
</pre>
The name in the 'Zombie' slot has been identified as a zombie. The names in the Contact slots are students they had close contact with - they may or may not be zombies also!

We'll store each row as a Person object. This is already implemented for you - you just need to use it. A Person has two member variables:
- name (a string)
- contacts (a list of strings)

You should implement the load_persons function. It should take as input a filename, open that file, read in each line, and for each line create a Person.
Store the Persons in the list_of_people list, and return that at the end of your function.


#### Task 2. 
Let's start by generating a list of all the zombies and their contacts. Implement print_all_contacts. 
It should take as input a list of Persons and loop through that list, calling printContacts() for each Person.

#### Task 3. 
We need to figure out who might have started this outbreak! We'll call them 'patient zeros.' They're the people who are zombies, but aren't listed as anyone's contact.

Implement find_patient_zeros. It should take as input a list of Persons and return a list of all Persons that don't appear in anyone's contact list.

##### Task 4. 
We need to keep this from spreading further! Let's identify potential zombies so that we can treat and isolate them.

A potential zombie is someone who's listed as a contact, but is not currently known to be a zombie.

Implement the function find_potential_zombies. Given a list of Persons, it should return a list containing those persons who are potential zombies.

#### Task 5. 
Maybe if we can identify the super-spreaders, we can get this under control! Let's identify the most viral person.
The most viral Person is the Person with the most contacts. 

Implement most_viral. Given a list of Persons, return the Person with the longest list of contacts. (you may choose how to deal with ties.)

#### Task 6. 

People who've been repeatedly exposed are particularly likely to become zombies. We need to find those people who've had the most contacts.

Implement most_contacted. Given a list of Persons, find the name that appears in the most contact lists.

#### Task 7. 
We need to screen people and see whether they need treatment or not.

Implement should_get_treated. Given a list of Persons and a name, return True if that person is either a zombie or a contact,
and False otherwise.

#### Task 8. 
Let's wrap it up! Add a main function that tests each of your tasks.