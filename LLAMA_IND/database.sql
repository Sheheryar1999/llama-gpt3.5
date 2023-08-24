database.sql
CREATE DATABASE law_chatbot;

USE law_chatbot;


CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    is_admin BOOLEAN NOT NULL,
    role VARCHAR(50) NOT NULL
);

CREATE TABLE Training_Methods (
    method_id INT AUTO_INCREMENT PRIMARY KEY,
    method_name VARCHAR(100) NOT NULL,
    description TEXT
);


CREATE TABLE Questions (
    question_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    question_text TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);


CREATE TABLE Answers (
    answer_id INT AUTO_INCREMENT PRIMARY KEY,
    question_id INT,
    answer_text TEXT,
    is_reviewed BOOLEAN DEFAULT FALSE,
    reviewed_by INT,
    reviewed_timestamp TIMESTAMP,
    FOREIGN KEY (question_id) REFERENCES Questions(question_id),
    FOREIGN KEY (reviewed_by) REFERENCES Users(user_id)
);


CREATE TABLE Validation_Pool (
    validation_id INT AUTO_INCREMENT PRIMARY KEY,
    question_id INT,
    suggested_answer TEXT,
    comments TEXT,
    reviewed_by INT,
    review_timestamp TIMESTAMP,
    FOREIGN KEY (question_id) REFERENCES Questions(question_id),
    FOREIGN KEY (reviewed_by) REFERENCES Users(user_id)
);


CREATE TABLE Training_Pool (
    training_id INT AUTO_INCREMENT PRIMARY KEY,
    question_id INT,
    answer_id INT,
    method_id INT,
    training_data TEXT,
    status VARCHAR(50) DEFAULT 'pending',
    reviewed_by INT,
    reviewed_timestamp TIMESTAMP,
    FOREIGN KEY (question_id) REFERENCES Questions(question_id),
    FOREIGN KEY (answer_id) REFERENCES Answers(answer_id),
    FOREIGN KEY (method_id) REFERENCES Training_Methods(method_id),
    FOREIGN KEY (reviewed_by) REFERENCES Users(user_id)
);


CREATE TABLE Admin_Activities (
    activity_id INT AUTO_INCREMENT PRIMARY KEY,
    admin_user_id INT,
    action_description TEXT,
    action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (admin_user_id) REFERENCES Users(user_id)
);


CREATE TABLE Conversational_Record (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    professional_user_id INT,
    registered_client_id INT,
    conversation_data TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (professional_user_id) REFERENCES Users(user_id),
    FOREIGN KEY (registered_client_id) REFERENCES Users(user_id)
);

CREATE TABLE Prompt_Data (
    prompt_id INT AUTO_INCREMENT PRIMARY KEY,
    professional_user_id INT,
    prompt_text TEXT,
    correct_answer TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (professional_user_id) REFERENCES Users(user_id)
);

CREATE TABLE Video_Transcriptions (
    transcription_id INT AUTO_INCREMENT PRIMARY KEY,
    video_url VARCHAR(255) NOT NULL,
    transcription_text TEXT,
    transcription_status VARCHAR(50) DEFAULT 'pending',
    transcribed_by INT,
    transcription_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (transcribed_by) REFERENCES Users(user_id)
);

CREATE TABLE Formula_Detection (
    formula_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    detected_formula TEXT,
    detection_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
