### **Annex B**

### **Computational Thinking Exercise: "Smart Vending Machine"**

**Section: 9- Platinum______________________Score:____________**

**C\# / Name: Simon Bernard A. Andaya________ Date: 12/08/26____**

**Scenario**  
Your school installs a vending machine to provide snacks and drinks. However, students encounter several issues:

* Sometimes the machine does not give the correct change.  
  * Items run out, but the machine doesn’t notify anyone.  
  * Students press the wrong buttons and get the wrong item.  
  * The machine is slow when multiple students use it in succession.

Your task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

**Step 1: Identify the Big Problem**  
Main Problem: The software has difficulty in handling transactions and identifying the remaining stock. Then when a line is formed, this puts more stress on the software, causing it to slow down _________________________

**Step 2: Identify three to four Sub-Problems**  
Please list possible sub-problems:

1. It encounters problems in calculating the change to be given__________  

2. It does not update the number of products left properly______________  

3. The software is stressed when handling multiple transactions__________  

**Step 3: Define Computational Thinking Approaches**  
For each sub-problem, apply CT skills:

| Calculating problems | Abstraction | Simplify the software, so that it can focus properly on the orders |
| Product Updating | Algorithm Design | Create a trigger than when triggered, adds or subtracts the amount of product left |
| Multiple Transactions | Abstraction | When the transaction is done, update the products and ignore any other commands, except for starting a new order |

**Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem**

**Step 1: Calculating Problems**  
**Selected Sub-Problem**  
Make the correct  
**Pseudocode**  
START  
Display all available choices  
Ask the user for an input  
Ask the user if they would like to make another input  
IF user enters Y THEN  
	Repeat step 2  
ELSE  
	Calculate the total amount of all items  
Display the output  
END