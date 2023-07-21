-- User table
CREATE TABLE User (
  user_id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  role ENUM('anonymous_user', 'registered_user', 'professional_user', 'admin') NOT NULL
);

-- Conversation table
CREATE TABLE Conversation (
  conversation_id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  timestamp DATETIME NOT NULL,
  message TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES User (user_id)
);

-- TrainingData table
CREATE TABLE TrainingData (
  training_id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  source_type ENUM('prompt', 'document', 'jsonl') NOT NULL,
  source_details TEXT NOT NULL,
  status ENUM('pending', 'reviewed') NOT NULL,
  reviewed_by INT,
  FOREIGN KEY (user_id) REFERENCES User (user_id),
  FOREIGN KEY (reviewed_by) REFERENCES User (user_id)
);

-- ValidationPool table
CREATE TABLE Validation (
  validation_id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  question TEXT NOT NULL,
  answer TEXT NOT NULL,
  comment TEXT,
  status ENUM('pending', 'reviewed') NOT NULL,
  reviewed_by INT,
  FOREIGN KEY (user_id) REFERENCES User (user_id),
  FOREIGN KEY (reviewed_by) REFERENCES User (user_id)
);

-- Review table
CREATE TABLE Review (
  review_id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  training_id INT NOT NULL,
  validation_id INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES User (user_id),
  FOREIGN KEY (training_id) REFERENCES TrainingData (training_id),
  FOREIGN KEY (validation_id) REFERENCES ValidationPool (validation_id)
);

-- ActivityLog table
CREATE TABLE ActivityLog (
  log_id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  activity_type ENUM('training', 'validation') NOT NULL,
  activity_details TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES User (user_id)
);
