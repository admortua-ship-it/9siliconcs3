# Advanced Class Relationships

## Previous Activities

[classAttrib](classAttributesMethods.md)

[classRel](classRelationships.md)


## Existing System Description:

## Inheritance Relationship

Parent: Enemy

Child: BossEnemy

Explanation: A BossEnemy child is a type of the parent Enemy because BossEnemy would be a more complex and specialized form of Enemy.

## Inheritance UML

![Inheritance](images/inheritanceDiagram.png)


## Composition/Aggregation

Relationship: Aggregation

Explanation: With BossEnemy being a more complex an special form of Enemy, a BossEnemy can still exist without an Enemy.


## Advanced UML Diagram

![Advanced UML](images/advancedClassDiagram.png)

## Python Implementation

[Source Code](advancedRelationships.py)

## Test Run

![Test](images/advancedTestRun.png)

## Object Diagram

![Objects](images/advancedObjectDiagram.png)


## Reflection

Answers:

1. ) I chose this inheritence relationship of making BossEnemy a child class of parent class Enemy. This is because BossEnemy would imply a more complex and specialized form of enemy. Thus, BossEnemy will inherit features from Enemy and introduce its own attributes and methods.
2. ) Inheritance reduced duplicate code by defining the code once and letting other objects use it. The attributes reused were name, type, allyType, rivalType, health, damage, position, speed, range, alliesInSamePos, rivalsInSamePos, accuracy, isLeader, otherLeadersInSamePos, synergyChance. The methods reused were move, basicAttack, typeSynergy, takeDamage, stepAside, and death.
3. ) My HAS-A relationship is Aggregation. It means the child object contained within the parent can still exist without the parent. For this system, it allows the BossEnemy to be independent from the normal Enemy while still being related to it.
4. ) Association followed with two related classes. Meanwhile, the advanced relationship created another class from a parent class without creating a new class altogether. This relationship can be a faster way to form related classes better than classes associated with it.
5. ) This design follows the DRY principle by Inheritance and Aggregation. By Inheritance, it simple reuses code from the parent class. By Aggregation, it allows independence from the parent class while still being related.