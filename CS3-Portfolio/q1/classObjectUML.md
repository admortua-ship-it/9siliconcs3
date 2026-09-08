# SG4 - Understanding Classes and Objects

## Class Name: Enemy Character

## Class Description: Represents a very basic enemy character in a video game.

## Properties

| Property | Data Type | Description |
|---|---|---|
| name | string | The name of the enemy. |
| type | string | The category of the enemy. |
| allyType | string | The enemy's preferred ally type other than themselves. |
| rivalType | string | The enemy's rival type. |
| health | int | The enemy's base health. |
| damage | int | The enemy's maximum damage it can inflict on the hero. |
| position | int | The enemy's position. |
| speed | int | The enemy's maximum units it can move forward or backward. |
| range | int | The enemy's required distance from the hero to execute an attack or team attack. |
| alliesInSamePos | int | Other enemies of similar or synergy-compatible type in the same position as them. |
| rivalsInSamePos | int | Other enemies of synergy-incompatible type in the same position as them. |
| accuracy | int | Base chance of hitting the hero or doing friendly fire with other enemies. |

## Methods

| Method | Description |
|---|---|
| move(position: int, speed: int) | Makes the enemy move a certain units forward or backward. |
| attack(damage: int, accuracy: int, range: int) | An attack that deals a certain amount of damage to the hero or unintentionally another enemy if it reaches a certain range. |
| takeDamage(health: int, damage: int, position: int, range: int) | Takes a certain form of damage when hit within a certain range requirement. |
| typeSynergy(damage: int, type: string, allyType: string, rivalType: string, position: int, range: int, alliesInSamePos: int, rivalsInSamePos: int) | A complex action that makes the enemy look for synergy-compatible and synergy-incompatible to deliver a more powerful or weaker combined attack based on how many allies or rivals it found. |

## Class Diagram
![Class Diagram](images/classDiagram.png)

## Design Explanation

### Why did you choose this class?

### Which property is the most important? Why?

### Which method is the most useful? Why?
