

### Nick Gammal
### Dr. Vanessa Aguiar
### DSC 623
### 7 December 2024


# # Project Part 3 - Implementation



# load packages

import sqlite3
import pandas as pd

# set up SQLite3

con = sqlite3.connect('pawsome_pets.db')
cur = con.cursor()

# make viewing prettier

def show(table = None):          # This doesn't work in the .py file because theres nowhere to display
    data = cur.fetchall()
    df = pd.DataFrame(data, columns = [row[0] for row in cur.description])
    display(df)
    return None



# ## Create Tables

# drop tables

cur.execute("DROP TABLE IF EXISTS Examination;")
cur.execute("DROP TABLE IF EXISTS Pet;")
cur.execute("DROP TABLE IF EXISTS Staff;")
cur.execute("DROP TABLE IF EXISTS Clinic;")
cur.execute("DROP TABLE IF EXISTS Owner;")

# generate tables and define constraints

cur.execute(
    """
    CREATE TABLE Owner(
    ownerNo VARCHAR(11) UNIQUE NOT NULL,
    oNameFirst VARCHAR(32) NOT NULL,
    oNameLast VARCHAR(32) NOT NULL,
    oAddress VARCHER(32) NOT NULL,
    oPhone VARCHAR(10) NOT NULL,
    PRIMARY KEY (ownerNo),
    CONSTRAINT oPhoneLength CHECK (LENGTH(oPhone) == 10),
    CONSTRAINT oPhoneChars CHECK (oPhone NOT GLOB '^[0123456789]+$'),
    CONSTRAINT ownerNoChars CHECK (ownerNo NOT GLOB '^[01]+$')
    );
    """
)

cur.execute(
    """
    CREATE TABLE Clinic(
    clinicNo VARCHAR(11) UNIQUE NOT NULL,
    managerNo VARCHAR(11) UNIQUE NOT NULL,
    cName VARCHAR(32) NOT NULL,
    cAddress VARCHER(32) NOT NULL,
    cPhone VARCHAR(10) NOT NULL,
    PRIMARY KEY (clinicNo),
    FOREIGN KEY (managerNo) REFERENCES Staff(staffNo),
    CONSTRAINT cPhoneLength CHECK (LENGTH(cPhone) == 10),
    CONSTRAINT cPhoneChars CHECK (cPhone NOT GLOB '^[0123456789]+$'),
    CONSTRAINT clinicNoChars CHECK (clinicNo NOT GLOB '^[01]+$')
    );
    """
)

cur.execute(
    """
    CREATE TABLE Staff(
    staffNo VARCHAR(11) UNIQUE NOT NULL,
    clinicNo VARCHAR(11) NOT NULL,
    sNameFirst VARCHAR(32) NOT NULL,
    sNameLast VARCHAR(32) NOT NULL,
    sAddress VARCHER(32) NOT NULL,
    sPhone VARCHAR(10) NOT NULL,
    DOB DATE NOT NULL,
    position VARCHAR(32) NOT NULL,
    salary INTEGER NOT NULL,
    PRIMARY KEY (staffNo),
    FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo),
    CONSTRAINT sPhoneLength CHECK (LENGTH(sPhone) == 10),
    CONSTRAINT sPhoneChars CHECK (sPhone NOT GLOB '^[0123456789]+$'),
    CONSTRAINT staffNoChars CHECK (staffNo NOT GLOB '^[01]+$')
    );
    """
)

cur.execute(
    """
    CREATE TABLE Pet(
    petNo VARCHAR(11) UNIQUE NOT NULL,
    clinicNo VARCHAR(11) NOT NULL,
    ownerNo VARCHAR(11) NOT NULL,
    pName VARCHAR(32) NOT NULL,
    DOB DATE NOT NULL,
    species VARCHAR(32) NOT NULL,
    breed VARCHAR(32),
    color VARCHAR(32) NOT NULL,
    PRIMARY KEY (petNo),
    FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo),
    FOREIGN KEY (ownerNo) REFERENCES Owner(ownerNo),
    CONSTRAINT petNoChars CHECK (petNo NOT GLOB '^[01]+$')
    );
    """
)

