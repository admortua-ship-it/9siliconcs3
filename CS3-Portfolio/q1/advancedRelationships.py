import random

class Enemy_Character:
    def __init__(self, name, type, allyType, rivalType, health, damage, position, speed, range, alliesInSamePos, rivalsInSamePos, accuracy, isLeader, otherLeadersInSamePos, synergyChance):
        self._name = str(name)
        self._type = str(type)
        self._allyType = str(allyType)
        self._rivalType = str(rivalType)
        self._health = int(health)
        self._damage = int(damage)
        self._position = int(position)
        self._speed = int(speed)
        self._range = int(range)
        self._alliesInSamePos = int(alliesInSamePos)
        self._rivalsInSamePos = int(rivalsInSamePos)
        self._accuracy = int(accuracy)
        self._isLeader = bool(isLeader)
        self._otherLeadersInSamePos = bool(otherLeadersInSamePos)
        self._synergyChance = int(synergyChance)
        self._neighbors = []

    def addNeighbor(self, Enemy_Character):
        self._neighbors.append(Enemy_Character)

    def enemyInfo(self):
            print("Name: " + self._name)
            print("Type: " + self._type)
            print("Ally Type: " + self._allyType)
            print("Rival Type: " + self._rivalType)
            print("Health: " + str(self._health))
            print("Damage: " + str(self._damage))
            print("Position: " + str(self._position))
            print("Speed: " + str(self._speed))
            print("Range: " + str(self._range))
            print("Allies in Same Position: " + str(self._alliesInSamePos))
            print("Rivals in Same Position: " + str(self._rivalsInSamePos))
            print("Accuracy: " + str(self._accuracy))
            print("Is Leader: " + str(self._isLeader))
            print("Other Leaders in Same Position: " + str(self._otherLeadersInSamePos))
            print("Synergy Chance: " + str(self._synergyChance))
            print("")
            self._countNeighbors()

    def _countNeighbors(self):
        self._alliesInSamePos = 0
        self._rivalsInSamePos = 0
        self._otherLeadersInSamePos = False
        for Enemy_Character in self._neighbors:
            if Enemy_Character._position == self._position and Enemy_Character._isLeader == False and Enemy_Character._type == self._allyType:
                self._alliesInSamePos += 1
        for Enemy_Character in self._neighbors:
            if Enemy_Character._position == self._position and Enemy_Character._isLeader == False and Enemy_Character._type == self._rivalType:
                self._rivalsInSamePos += 1
        if self._isLeader == True:
            for Enemy_Character in self._neighbors:
                if Enemy_Character._position == self._position and Enemy_Character._isLeader == True:
                    self._otherLeadersInSamePos = True
        return self._alliesInSamePos, self._rivalsInSamePos, self._otherLeadersInSamePos

    def move(self):
        self._countNeighbors()
        self._position += self._speed
        self._countNeighbors()
        self._stepAside()
        print("Enemy " + self._name + " moved to position " + str(self._position) + ".")
        return self._position

    def basicAttack(self):
        if random.randint(1,100) <= self._accuracy:
            return self._damage

    def _typeSynergy(self):
        self._alliesInSamePos, self._rivalsInSamePos, notused = self._countNeighbors()
        sFactor = self._alliesInSamePos - self._rivalsInSamePos
        if self._isLeader == True and random.randint(1,self._synergyChance) == self._synergyChance:
            return self._damage * sFactor + sFactor

    def takeDamage(self, amount):
        print("Enemy " + self._name + " took " + str(amount) + " damage!")
        return self._health - amount

    def _stepAside(self):
        notused1, notused2, self._otherLeadersInSamePos = self._countNeighbors()
        if self._isLeader == True and self._otherLeadersInSamePos == True:
            while self._otherLeadersInSamePos == True:
                return self._position + random.randint(-1*(self._speed),self._speed)

    def _death(self):
        if self._health <= 0:
            if self._isLeader == False:
                print("Enemy " + self._name + " has died.")
            elif self._isLeader == True:
                print("Leader Enemy "+ self._name + " has died.")

    def getEnemyName(self):
        return self._name

