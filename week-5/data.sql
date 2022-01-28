
SHOW DATABASES;
CREATE DATABASE `website`;
USE `website`;
CREATE TABLE `member`(
`id` BIGINT PRIMARY KEY AUTO_INCREMENT, 
`name` VARCHAR(255) NOT NULL,
`username` VARCHAR(255) NOT NULL,
`password` VARCHAR(255) NOT NULL,
`follower_count`INT NOT NULL DEFAULT 0,
`time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP

);
SELECT* FROM `member`;
INSERT INTO `member`(name, username, password, follower_count) VALUES("Mike", "test", "test", 2);
INSERT INTO `member`(name, username, password, follower_count) VALUES("May", "may", "test", 5);
INSERT INTO `member`(name, username, password, follower_count) VALUES("John", "test", "john", 10);
INSERT INTO `member`(name, username, password, follower_count) VALUES("Allen", "allen", "allen", 13);
SELECT* FROM `member`;
SELECT* FROM `member`
ORDER BY `time`
LIMIT 1,4;
SELECT* FROM `member`
WHERE `username`="test" AND `password`="test";
UPDATE `member`
SET `name`="test2"
WHERE `username`="test";
SELECT COUNT(*) FROM `member`;
SELECT AVG(`follower_count`) FROM `member`;

CREATE TABLE `message`(
`id` BIGINT PRIMARY KEY AUTO_INCREMENT,
`member_id` BIGINT NOT NULL,
FOREIGN KEY (member_id) REFERENCES member(id),
`content` VARCHAR(255) NOT NULL,
`time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
SELECT* FROM `message`;
INSERT INTO `message`(member_id, content) VALUES(14, "讚");
INSERT INTO `message`(member_id, content) VALUES(15, "好棒棒");
INSERT INTO `message`(member_id, content) VALUES(16, "五星吹捧");
INSERT INTO `message`(member_id, content) VALUES(17, "支持");
SELECT `name`, `content`
FROM `member`
JOIN `message`
ON `member`.`id` = `member_id`;
SELECT `name`,`username`,`content` 
FROM `member`
JOIN `message`
ON `member`.`id` = `member_id`
WHERE `member`.`username`="test";