-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE average FLOAT;
    DECLARE user_name VARCHAR(255);
    DECLARE score_count INT;
    SELECT SUM(score) INTO average FROM corrections WHERE user_id = user_id;
    SELECT name INTO user_name FROM users WHERE id = user_id;
    SELECT COUNT(*) INTO score_count FROM corrections WHERE corrections.user_id = user_id;
    INSERT INTO users (id, name, average_score) VALUES (user_id, user_name, (average / score_count)) ON DUPLICATE KEY UPDATE average_score = average;
END //
DELIMITER ;
