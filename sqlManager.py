import sqlite3
import pathlib
filepath = str(pathlib.Path(__file__).parent.resolve())
theDB = filepath + '/DB/GameDB.db'
addCharacterExtension = '/SQLStatements/addCharacter.sql'
characterListExtension = '/SQLStatements/characternameList.sql'
updateCharacterExtension = '/SQLStatements/updateCharacter.sql'
addAbilityExtension = '/SQLStatements/addAbility.sql'
AbilityListExtension = '/SQLStatements/abilityNameList.sql'
updateAbilityExtension = '/SQLStatements/updateAbility.sql'
addSkillExtension = '/SQLStatements/addSkill.sql'
SkillListExtension = '/SQLStatements/skillNameList.sql'
updateSkillExtension = '/SQLStatements/updateSkill.sql'
skillprogressionExtension = '/SQLStatements/grabSkillProgression.sql'
updateskillprogressionExtension = '/SQLStatements/updateSkillprogression.sql'

def grabScript(scriptExtension):
    with open(filepath + scriptExtension,"r",encoding="utf-8") as f:
        scriptText = f.read()
    return scriptText
def add_Character(character):
    with sqlite3.connect(theDB) as conn:
        cur = conn.cursor()
        cur.execute(grabScript(addCharacterExtension),character)
        conn.commit()
        return cur.lastrowid
def update_Character(character):
    with sqlite3.connect(theDB) as conn:
        cur = conn.cursor()
        cur.execute(grabScript(updateCharacterExtension),character)
        conn.commit()
        return cur.lastrowid
def generate_Character_List(filterParameter = None):
    with sqlite3.connect(theDB) as conn:
        cur = conn.cursor()
        cur.execute(grabScript(characterListExtension))
        names = [row[1] for row in cur.fetchall()]
        cur.execute(grabScript(characterListExtension))
        statblocks = cur.fetchall()
        return names, statblocks

def add_Ability(Ability):
    with sqlite3.connect(theDB) as conn:
        cur = conn.cursor()
        cur.execute(grabScript(addAbilityExtension),Ability)
        conn.commit()
        return cur.lastrowid
def update_Ability(Ability):
    with sqlite3.connect(theDB) as conn:
        cur = conn.cursor()
        cur.execute(grabScript(updateAbilityExtension),Ability)
        conn.commit()
        return cur.lastrowid
def generate_Ability_List(filterParameter = None):
    with sqlite3.connect(theDB) as conn:
        cur = conn.cursor()
        cur.execute(grabScript(AbilityListExtension))
        names = [row[0] for row in cur.fetchall()]
        cur.execute(grabScript(AbilityListExtension))
        statblocks = cur.fetchall()
        return names, statblocks
def add_Skill(Skill):
    with sqlite3.connect(theDB) as conn:
        cur = conn.cursor()
        cur.execute(grabScript(addSkillExtension),Skill)
        conn.commit()
        return cur.lastrowid
def update_Skill(Skill):
    with sqlite3.connect(theDB) as conn:
        cur = conn.cursor()
        cur.execute(grabScript(updateSkillExtension),Skill)
        conn.commit()
        return cur.lastrowid
def generate_Skill_List(filterParameter = None):
    with sqlite3.connect(theDB) as conn:
        cur = conn.cursor()
        cur.execute(grabScript(SkillListExtension))
        names = [row[0] for row in cur.fetchall()]
        cur.execute(grabScript(SkillListExtension))
        statblocks = cur.fetchall()
        return names, statblocks
def collectStatsNew(statEntryArray):
    statArray=[]
    for entry in statEntryArray:
        statArray.append(entry.get())
    print (statArray)
    character = tuple(statArray)
    add_Character(character)
def collectStatsUpdate(statEntryArray,CharacterMenu):
    statArray=[]
    for entry in statEntryArray:
        statArray.append(entry.get())
    statArray.append(CharacterMenu)
    print (statArray)
    character = tuple(statArray)
    update_Character(character)

def collectAbilityStatsNew(statEntryArray):
    statArray=[]
    for entry in statEntryArray:
        statArray.append(entry.get())
    print (statArray)
    ability = tuple(statArray)
    add_Ability(ability)
def collectAbilityStatsUpdate(statEntryArray,AbilityMenu):
    statArray=[]
    for entry in statEntryArray:
        statArray.append(entry.get())
    statArray.append(AbilityMenu.get())
    ability = tuple(statArray)
    update_Ability(ability)

def collectSkillStatsNew(statEntryArray):
    statArray=[]
    for entry in statEntryArray:
        statArray.append(entry.get())
    print (statArray)
    Skill = tuple(statArray)
    add_Skill(Skill)
def collectSkillStatsUpdate(statEntryArray,SkillMenu):
    statArray=[]
    for entry in statEntryArray:
        statArray.append(entry.get())
    statArray.append(SkillMenu.get())
    ability = tuple(statArray)
    update_Skill(ability)

def generate_Skill_Progress_List(Character):
    with sqlite3.connect(theDB) as conn:
        cur = conn.cursor()
        cur.execute(grabScript(skillprogressionExtension),(Character,))
        statblocks = cur.fetchall()
        return statblocks

def skillProgressUpdate(labelArray,theLevelArray,theExpArray,CharacterName):
    with sqlite3.connect(theDB) as conn:
        cur = conn.cursor()
        j = 0
        for item in labelArray:
            uniqueID = CharacterName + item.cget("text")
            cur.execute(grabScript(updateskillprogressionExtension),(item.cget("text"),CharacterName,theLevelArray[j].get(),theExpArray[j].get(),uniqueID,item.cget("text"),CharacterName,theLevelArray[j].get(),theExpArray[j].get(),uniqueID))
            j+=1
            conn.commit()
    print(f'stats for {CharacterName} committed to database.')