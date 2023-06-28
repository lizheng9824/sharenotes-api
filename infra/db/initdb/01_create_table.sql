DROP SCHEMA IF EXISTS demo;
CREATE SCHEMA demo;
USE demo;

DROP TABLE IF EXISTS notes;

CREATE TABLE notes
(
    note_id             INT AUTO_INCREMENT,
    title               VARCHAR(256),
    content             VARCHAR(1024),
    parent_explorer_id  INT,
    PRIMARY KEY(note_id)
);
