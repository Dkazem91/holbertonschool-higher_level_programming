-- creates unique id table
CREATE TABLE IF NOT EXISTS `unique_id`
(`id` INT DEFAULT 1, `name` VARCHAR(256), UNIQUE(`id`));
