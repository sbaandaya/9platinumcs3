# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)
## Existing System Description:
## Inheritance Relationship
Parent: ElectronicDevice
Child: Computer
Explanation: I choose ElectronicDevice as the parent class, because it is an umbrella term. Under this, a child class could be a cellphone, a laptop, or a computer. I picked Computer, since it is the first thing that came into my mind when talking about an electronic device.
## Inheritance UML
[Inheritance](image-7.png)
## Composition/Aggregation
Relationship: Composition
Explanation: Since if we we're to remove the object Motherboard, or the class Computer, both of them would disappear.
## Advanced UML Diagram
[Advanced UML](image-8.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
[Test](image-9.png)
## Object Diagram
[Objects](image-10.png)

## Reflection
Answers:
1. I choose inheritance relatioship because it makes coding easier. My child class ia a type of my chosen parent class, becuase my parent class is an umbrella term. When checking the umbrella term, this child class is under it.
2. Inheritance reduced duplicate code by reusing original parent code. By using the "super().__init()". Attributes and methods that were reused is the Hardware, Software, and Action.
3. My HAS-A relationship is composition. This is because they both need each other. The life-cycle between the two is simple.
4. There is much difference between them. I believe that both of them just place common code into one place, and call. This works in both association, and the advance relationships.
5. My design follows the DRY prinicple, by placing common attributes in the parent class. THis makes it easier to call them in the child class. THis makes the code cleaner and shorter.