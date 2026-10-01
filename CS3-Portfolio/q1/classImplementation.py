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
    

    def __move(self):
        return self.__position + self.__speed

    def __basicAttack(self):
        if random.randint(1,100) <= self.__accuracy:
            return self.__damage

    def __typeSynergy(self):
        if self.__isLeader == True and random.randint(1,self.__synergyChance) == self.__synergyChance:
            return self.__damage * (self.__alliesInSamePos - self.__rivalsInSamePos) + (self.__alliesInSamePos - self.__rivalsInSamePos)

    def takeDamage(self, amount):
        return self.__health - amount

    def __stepAside(self):
        if self.__isLeader == True and self.__otherLeadersInSamePos == True:
            while self.__otherLeadersInSamePos == True:
                return self.__position + random.randint(-1*(self.__speed),self.__speed)

    def __death(self):
        if self.__health <= 0:
            if self.__isLeader == False:
                print("Enemy " + self.__name + " has died.")
            elif self.__isLeader == True:
                print("Leader Enemy "+ self.__name + " has died.")
