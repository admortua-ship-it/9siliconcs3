# Computational Thinking Exercise

## Smart Vending Machine

**Name:** Achilles David M. Ortua

**Section:** Silicon

**Last Name:** Ortua

**Date:** 08/17/26

---

## Step 1: Identify the Big Problem

### Main Problem

The main problem is that the vending machine often fails to perform several functions.

---

## Step 2: Identify the Sub-Problems

1. The machine may sometimes give the wrong change.
2. The machine does not notify anyone if items run out.
3. The machine sometimes outputs the wrong item.
4. The machine slows when multiple students use it in succession.

## Step 3: Apply Computational Thinking Skills

| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| The machine may sometimes give the wrong change. | Algorithmic thinking | The machine will follow a simple formula that calculates the difference between how much the item costs and how much did the user pay. |
| The machine does not notify anyone if items run out. | Algorithmic thinking | The machine will update and first check if it has at least one of that item, otherwise it will explicitly notify that the item is unavailable. |
| The machine sometimes outputs the wrong item. | Decomposition | The machine will split an item into many smaller data points only relevant to the function, such as position in the vending machine, and have its physical mechanisms improved. |
| The machine slows when multiple students use it in succession. | Decomposition and Abstraction | The machine divides a large queue into smaller queue slots easier to focus on. Additionally, the machine's hardware will be optimized to be at its fastest if the decomposition wasn't enough. |

---

## Step 4: Algorithmic Solution

### Selected Sub-Problem

The machine may sometimes give the wrong change.

### Pseudocode

START

stock = [items and cost]

item_choice = stock[input(given number)]

get cost_item from item_choice in stock[given number]

user_payment = input(ask user for payment)

change = user_payment - item_choice(cost_item)

give change

END

---