class BossEnemy_Character(Enemy_Character):
    def __init__(self, name, type, allyType, rivalType, health, damage, position, speed, range, alliesInSamePos, rivalsInSamePos, accuracy, isLeader, otherLeadersInSamePos, synergyChance, phases):
        super().__init__(name, type, allyType, rivalType, health, damage, position, speed, range, alliesInSamePos, rivalsInSamePos, accuracy, isLeader, otherLeadersInSamePos, synergyChance)
        self.__phases = int(phases)
        self.__neighbors = []

    def addNeighbor(self, Enemy_Character):
        self.__neighbors.append(Enemy_Character)

    def enemyInfo(self):
            print("WARNING: Boss Enemy")
            print("Name: " + self._name)
            print("Type: " + self._type)
            print("Ally Type: " + self._allyType)
            print("Rival Type: " + self._rivalType)
            print("Health: " + str(self._health))
            print("Damage: " + str(self._damage))
            print("Position: " + str(self._position))
            print("Speed: " + str(self._speed))
            print("Range: " + str(self._range))
            print("Allies in Same Position: " + str(self._alliesInSamePos))
            print("Rivals in Same Position: " + str(self._rivalsInSamePos))
            print("Accuracy: " + str(self._accuracy))
            print("Is Leader: " + str(self._isLeader))
            print("Other Leaders in Same Position: " + str(self._otherLeadersInSamePos))
            print("Synergy Chance: " + str(self._synergyChance))
            print("Phases: " + str(self.__phases))
            print("")
            self._countNeighbors()

    def _countNeighbors(self):
        self._alliesInSamePos = 0
        self._rivalsInSamePos = 0
        self._otherLeadersInSamePos = False
        for Enemy_Character in self._neighbors:
            if Enemy_Character._position == self._position and Enemy_Character._isLeader == False and Enemy_Character._type == self._allyType:
                self._alliesInSamePos += 1
        for Enemy_Character in self._neighbors:
            if Enemy_Character._position == self._position and Enemy_Character._isLeader == False and Enemy_Character._type == self._rivalType:
                self._rivalsInSamePos += 1
        if self._isLeader == True:
            for Enemy_Character in self._neighbors:
                if Enemy_Character._position == self._position and Enemy_Character._isLeader == True:
                    self._otherLeadersInSamePos = True
        return self._alliesInSamePos, self._rivalsInSamePos, self._otherLeadersInSamePos

    def move(self):
        self._countNeighbors()
        self._position += self._speed
        self._countNeighbors()
        self._stepAside()
        print("Boss " + self._name + " moved to position " + str(self._position) + ".")
        return self._position

    def basicAttack(self, targetPosition):
        if random.randint(1,100) <= self._accuracy and abs(self._position - targetPosition) <= self._range:
            return self._damage
        return 0

    def advancedAttack(self, targetPosition):
        if random.randint(1,100) <= self._accuracy and abs(self._position - targetPosition) <= self._range:
            return self._damage * 2
        return 0

    def beamAttack(self, targetPosition):
        if random.randint(1,100) <= self._accuracy:
            return self._damage * 1.5
        return 0

    def orbitalAttack(self, targetPosition):
        if abs(self._position - targetPosition) <= self._range:
            return self._damage * 2.5
        return 0

    def __typeSynergy(self):
        self._alliesInSamePos, self._rivalsInSamePos, notused = self._countNeighbors()
        sFactor = self._alliesInSamePos - self._rivalsInSamePos
        if self._isLeader == True and random.randint(1,self._synergyChance) == self._synergyChance:
            return self._damage * sFactor + sFactor

    def takeDamage(self, amount):
        print("Boss " + self._name + " took " + str(amount) + " damage!")
        return self._health - amount

    def __stepAside(self):
        notused1, notused2, self._otherLeadersInSamePos = self._countNeighbors()
        if self._isLeader == True and self._otherLeadersInSamePos == True:
            while self._otherLeadersInSamePos == True:
                return self._position + random.randint(-1*(self._speed),self._speed)

    def __switchPhase(self):
        if self.__phases > 1:
            self.__phases -= 1
            print("Boss " + self._name + " has switched to phase " + str(self._phases) + ".")
        else:
            print("Boss " + self._name + " is already in the final phase.")

    def __death(self):
        if self._health <= 0 and self.__phases >= 1:
            self.__switchPhase()
        elif self._health <= 0 and self.__phases < 1:
            print("Boss " + self._name + " has died.")

    def getEnemyName(self):
        return self._name

# Demonstration Run

## Test 1 - Inheritance

enemy1 = Enemy_Character("Decay", "Wither", "Wither", "Organic", 100, 10, 0, 5, 10, 0, 0, 60, False, False, 20)
boss = BossEnemy_Character("Avernus, Seraph of Entropy", "Titan", "Angel", ["Organic","Machine"], 3000, 100, 0, 25, 50, 0, 0, 90, True, False, 70, 3)

print("INHERITANCE TEST")
print("")
enemy1.enemyInfo()
boss.enemyInfo()

## Test 2 - Aggregation

enemy1.addNeighbor(boss)
boss.addNeighbor(enemy1)

print("AGGREGATION TEST")
print("")
for enemy in boss._BossEnemy_Character__neighbors:
    print(enemy.getEnemyName() + " is a neighbor (minion) of " + boss.getEnemyName() + ".")
