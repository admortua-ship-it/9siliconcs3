import random

class Enemy_Character:
    def __init__(self, name, type, allyType, rivalType, health, damage, position, speed, range, alliesInSamePos, rivalsInSamePos, accuracy, isLeader, otherLeadersInSamePos, synergyChance):
        self.__name = str(name)
        self.__type = str(type)
        self.__allyType = str(allyType)
        self.__rivalType = str(rivalType)
        self.__health = int(health)
        self.__damage = int(damage)
        self.__position = int(position)
        self.__speed = int(speed)
        self.__range = int(range)
        self.__alliesInSamePos = int(alliesInSamePos)
        self.__rivalsInSamePos = int(rivalsInSamePos)
        self.__accuracy = int(accuracy)
        self.__isLeader = bool(isLeader)
        self.__otherLeadersInSamePos = bool(otherLeadersInSamePos)
        self.__synergyChance = int(synergyChance)
        self.__neighbors = []

    def addNeighbor(self, Enemy_Character):
        self.__neighbors.append(Enemy_Character)

    def enemyInfo(self):
            print("Name: " + self.__name)
            print("Type: " + self.__type)
            print("Ally Type: " + self.__allyType)
            print("Rival Type: " + self.__rivalType)
            print("Health: " + str(self.__health))
            print("Damage: " + str(self.__damage))
            print("Position: " + str(self.__position))
            print("Speed: " + str(self.__speed))
            print("Range: " + str(self.__range))
            print("Allies in Same Position: " + str(self.__alliesInSamePos))
            print("Rivals in Same Position: " + str(self.__rivalsInSamePos))
            print("Accuracy: " + str(self.__accuracy))
            print("Is Leader: " + str(self.__isLeader))
            print("Other Leaders in Same Position: " + str(self.__otherLeadersInSamePos))
            print("Synergy Chance: " + str(self.__synergyChance))
            print("")
            self.__countNeighbors()

    def __countNeighbors(self):
        self.__alliesInSamePos = 0
        self.__rivalsInSamePos = 0
        self.__otherLeadersInSamePos = False
        for Enemy_Character in self.__neighbors:
            if Enemy_Character.__position == self.__position and Enemy_Character.__isLeader == False and Enemy_Character.__type == self.__allyType:
                self.__alliesInSamePos += 1
        for Enemy_Character in self.__neighbors:
            if Enemy_Character.__position == self.__position and Enemy_Character.__isLeader == False and Enemy_Character.__type == self.__rivalType:
                self.__rivalsInSamePos += 1
        if self.__isLeader == True:
            for Enemy_Character in self.__neighbors:
                if Enemy_Character.__position == self.__position and Enemy_Character.__isLeader == True:
                    self.__otherLeadersInSamePos = True
        return self.__alliesInSamePos, self.__rivalsInSamePos, self.__otherLeadersInSamePos

    def move(self):
        self.__countNeighbors()
        self.__position += self.__speed
        self.__countNeighbors()
        self.__stepAside()
        print("Enemy " + self.__name + " moved to position " + str(self.__position) + ".")
        return self.__position

    def basicAttack(self):
        if random.randint(1,100) <= self.__accuracy:
            return self.__damage 

    def __typeSynergy(self):
        self.__alliesInSamePos, self.__rivalsInSamePos, notused = self.__countNeighbors()
        sFactor = self.__alliesInSamePos - self.__rivalsInSamePos
        if self.__isLeader == True and random.randint(1,self.__synergyChance) == self.__synergyChance:
            return self.__damage * sFactor + sFactor

    def takeDamage(self, amount):
        print("Enemy " + self.__name + " took " + str(amount) + " damage!")
        return self.__health - amount

    def __stepAside(self):
        notused1, notused2, self.__otherLeadersInSamePos = self.__countNeighbors()
        if self.__isLeader == True and self.__otherLeadersInSamePos == True:
            while self.__otherLeadersInSamePos == True:
                return self.__position + random.randint(-1*(self.__speed),self.__speed)

    def __death(self):
        if self.__health <= 0:
            if self.__isLeader == False:
                print("Enemy " + self.__name + " has died.")
            elif self.__isLeader == True:
                print("Leader Enemy "+ self.__name + " has died.")

    def getEnemyName(self):
        return self.__name

