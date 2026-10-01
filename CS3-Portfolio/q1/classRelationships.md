# Class Relationships: Association and Multiplicity

## Previous Work

[Part I - Classes and Objects](classObjectUML.md)

[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class

Class: Enemy Character

Description: An enemy character to fight in a video game context.

## New Related Class

Class: Hero Character

Description: A hero character that will fight the enemy characters.

## Association

Relationship: Enemy fights Hero.

Explanation: Logically, enemy characters fight the hero character and the hero fights the enemies.

## Multiplicity

Multiplicity: 1

Explanation: Enemies can only target a single hero at a time. Otherwise, enemies may target no one or in an uncoordinated manner target multiple people.

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](images/relationshipTestRun.png)

## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)

## Analysis

### What is the association between your two classes?


### What multiplicity did you choose and why?


### How did you implement the relationship in Python?


### Why did you store an object reference instead of copying its data?


### If your relationship uses many, why is a list appropriate?
