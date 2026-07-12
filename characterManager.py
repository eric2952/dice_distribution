import sqlite3

theDB = '/home/daniel/Desktop/Projects/SQL_Practice/GameDB.db'
insert_Statement = """INSERT INTO characterDB (
                name,
                Character_Type,
                Max_Hit_Points,
                Armor_Class,
                Initiative_Bonus,
                Core_Stat_Strength,
                Core_Stat_Dexterity,
                Core_Stat_Constitution,
                Core_Stat_Intelligence,
                Core_Stat_Wisdom,
                Core_Stat_Charisma,
                Ability_List
                )
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"""
def add_Character(conn,character):
    cur = conn.cursor()
    cur.execute(insert_Statement,character)
    conn.commit()
    return cur.lastrowid
    
try:
    with sqlite3.connect(theDB) as conn:
        character = ('Rema','Player',6,12,3,8,10,8,16,14,16,'Magic Missile;Firebolt;Staff')
        character_ID = add_Character(conn,character)
        print(f'Character {character[0]} is added with id: {character_ID}')
except sqlite3.OperationalError as e:
    print("Failed to connect: ", e)
conn.close()