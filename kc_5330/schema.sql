DROP TABLE IF EXISTS datasetoverview;
DROP TABLE IF EXISTS gwascatalog;
DROP TABLE IF EXISTS encodeccre;
DROP TABLE IF EXISTS codeoverview;
DROP TABLE IF EXISTS resultsoverview;
DROP TABLE IF EXISTS table1;
DROP TABLE IF EXISTS table2;
DROP TABLE IF EXISTS table3;
DROP TABLE IF EXISTS table4;

CREATE TABLE datasetoverview (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tool TEXT NOT NULL,
    ver TEXT NOT NULL,
    src TEXT NOT NULL,
    aim TEXT NOT NULL
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

CREATE TABLE codeoverview (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filenm TEXT NOT NULL,
    purpose TEXT NOT NULL
);

CREATE TABLE resultsoverview (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filenm TEXT NOT NULL,
    title TEXT NOT NULL,
    caption TEXT NOT NULL
);

CREATE TABLE table1 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rsid TEXT NOT NULL,
    phenotype TEXT NOT NULL,
    genes TEXT NOT NULL
);

CREATE TABLE table2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rsid TEXT NOT NULL,
    phenotype TEXT NOT NULL,
    genes TEXT NOT NULL,
    exon_location TEXT NOT NULL
);

CREATE TABLE table3 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gene TEXT NOT NULL,
    variantId TEXT NOT NULL,
    chr_bp TEXT NOT NULL,
    alleles TEXT NOT NULL,
    class TEXT NOT NULL
);

CREATE TABLE table4 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    rsid TEXT NOT NULL,
    phenotype TEXT NOT NULL,
    genes TEXT NOT NULL,
    regulatory_element TEXT NOT NULL
);