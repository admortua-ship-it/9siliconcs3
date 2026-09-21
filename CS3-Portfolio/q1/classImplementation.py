import random

class Enemy_Character:
    def __init__(self, name, type, allyType, rivalType, health, damage, position, speed, range, alliesInSamePos, rivalsInSamePos, accuracy, isLeader, otherLeadersInSamePos, synergyChance):
        self.__name = name
        self.__type = type
        self.__allyType = allyType
        self.__rivalType = rivalType
        self.__health = health
        self.__damage = damage
        self.__position = position
        self.__speed = speed
        self.__range = range
        self.__alliesInSamePos = alliesInSamePos
        self.__rivalsInSamePos = rivalsInSamePos
        self.__accuracy = accuracy
        self.__isLeader = isLeader
        self.__otherLeadersInSamePos = otherLeadersInSamePos
        self.__synergyChance = synergyChance

    def __move(self):
        return self.__position + self.__speed

    def __basicAttack(self):
        return self.__damage

    def typeSynergy(self):
        if self.__isLeader == True and random.randint(1,self.__synergyChance) == self.__synergyChance:
            print("wip")

    def takeDamage(self, amount):
        return self.__health - amount

    def stepAside(self):
        if self.__otherLeadersInSamePos == True:
            while self.__otherLeadersInSamePos == True:
                return self.__positon + random.randint(-1*(self.__speed),self.__speed)

    def death():
        print("wip")