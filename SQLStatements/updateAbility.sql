UPDATE AbilityLibrary
SET             AbilityName = ?,
                PrimaryStat = ?,
                SecondaryStat = ?,
                RequisitSkill = ?,
                SkillMinLevel = ?,
                AbilityType = ?,
                DiceCount = ?,
                DiceSides = ?,
                Description = ?
                where AbilityName = ?;