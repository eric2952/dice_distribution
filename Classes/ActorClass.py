class Actor:
    #Intellect for abilities that require knowledge gain and recall
    #Conscious for abilities that require problem solving and observation
    #Coordination for abilities that require fine control complex maneuvers
    #Physiqe for abilites that require strong body form and presence
    #Abilites can draw on more than one core stat to influence their effect
    def __init__(self, hp, ac, name,InitiativeScore, movementSpeed=None,characterType=None,InitiativeBonus=None,Intellect=None,Conscious=None,Coordination=None,Physique=None,Abilities=None,Inventory=None,Skills=None):
        self.hp = hp
        self.ac = ac
        self.name = name
        self.movementSpeed=movementSpeed
        self.characterType = characterType
        self.InitiativeBonus = InitiativeBonus
        self.Intellect = Intellect
        self.Conscious = Conscious
        self.Coordination = Coordination
        self.Physique = Physique
        self.Abilities = Abilities
        self.Inventory = Inventory
        self.InitiativeScore = InitiativeScore
        self.Skills = Skills
        
    def apply_damage(self,damage):
        self.hp -= damage
    def test_hit(self,attackRoll):
        if attackRoll < self.ac:
            return False
        else:
            return True
    def apply_healing(self,heals):
        self.hp += heals
    def updateInitiative(self,totalCombatants):
        if self.InitiativeScore == 1:
            self.InitiativeScore == totalCombatants
        else:
            self.InitiativeScore-=1
    
