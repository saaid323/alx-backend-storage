--  SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
	DECLARE sum_weight INT;
	DECLARE scoreAndWeight INT;
	SELECT SUM(projects.weight) INTO sum_weight FROM projects;
	SELECT SUM(corrections.score * projects.weight) INTO scoreAndWeight FROM corrections, projects WHERE
	corrections.project_id = projects.id AND corrections.user_id = user_id;
	UPDATE users SET average_score = scoreAndWeight / sum_weight WHERE id = user_id;
END //
DELIMITER ;
