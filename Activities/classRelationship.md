# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Restaurant
Description: Has 4 attributes namely, Restaurant Name, Amount of Stock, Location, and Open. And has 4 methods, Closing, Serving, Checking Stock, and Updating Stock
## New Related Class
Class: Staff
Description: I want this class to have 4 attributes, Name, Age, Profession, and Rating. And 4 methods, Serving, Cleaning, Closing, Stocking.
## Association
Relationship: Restaurant has Staff. The Staff manages the Restaurant, and the Staff can be assigned to tasks within the Restaurant.
Explanation: This is because the Staff is needed tp make the Restaurant functional. Without the Staff, the Restaurant cannot do anything.
## Multiplicity
Multiplicity: 1..*
Explanation: A restaurant can be run by one person(though very rare), or by multiple people.
## UML Class Relationship Diagram
![Class Relationship Diagram](image-4.png)
## Python Implementation
[View Python Source](classRelationship.py)
## Test Run
![Relationship Test Run](image-5.png)
## Object Relationship Diagram
![Object Relationship Diagram](image-6.png)
## Analysis
### The association between my two classes, is that a Restaurant has Staff. The Restaurant needs the Staff to function properly, and vice vresa. 
### The multiplicity that I chose is one or more. This is because the Restaurant can have only one or more Staff  working in it. There are multiple different reasons, why this is, so I will leave it at that.
### I implemented this relationship in python, by following the instrucion given, and searching it up on the internet. I followed the way a youtuber did their code, and applied it on my own code. This resulted in me getting my present code.
### I stored an object refrence instead of copying it to make my life easier. You could just refer to the object reference once again, to get your wanted output. This is significantly easier than copying it, because it is less time consuming and easier to code.
### A list is appropriate, since you could refer to an object in the list. And since the list can contain the many that you need to define.
