Insert into SkillProgress(
                SkillName,
                CharacterName,
                SkillLevel,
                SkillProgress,
                uniqueID)
                VALUES(?,?,?,?,?)
on conflict (uniqueID) do
UPDATE
SET             SkillName = ?,
                CharacterName = ?,
                SkillLevel = ?,
                SkillProgress = ?
                where uniqueID = ?;
