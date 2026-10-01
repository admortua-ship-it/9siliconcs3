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

# Demonstration Run

## BEFORE:
Enemy1 = Enemy_Character("Husk", "Organic", "Organic", "Machine", 100, 10, 0, 5, 10, 0, 0, 80, False, False, 20)
Enemy2 = Enemy_Character("The Insurrectionist", "Organic", "Organic", "Machine", 200, 20, 0, 5, 10, 0, 0, 80, True, False, 20)
Enemy1.addNeighbor(Enemy2)
Enemy2.addNeighbor(Enemy1)

print("BEFORE ACTION")
print("Object 1:")
Enemy1.enemyInfo()
print("")
print("Object 2:")
Enemy2.enemyInfo()

## ACTION
print("\nACTION")
Enemy1.move()
Enemy1.takeDamage(50)

## AFTER
print("\nAFTER ACTION")
print("Object 1:")
Enemy1.enemyInfo()
print("")
print("Object 2:")
Enemy2.enemyInfo()