class Hero_Character:
    def __init__(self, name, health, position, moveRange, attackRange, maxDamage, lazyAttackPenalty, gambleAttackBonus, gambleAttackChance):
        self.__name = str(name)
        self.__health = int(health)
        self.__position = int(position)
        self.__moveRange = int(moveRange)
        self.__attackRange = int(attackRange)
        self.__maxDamage = int(maxDamage)
        self.__lazyAttackPenalty = int(lazyAttackPenalty) #Lazy attacks have infinite range but are penalized by this amount
        self.__gambleAttackBonus = int(gambleAttackBonus)
        self.__gambleAttackChance = int(gambleAttackChance)
        self.__enemies = [] #List of Enemy_Character objects that the hero can interact with

    def addEnemies(self, Enemy_Character):
        self.__enemies.append(Enemy_Character)
        print("Enemy " + Enemy_Character.getEnemyName() + " added to hero's enemy list.")
        print("")

    def heroInfo(self):
        print("Name: " + self.__name)
        print("Health: " + str(self.__health))
        print("Position: " + str(self.__position))
        print("Move Range: " + str(self.__moveRange))
        print("Attack Range: " + str(self.__attackRange))
        print("Max Damage: " + str(self.__maxDamage))
        print("Lazy Attack Penalty: " + str(self.__lazyAttackPenalty))
        print("Gamble Attack Bonus: " + str(self.__gambleAttackBonus))
        print("Gamble Attack Chance: " + str(self.__gambleAttackChance))
        print("")

    def move(self, newPosition):
        if abs(newPosition - self.__position) <= self.__moveRange:
            self.__position = newPosition
            print("Hero " + self.__name + " moved to position " + str(self.__position) + ".")
        else:
            print("Hero " + self.__name + " cannot move to position " + str(newPosition) + ". Out of range.")

    def basicAttack(self, targetPosition):
        if abs(targetPosition - self.__position) <= self.__attackRange:
            damage = random.randint(1, self.__maxDamage)
            print("Hero " + self.__name + " attacked position " + str(targetPosition) + " for " + str(damage) + " damage.")
            return damage
        else:
            print("Hero " + self.__name + " cannot attack position " + str(targetPosition) + ". Out of range.")
            return 0

    def lazyAttack(self, targetPosition):
        damage = random.randint(1, self.__maxDamage - self.__lazyAttackPenalty)
        print("Hero " + self.__name + " performed a lazy attack on position " + str(targetPosition) + " for " + str(damage) + " damage.")
        return damage

    def gambleAttack(self, targetPosition):
        if random.randint(1, 100) <= self.__gambleAttackChance:
            damage = random.randint(1, self.__maxDamage + self.__gambleAttackBonus)
            print("Hero " + self.__name + " performed a gamble attack on position " + str(targetPosition) + " for " + str(damage) + " damage.")
            return damage
        else:
            print("Hero " + self.__name + "'s gamble attack failed.")
            return 0
        
    def takeDamage(self, amount):
        print("Hero " + self.__name + " took " + str(amount) + " damage!")
        self.__health -= amount

    def __death(self):
        if self.__health <= 0:
            print("Hero " + self.__name + " has died.")

    def getHeroName(self):
        return self.__name

# Demonstration Run

## BEFORE RELATIONSHIP
hero1 = Hero_Character("Zanitha", 150, 0, 5, 10, 30, 5, 10, 20)
enemy1 = Enemy_Character("Heathcliff", "Organic", "Machine", "Angel", 100, 10, 0, 5, 10, 0, 0, 60, False, False, 20)
enemy2 = Enemy_Character("Gabriel", "Angel", "Organic", "Machine", 200, 20, 0, 5, 10, 0, 0, 80, True, False, 40)
enemy3 = Enemy_Character("Sentient S.S.P. Panopticon", "Machine", "Machine", "Organic", 300, 30, 0, 5, 10, 0, 0, 100, True, False, 30)

print("BEFORE RELATIONSHIP")
print("")
hero1.heroInfo()
enemy1.enemyInfo()
enemy2.enemyInfo()
enemy3.enemyInfo()
print("")

## BUILDING RELATIONSHIP
print("BUILDING RELATIONSHIP")
print("")
hero1.addEnemies(enemy1)
hero1.addEnemies(enemy2)
hero1.addEnemies(enemy3)
print("")

## AFTER RELATIONSHIP
print("AFTER RELATIONSHIP")
for enemy in hero1._Hero_Character__enemies:
    enemy.enemyInfo()
print("")

### Related Object(s):
print("Related Objects:")
for enemy in hero1._Hero_Character__enemies:
    print(enemy.getEnemyName() + " is an enemy of " + hero1.getHeroName() + ".")
    print("")