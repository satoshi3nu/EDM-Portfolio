CREATE TABLE submission (
    username VARCHAR(50),
    shortname VARCHAR(50),
    version INT,
    submit_date DATE NOT NULL,
    data TEXT,
    PRIMARY KEY (username, shortname, version),
    FOREIGN KEY (username) REFERENCES student(username)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (shortname) REFERENCES assignment(shortname)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

DESCRIBE submission;