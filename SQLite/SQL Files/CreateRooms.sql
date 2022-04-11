CREATE TABLE Room(
    Room smallint(255) NOT NULL,
    Username varchar(255) NOT NULL,
    First varchar(50) NOT NULL,
    Last varchar(50) NOT NULL,
    Checked BOOL NOT NULL,
    Status varchar(100) NOT NULL,
    Occupancy varchar(100) NOT NULL,
    PRIMARY KEY(Room)
)