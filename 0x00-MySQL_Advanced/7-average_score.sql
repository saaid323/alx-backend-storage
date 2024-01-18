-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE average FLOAT;
    DECLARE user_name VARCHAR(255);
    
    SELECT AVG(score) INTO average FROM corrections WHERE user_id = user_id;
    SELECT name INTO user_name FROM users WHERE id = user_id;
    
    INSERT INTO users (id, name, average_score) VALUES (user_id, user_name, average) ON DUPLICATE KEY UPDATE average_score = average;
END //
DELIMITER ;
