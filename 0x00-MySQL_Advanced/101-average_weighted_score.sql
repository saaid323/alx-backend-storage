-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DROP PROCEDURE IF EXISTS compute; 
DELIMITER //
CREATE PROCEDURE Compute (IN user_id INT)
BEGIN
	DECLARE sum_weight INT;
	DECLARE scoreAndWeight INT;
	SELECT SUM(projects.weight) INTO sum_weight FROM projects;
	SELECT SUM(corrections.score * projects.weight) INTO scoreAndWeight FROM corrections, projects WHERE
	corrections.project_id = projects.id AND corrections.user_id = user_id;
	UPDATE users SET average_score = scoreAndWeight / sum_weight WHERE id = user_id;
END //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE c INT;
	SET c = (SELECT COUNT(*) FROM users);
	WHILE c > 0 DO
		CALL Compute(c);
		SET c = c - 1;
	END WHILE;
END //
DELIMITER ;
