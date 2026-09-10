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
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### The association between my two classes, is that a Restaurant has Staff.
### The multiplicity that I chose is one or more. 
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?
