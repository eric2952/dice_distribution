from ActorClass import Actor
class Ability:
    #
    #skill Level corresponds to the skill that unlocks the ability, the trunk of the tree
    # the Primary and Secondary attributes correspond to the core stats of the character, and do not carry as much influence as the parent skill
    def __init__(self, name, description,skillLevel, AttributeScorePrimary, AttributeLevelSecondary=None):
        self.name = name
        self.description = description
        self.skillLevel = skillLevel
        self.AttributeScorePrimary = AttributeScorePrimary
        self.AttributeLevelSecondary = AttributeLevelSecondary
    
    def determineBonus(self,theActor: Actor):
        abilityList = theActor.Abilities
        i = 0
        while abilityList[i] != self.name:
            i+=1
        
        primaryStatScore = getattr(Actor,self.AttributeScorePrimary)
        if self.AttributeLevelSecondary != None:
            secondaryStatScore = getattr(Actor,self.AttributeLevelSecondary)

        primaryBonus = primaryStatScore 



    

    
