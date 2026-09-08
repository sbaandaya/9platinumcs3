# Class Attributes and Methods
## Previous Design
Link to my previous activity:
(classObjectUML.md)
## Design Revision
No major changes were needed from my original design.## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|Restaurant Name|String|Public|The restaurant name is public, since they need to identify what restaurant they are going to, and where it is located.|
|Amount of stock|Int|Private|The customer doesn’t need to know this, since they are only here to order, eat, pay and leave.|
|Open|Boolean|Public|To know if they would still be served or not when they come to the restaurant.|
|Location|String|Public|To know where they should go in order to find their wanted restaurant.|
## Updated UML Class Diagram
![Class Diagram](image.png)
## Python Implementation
#No image regarding this was ever said.
## Test Run
![Test Run](image-2.png)
## Object Diagram
![Obejct Diagram](image-3.png)
## Analysis
### I made my chosen attributes private, because of abstraction. The customers only need to order, get served and leave, not know how much stock is left. Nothing would go wrong if other parts of the program could interact with this, since this function needs an Int to function, not a String. But if something did go wrong, it would possibly be the checking the amount of stock, that made a mistake.
### The method that changes the state of my object, is updating the amount of stock. This could add or subtract any new amount to the remaining amount of stock. The attribute affected by this is amount of stock, and it could be added or subtracted.
### My two objects demonstrate that instances are independent, because when I updated the amount of stock, only Restaurant 1 hd an update. This is because I refered to it as restaurant1, not restaurant2, this signals the system what to change, and not change.
### The difference between the two diagrams, is that the object diagram has a constructor. The constructor is needed to create objects that uses inheritance to create their attributes, and methods. Without a constructor, no objects can be made from the class.