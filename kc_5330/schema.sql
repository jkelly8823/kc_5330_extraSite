DROP TABLE IF EXISTS datasetoverview;
DROP TABLE IF EXISTS codeoverview;

CREATE TABLE datasetoverview (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tool TEXT NOT NULL,
    ver TEXT NOT NULL,
    src TEXT NOT NULL,
    aim TEXT NOT NULL
);

CREATE TABLE codeoverview (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filenm TEXT NOT NULL,
    purpose TEXT NOT NULL
);
