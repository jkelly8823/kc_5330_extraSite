DROP TABLE IF EXISTS datasetoverview;
DROP TABLE IF EXISTS codeoverview;
DROP TABLE IF EXISTS gwascatalog;
DROP TABLE IF EXISTS encodeccre;

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

CREATE TABLE gwascatalog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chromosome TEXT NOT NULL,
    start_loc INT NOT NULL,
    stop_loc INT NOT NULL,
    rsid TEXT NOT NULL,
    phenotype TEXT NOT NULL,
    gene TEXT NOT NULL
);

CREATE TABLE encodeccre (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chromosome TEXT NOT NULL,
    start_loc INT NOT NULL,
    stop_loc INT NOT NULL,
    regulatory_element TEXT NOT NULL
);
