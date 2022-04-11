CREATE TABLE Employee(
    Username varchar(255) NOT NULL,
    First varchar(50) NOT NULL,
    Last varchar(50) NOT NULL,
    Role varchar(64) NOT NULL,
    Status BOOL NOT NULL,
    PRIMARY KEY(Username)
)