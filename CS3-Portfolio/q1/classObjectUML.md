# SG4 - Understanding Classes and Objects

## Class Name: Enemy Character

## Class Description: Represents a very basic enemy character in a video game.

## Properties

| Property | Data Type | Description |
|---|---|---|
| name | string | The name of the enemy. |
| health | int | The enemy's base health. |
| type | string | The category of the enemy. |
| allyType | string | The enemy's preferred ally type other than themselves. |
| rivalType | string | The enemy's rival type. |
| position | int | The enemy's position. |
| alliesInSamePos | int | Other enemies of similar or synergy-compatible type in the same position as them. |
| rivalsInSamePos | int | Other enemies of synergy-incompatible type in the same position as them. |
| speed | int | The enemy's maximum units it can move forward or backward. |
| range | int | The enemy's required distance from the hero to execute an attack or team attack. |
| damage | int | The enemy's maximum damage it can inflict on the hero. |
| accuracy | int | Base chance of hitting the hero or doing friendly fire with other enemies. |
| isLeader | boolean | Dictates if an enemy is elegible for initiating a synergy attack. |
| otherLeadersInSamePos | boolean | Looks for if there are more than one leader enemies are standing in the same position as them. |
| synergyChance | int | Base chance of leader enemy attempting to initiate a synergy attack. |

## Methods

| Method | Description |
|---|---|
| move(position: int, speed: int) | Makes the enemy move a certain units forward or backward. |
| basicAttack(damage: int, accuracy: int, range: int) | A basic attack that deals a certain amount of damage to the hero or unintentionally another enemy if it reaches a certain range. |
| takeDamage(health: int, damage: int, position: int, range: int) | Takes a certain form of damage when hit within a certain range requirement. |
| typeSynergy(damage: int, type: string, allyType: string, rivalType: string, position: int, range: int, alliesInSamePos: int, rivalsInSamePos: int, isLeader: boolean, otherLeadersInSamePos synergyChance: int) | A complex action that makes a leader enemy look for synergy-compatible and synergy-incompatible to deliver a more powerful or weaker combined attack based on how many allies or rivals it found. |
| stepAside(position: int, isLeader: boolean, otherLeadersInSamePos: boolean) | Makes leader enemy avoid being in the same spot as another leader by moving a random number of units forward or backward below or equal to base speed. |


## Class Diagram
![Class Diagram](images/classDiagram.png)

## Design Explanation

### Why did you choose this class?
I chose this class because it takes the least effort to apply the context of a video game, specifically one of its core aspects being the enemies.

### Which property is the most important? Why?
The type property, because it serves as the core component on the class's most complex method being the typeSynergy method.

### Which method is the most useful? Why?
The move method because it is fundamental to the enemy because it needs to move around, besides the basicAttack method in what the enemy will do.

## Design Revision:
Changes from my previous design:
- Organized the properties in the class diagram for cleanliness.