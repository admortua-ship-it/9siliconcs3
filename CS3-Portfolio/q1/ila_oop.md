# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation can be applied in the inventory system by grouping different variables of data and many methods of using them into a singular object. For example, an item in stock having the metadata of an item class containing name, price, and supply, and the different processes that manage them. In terms of organization, a specific inventory action will change the remaining supply or another variable instead of letting every part of the program change it randomly.

### 2. Abstraction
Abstraction can be used by removing or hiding unnecessary details or data needed, helping users use something without knowing how it works, but knowing what it does. In terms of an inventory system, simple actions such as adding or selling a product or adjusting the price will be provided rather than letting the users know how it works on the inside. This helps guide users in using the system because they only need a simpler interface hiding the complicated processes.

### 3. Inheritance
Inheritance can be used by introducing a broad, general category containing all the necessary information, and then branching it into many sub-categories and introduce their own data but still keep the parent category's characteristics. Moreover, it helps reuse existing functions in product types instead of simply repeating it. For example, a general Product type having the core properties, and sub-categories Food, Clothing, Electronics, and others, inherit Product's core properties but contain information unique to them.

### 4. Polymorphism
Polymorphism in terms of inventory systems can have the same inventory action make different product types or categories respond differently. A system using polymorphism takes less effort to operate because a common interface is required to simply change data in different products in unique manners. For example, a specific action calculating the storage or supply requirement will have different product types like food or hygiene items respond differently.

## Reflection
The pillar of Object-Oriented Programming most useful for improving the sari-sari store inventory system is **inheritance**. Inheritance can be used by putting core properties in a broad parent category like Product and then pass those properties down to sub-categories like Food, Hygiene, and School/Office Supplies with their own properties unique to them alongside the core ones and/or override some of them. This is useful for improving the system because it avoids repetition in having to define every data in every product category by having the common features defined only ones while the child classes can reuse, add, or override those features. Inheritance also allows room for future sub-categories for products because the first step simply takes building them based on the general Product's properties instead of making them from scratch.
