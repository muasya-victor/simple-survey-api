CREATE DATABASE survey_db;

USE survey_db;

CREATE TABLE question (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type ENUM('short_text', 'long_text', 'email', 'choice', 'file') NOT NULL,
    required BOOLEAN DEFAULT TRUE,
    text TEXT NOT NULL,
    description TEXT,
    multiple BOOLEAN
);

CREATE TABLE choice (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question_id INT NOT NULL,
    option_text VARCHAR(255) NOT NULL,
    FOREIGN KEY (question_id) REFERENCES question(id) ON DELETE CASCADE
);

CREATE TABLE response (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question_id INT NOT NULL,
    response_text TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (question_id) REFERENCES question(id) ON DELETE CASCADE
);

CREATE TABLE response_selected_options (
    response_id INT NOT NULL,
    choice_id INT NOT NULL,
    PRIMARY KEY (response_id, choice_id),
    FOREIGN KEY (response_id) REFERENCES response(id) ON DELETE CASCADE,
    FOREIGN KEY (choice_id) REFERENCES choice(id) ON DELETE CASCADE
);