cur.execute(
    """
    CREATE TABLE Examination(
    examNo VARCHAR(11) UNIQUE NOT NULL,
    staffNo VARCHAR(11) NOT NULL,
    petNo VARCHAR(11) NOT NULL,
    chiefComplaint VARCHAR(256) NOT NULL,
    description VARCHAR(256) NOT NULL,
    dateSeen DATE,
    actionsTaken VARCHAR(256) NOT NULL,
    PRIMARY KEY (examNo),
    FOREIGN KEY (staffNo) REFERENCES Staff(staffNo),
    FOREIGN KEY (petNo) REFERENCES Pet(petNo),
    CONSTRAINT examNoChars CHECK (examNo NOT GLOB '^[01]+$')
    );
    """
)

cur.execute("SELECT * FROM Owner")
#show()

cur.execute("SELECT * FROM Pet")
#show()

cur.execute("SELECT * FROM Staff")
#show()

cur.execute("SELECT * FROM Clinic")
#show()

cur.execute("SELECT * FROM Examination")
#show()



# ## Create Data

# input 5 rows for each table

cur.execute("DELETE FROM Examination;")
cur.execute("DELETE FROM Owner;")
cur.execute("DELETE FROM Pet;")
cur.execute("DELETE FROM Staff;")
cur.execute("DELETE FROM Clinic;")

cur.execute(
    """
    INSERT INTO Owner
    VALUES
        ('00000000000', 'Nicholas', 'Gammal', '16 Rioja Way, Miami FL', '3051234567'),
        ('10000000000', 'Anabelle', 'Sweeney', '4200 Baker St, Miami FL', '3050987654'),
        ('01000000000', 'Denise', 'Gammal', '37 Largo Ave, Homestead FL', '6451234567'),
        ('11000000000', 'Jen', 'Borenstein', '51 Area Blvd, Coral Gables FL', '3052749673'),
        ('00100000000', 'Sharon', 'Lohrey', '6280 Blue Road, South Miami FL', '3058362637'),
        ('10100000000', 'James T.', 'Kirk', 'NCC-1701, Space', '3236345667'),
        ('01100000000', 'Harry', 'Potter', '4 Privet Drive, Cupboard Under the Stairs', '6927496873');
    """
)

cur.execute(
    """
    INSERT INTO Staff
    VALUES
        ('00000000000', '00000000000', 'Andrei', 'Gronkowski', '5172 Grand Ave, Miami FL', '3058863253', '1982-07-02', 'Animal Dietician', 120000),
        ('10000000000', '00000000000', 'Sarah', 'Gronkowski', '5172 Grand Ave, Miami FL', '3058861937', '1983-12-22', 'Senior Veterinarian', 135000),
        ('01000000000', '01000000000', 'Marcus', 'Aurelius', '1 Roman Blvd, South Miami FL', '3052365940', '1967-05-15', 'Senior Veterinarian', 135000),
        ('11000000000', '11000000000', 'Elizabeth', 'Vanderstein', '36 Blanco Street, Homestead FL', '6452985783', '1991-08-05', 'Senior Veterinarian', 125000),
        ('00100000000', '01000000000', 'Hannah', 'Hall', '52 Sextant Way, Coral Gables FL', '3053647592', '1979-10-10', 'Assistant Veterinarian', 78000);
    """
)

cur.execute(
    """
    INSERT INTO Clinic
    VALUES
        ('00000000000', '10000000000', 'Miami Pawsome Hospital', '1 Vetrinarian Way, Miami FL', '3052342345'),
        ('10000000000', '00010000000', 'San Antonio Pawsome Clinic', '22 Bulldog Blvd, San Antonio TX', '2102349393'),
        ('01000000000', '01000000000', 'UMiami Pet Clinic', '6100 Red Road, Coral Gables FL', '3052348671'),
        ('11000000000', '11000000000', 'Homestead Pawsome Hospital', '2573 Verde Ave, Homestead FL', '3052340027'),
        ('00100000000', '00000101000', 'South Beach Dolphin Care', '17 Embaracero Road, Miami Beach FL', '3052341526');
    """
)

