# Study Guide 11 - Polymorphism
## Activity 2

### 1. Questions

    a. "What is duck typing, as explained in the video?"
        Duck typing is another way to achieve polymorphism where an object must have the minimum necessary attributes and/or methods.

    b. "What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?"
        The Car class needed to have the same speak() method as the Dog and Cat classes in order to be part of the same loop.

### 2. Python Code
[Python Code for SG11: Polymorphism, Activity 2 Item 2](sg11_polymorphismAct2Code.py)

### 3. "How does the code in 2.2 demonstrate polymorphism?"

    This code demonstrates polymorphism by having all three classes share the same method name, but have their own unique output per class.