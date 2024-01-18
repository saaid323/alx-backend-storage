-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student
DELIMITER //
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	DECLARE pro_id INT;
	SELECT id INTO pro_id FROM projects WHERE name = project_name;
	IF pro_id IS NULL THEN
		INSERT INTO projects (name) VALUES (project_name);
	END IF;
	SELECT id INTO pro_id  FROM projects WHERE name = project_name;
	INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, pro_id, score);
END //

DELIMITER ;
