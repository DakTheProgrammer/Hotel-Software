CREATE TABLE Bags(
    Username varchar(255) NOT NULL,
    First varchar(50) NOT NULL,
    Last varchar(50) NOT NULL,
    Room smallint(255) NOT NULL,
    Status varchar (32) NOT NULL,
    Location varchar(100) NOT NULL,
    Request BOOL NOT NULL,
    PRIMARY KEY(Username)
)