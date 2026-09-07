# SG4 - Understanding Classes and Objects

## Class Name: Enemy

## Class Description: Represents a very basic enemy character in a video game.

## Properties

| Property | Data Type | Description |
|---|---|---|
| name | string | The name of the enemy. |
| type | string | The category of the enemy. |
| rank | string | The significance or rank of the enemy. |
| health | int | The enemy's base health. |
| variant | string | A slight variation of the same enemy. |
| weight | string | The weight category of the enemy. |
| canInteractWith | list[string, string, string] | A list of environmental objects the enemy can interact with along with a corresponding action and effect. |

## Methods

| Method | Description |
|---|---|
| move(x speed: int, xdestination: float, ydestination: float, zdestination: float) | Makes the enemy move a certain speed towards a certain position. |
| attack(damage: int) | An attack that deals a certain amount of damage. |
| interact(target: canInteractWith[i]) | Interacts with a certain target via a specifc action to get a specific effect. |

## Class Diagram
![Class Diagram](images/classDiagram.png)

## Design Explanation

### Why did you choose this class?

### Which property is the most important? Why?

### Which method is the most useful? Why?
