CREATE TABLE Users(
    Username varchar(255) NOT NULL,
    Password varchar(255) NOT NULL,
    First varchar(50) NOT NULL,
    Last varchar(50) NOT NULL,
    Email varchar(62) NOT NULL,
    Type varchar(64) NOT NULL,
    PRIMARY KEY (Username)
)