cur.execute(
    """
    INSERT INTO Pet
    VALUES
        ('00000000000', '01000000000', '10000000000', 'Mr. Pickles', '2022-08-05', 'Felis catus', 'American Shorthair', 'gray'),
        ('10000000000', '01000000000', '01000000000', 'Kiva', '2014-06-27', 'Canis lupus familiaris', 'Australian Labradoodle', 'caramel'),
        ('01000000000', '01000000000', '00000000000', 'Bubble', '2024-01-13', 'Canis lupus familiaris', 'Pitbull', 'brown'),
        ('11000000000', '00000000000', '00100000000', 'Fox', '2018-10-12', 'Canis lupus familiaris', 'Shiba', 'red'),
        ('00100000000', '00000000000', '11000000000', 'Hestia', '2015-03-30', 'Felis catus', 'Siamese', 'white'),
        ('10100000000', '00000000000', '10100000000', 'Butler', '2019-02-15', 'Canis lupus familiaris', 'Great Dane', 'tan'),
        ('11100000000', '00000000000', '10100000000', 'Mr. Spock', '2010-11-17', 'Felis catus', 'Orange Tabby', 'orange'),
        ('01100000000', '00000000000', '10100000000', 'Snuggles', '2018-06-28', 'Canis lupus familiaris', 'Poodle', 'white'),
        ('00010000000', '10000000000', '01100000000', 'Hedwig', '2001-11-16', 'Bubo scandiacus', NULL, 'white');
    """
)

cur.execute(
    """
    INSERT INTO Examination
    VALUES
        ('00000000000', '10000000000', '10100000000', 'Attacking people, frothing at the mouth, speaking unknown alien language. Alien parasite infected dog via respiratory system.', 'Lung medication and breathing therapy to remove parasite and restore proper behavior.', '2021-04-23', 'treatment administered, breathing therapist recommended'),
        ('10000000000', '00100000000', '01000000000', 'Itchy spot on hind leg, excessive licking until skin raw', 'cone of shame to stop licking, antibiotic oinment for itchy spot', '2024-09-16', 'cone attached to dog, ointment given to owner'),
        ('01000000000', '01000000000', '10000000000', 'indigestion', 'dietary restrictions including food supplement', '2023-05-15', 'recommended new diet and sold supplement to owner'),
        ('11000000000', '10000000000', '11100000000', 'violently stealing and consuming all milk on the starship Enterprise. Serious addiction', 'send to rehabilitation center for one week', '2024-12-07', 'cat sent to addiction rehabilitation center'),
        ('00100000000', '00100000000', '00000000000', 'morbidly obese', 'more exercise needed, dietary changes also recommended', '2023-04-30', 'wrote workout plan and taught to owner, also recommended diet pills to help weight loss'),
        ('10100000000', '00100000000', '01100000000', 'broken leg', 'set bones correctly, apply splint', '2022-10-31', 'bones set, splint applied and brace for future sold to owner');
    """
)

# show contents of tables

cur.execute("SELECT * FROM Owner")
#show()

cur.execute("SELECT * FROM Pet")
#show()

cur.execute("SELECT * FROM Staff")
#show()

cur.execute("SELECT * FROM Clinic")
#show()

cur.execute("SELECT * FROM Examination")
#show()



# ## 5 Queries

# Q1 - Show the records of all examinations performed on pets owned by James T. Kirk

cur.execute(
    """
    SELECT *
    FROM Examination
    WHERE petNo IN (
        SELECT petNo
        FROM Pet p 
        JOIN Owner o ON o.ownerNo = p.ownerNo
        WHERE (oNameFirst = 'James T.') AND (oNameLast = 'Kirk')
    ) 
    """
)

#show()

# Q2 - Show the list of all staff who manage clinics, the name of the clinic they manage, and their salary

cur.execute(
    """
    SELECT staffNo, c.clinicNo, sNameFirst, sNameLast, cName, salary
    FROM Staff s
    JOIN Clinic c ON managerNo = staffNo
    """
)

#show()

# Q3 - Show the list of all Poodles examined by staff member Hannah Hall

cur.execute(
    """
    SELECT p.petNo, p.pName, examNo
    FROM Examination e
    JOIN Pet p ON p.petNo = e.petNo
    JOIN Staff s ON s.staffNo = e.staffNo
    WHERE (s.sNameFirst = 'Hannah') AND (s.sNameLast = 'Hall') AND breed = 'Poodle'
    """
)

#show()

# Q4 - List all pet owners who have a pet registered with Pawsome Pets clinics in San Antonio, TX

cur.execute(
    """
    SELECT *
    FROM Owner
    WHERE ownerNo IN (
        SELECT ownerNo
        FROM Pet p
        JOIN clinic c ON c.clinicNo = p.clinicNo
        WHERE cAddress LIKE '%San Antonio TX'
    )
    """
)

#show()

# Q5 - Show all pets registered at UMiami Pet Clinic

cur.execute(
    """
    SELECT *
    FROM Pet
    WHERE clinicNo IN (
        SELECT clinicNo
        FROM Clinic
        WHERE cName = 'UMiami Pet Clinic'
    )
    """
)

#show()



