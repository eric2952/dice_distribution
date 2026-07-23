UPDATE characterDB
SET             name = ?,
                Character_Type = ?,
                Max_Hit_Points = ?,
                Armor_Class = ?,
                Initiative_Bonus = ?,
                MovementSpeed = ?,
                Intellect = ?,
                Conscious = ?,
                Coordination = ?,
                Physique = ?
                where name = ?;