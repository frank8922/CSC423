# Final Project

Date: Dec 2, 2020
Name: Francisco Belliard

## Case Study Notes: *Reliable Rentals*

> Purpose: Rent out vehicles to clients.

- Case Study Description

    A company called Reliable Rentals rents out vehicles at different outlets (locations/sites).
    Each outlet has a number, address, phone number and a fax number. Each site is allocated a stock of vehicles for hire. The registration number uniquely identifies each vehicle for hire
    and is used when hiring a vehicle to a client.

    Clients may hire vehicles for various periods of time. Each individual hire agreement between
    a client and the Company is uniquely identified using a hire number. Information stored on
    the vehicles for hire include: the vehicle registration number, model, make, engine size,
    capacity, current mileage, daily hire rate, and the current location (outlet) of each vehicle.
    The data stored on clients includes the client number (unique identifier), name (first and last
    name), home address, phone number, date of birth, and driving license number.

    The data stored on a hire agreement includes: the hire number, the client’s number, name,
    address, and phone number, date the client started the hire period, date the client wishes to
    terminate the hire period, the vehicle registration number, model and make, the mileage
    before and after the hire period. Finally, information is stored on the staff based at various
    outlets including: staff number, name (first and last name), home address, home phone
    number, date of birth (DOB), sex, date joined the Company, job title, and salary. Each staff
    member is associated with a single outlet.

### 1. Develop a conceptual data model reflecting the following requirements:

---

**a.  Identify the relations or entity types.**

- Client(**clientNo,** fName, lName, address, phoneNo, DOB, dLicenseNo).
- Staff(**staffNo**, fName, lName, address, phoneNo, DOB, sex, jobTitle, dateHired, salary, outletNo).
- Outlet(**outletNo**, address, phoneNo, faxNo, staffNo,)
- Vehicle(regNo, make, model, engineSize, capacity, currentMileage, dailyRate, outletNo)
- HireAgreement(**hireNo**, clientNo, fName,lName, rentalStarted, returnBy, startMileage, endMileage, regNo)

---

**b.  Identify the relationship types as well as their participation and cardinality**

### Relationship Types

- Outlet *has* Staff
- Outlet *is allocated* Vehicles
- A Client *signs a* Hire Agreement
- Each Hire agreement is *for a* Vehicle

![Final%20Project%202a4067fb3de3414f9a37c966055a2877/Partial-Entity-Relation-Diagram.png](Final%20Project%202a4067fb3de3414f9a37c966055a2877/Partial-Entity-Relation-Diagram.png)

Fig 1. Individual entities and their respective relationships.

![Final%20Project%202a4067fb3de3414f9a37c966055a2877/Entity-Relation-Diagram.png](Final%20Project%202a4067fb3de3414f9a37c966055a2877/Entity-Relation-Diagram.png)

Fig 1.1 Connected ER-Diagram to show entity relationships.

### Cardinality Constraints

- Outlet is allocated Vehicles
    - An outlet is allocated vehicles (1..*)
    - A vehicle is allocated to an outlet (1..1)
- Outlet has Staff
    - An outlet has one or more staff members (1..*)
    - A staff member is assigned to a an outlet (1..1)
- A Client *signs a* Hire Agreement
    - A client signs one or more hire agreements (1..*)
    - A hire agreement is signed by a client (1..1)
- Each Hire agreement is *for a* Vehicle
    - A hire agreement is for a vehicle (1..1)
    - A vehicle can either have a hire agreement or not (0..1)

![Final%20Project%202a4067fb3de3414f9a37c966055a2877/Partial-Cardinality-Relation_Diagram.png](Final%20Project%202a4067fb3de3414f9a37c966055a2877/Partial-Cardinality-Relation_Diagram.png)

Fig 1.2 Individual entities and their cardinality constraints.

![Final%20Project%202a4067fb3de3414f9a37c966055a2877/Cardinality-Relation_Diagram.png](Final%20Project%202a4067fb3de3414f9a37c966055a2877/Cardinality-Relation_Diagram.png)

Fig. 1.3 Entities and their relationships along with their respective cardinality constraints.

---

c.  **Identify the attributes associated to the previous entity or relationship types.**

---

- Client(**clientNo,** fName, lName, address, phoneNo, DOB, dLicenseNo).
    1. clientNo: a single-valued attribute to hold the client number
    2. fName: a single-valued attribute to hold the clients first name.
    3. lName: a single-valued attribute to hold the clients last name.
    4. address: a single-valued attribute to hold the client addressD
    5. phone: a single-valued attribute to hold the client phone number.
    6. DOB: a single-valued attribute to hold the client date of birth.
    7. dLicenseNo: a single-valued attribute to hold the client driver license number.

- Staff(**staffNo**, fName, lName, address, phoneNo, DOB, sex, jobTitle, dateHired, salary, outletNo).
    1. staffNo: a single-valued attribute to hold the staff number
    2. fName: a single-valued attribute to hold the staff member first name.
    3. lName: a single-valued attribute to hold the staff member last name.
    4. address: a single-valued attribute to hold the staff member addressD
    5. phone: a single-valued attribute to hold the staff member phone number.
    6. DOB: a single-valued attribute to hold the staff member date of birth.
    7. sex: single-valued attribute to hold the staff members sex.
    8. jobTitle: single-valued attribute to hold the staff job title.
    9. dateHired: singled-valued attribute to hold the date the staff member was hired.
    10. salary: single-valued attribute to hold the staff members salary.
    11. outletNo: single-valued attribute to hold the outlet the staff member is assigned to.
- Outlet(**outletNo**, address, phoneNo, faxNo, staffNo,)
    1. outletNo: a single-valued attribute to hold the outlet number.
    2. address: a single-valued attribute to hold the outlet address.
    3. phoneNo: a single-valued attribute to hold the outlet phone number.
    4. faxNo: a single-valued attribute to hold the outlet fax number.
    5. staffNo: a single-valued attribute to hold the staff number assigned to that outlet.
- Vehicle(regNo, make, model, engineSize, capacity, currentMileage, dailyRate, outletNo)
    1. regNo: a single-valued attribute to hold the vehicle registration number.
    2. make: a single-valued attribute to hold the vehicle make.
    3. model: a single-valued attribute to hold the vehicle model.
    4. engineSize: a single-valued attribute to hold the vehicle engine size.
    5. capacity: a single-valued attribute to hold the vehicle capacity.
    6. currentMileage: a single-valued attribute to hold the vehicle's current mileage.
    7. dailyRate: a single-valued attribute to hold the vehicle's daily rental rate.
    8. outletNo: a single-valued attribute to hold the outlet the vehicle belongs to.
- HireAgreement(**hireNo**, clientNo, fName,lName, rentalStarted, returnBy, startMileage, endMileage, regNo)
    1. hireNo: a single-valued attribute to hold the hire number.
    2. clientNo: a single-valued attribute to hold the client number.
    3. fName: a single-valued attribute to hold the clients first name.
    4. lName: a single-valued attribute to hold the clients last name.
    5. rentalStarted: a single-valued attribute to hold the rental start date.
    6. returnBy: a single-valued attribute to hold the rental return date.
    7. startMileage: a single-valued attribute to hold the rental start mileage.
    8. endMileage: a single-valued attribute to hold the rental end mileage.
    9. regNo: a single-valued attribute to hold the vehicle registration number assigned to the hire agreement.

![Final%20Project%202a4067fb3de3414f9a37c966055a2877/Attribute-Diagram.png](Final%20Project%202a4067fb3de3414f9a37c966055a2877/Attribute-Diagram.png)

Fig 1.4 Individual entities and their attributes

---

**d.  Determine candidate and primary key attributes of entity types.**

---

**Strong Entity Types:**

- Client(**clientNo,** fName, lName, address, phoneNo, DOB, dLicenseNo).
    - Primary key: client No
    - Candidate key: clientNo, dLicenseNo
- Staff(**staffNo**, fName, lName, address, phoneNo, DOB, sex, jobTitle, dateHired, salary, outletNo).
    - Primary key: staffNo
    - Candidate key: staffNo, outletNo
- Outlet(**outletNo**, address, phoneNo, faxNo, staffNo,)
    - Primary key: outletNo
    - Candidate key: outletNo, staffNo
- Vehicle(regNo, make, model, engineSize, capacity, currentMileage, dailyRate, outletNo)
    - Primary key: regNo
    - Candidate key: regNo, outletNo
- HireAgreement(**hireNo**, clientNo, fName,lName, rentalStarted, returnBy, startMileage, endMileage, regNo)
    - Primary key: hireNo
    - Candidate key: regNo, clientNo, regNo

**Weak Entity Types:**

- None

---

### 2. Develop a logical data model based on the following requirements:

---

a.  Derive relations from the conceptual model.

---

![Final%20Project%202a4067fb3de3414f9a37c966055a2877/Logical-Entity-Relationship_Diagram.png](Final%20Project%202a4067fb3de3414f9a37c966055a2877/Logical-Entity-Relationship_Diagram.png)

Fig. 2.1 Logical data model with foreign keys

b.  Validate the logical model using normalization to 3NF.

---

Tables defined in conceptual model: 

**1NF (Flattening the UNF Table**

- Client(**clientNo,** fName, lName, address, phoneNo, DOB, dLicenseNo).
- Staff(**staffNo**, fName, lName, address, phoneNo, DOB, sex, jobTitle, dateHired, salary, outletNo).
- Outlet(**outletNo**, address, phoneNo, faxNo, staffNo,)
- Vehicle(**regNo**, make, model, engineSize, capacity, currentMileage, dailyRate, outletNo)
- HireAgreement(**hireNo**, clientNo, fName,lName, rentalStarted, returnBy, startMileage, endMileage, regNo)

**Functional Dependancies**

- clientNo —> fName, lName, address, phoneNo, DOB, dLicense (Full)
- clientNo —> dLicense (candidate key)
- staffNo —> fName, lName, address, phoneNo, DOB, sex, jobTitle, dateHired, salary, outletNo (Full)
- outletNo —> address, phoneNo, faxNo, staffNo
- regNo —> make, model, engineSize, capacity, currentMileage, dailyRate, outletNo (Full)
- hireNo —> clientNo, fName,lName, rentalStarted, returnBy, startMileage, endMileage, regNo (Full)

**2NF (Remove partial dependancies)**

- No Partial dependancies found.

**3NF (Remove transitive dependancies)**

- No transitive dependancies found.

---

c. Define integrity constraints:

---

i.  Primary key constraints.

- all primary keys must be an integer and cannot be NULL

ii. Referential integrity / Foreign key constraints.

- For tables: Client, Staff, Outlet, and Vehicle, the foreign key must be an integer and cannot be NULL
- For the HireAgreement table the foreign key regNo, linking the Vehicle table with this one, can be NULL since the a vehicle either has a hire agreement or doesn't.

iii.  General constraints. (if any)

1. Registration numbers must be unique (likely PK)
2. Client rental start date must be < end date and > current date
3. Rental end date must be > current date
4. Hire numbers must be unique (likely PK)
5. Engine size must be either: 2L, 4L, 6L
6. Capacity must be either: 2 seats, 4 seats, 6 seats
7. Current mileage cannot exceed 100K miles
8. Daily hire rate must be ≥ $5
9. DOB must have a year ≥ 1995 (i.e age is at least 25)
10. Sex must be either male or female
11. Job title must be either: Sales Rep, Manager, Finance Rep, Customer Service Rep
12. Salary must be at least 45K but ≤ 100K

### 3. Translate the logical data model for the Oracle Enterprise DBMS.

---

a.  Develop SQL code to create the entire database schema, reflecting the constraints identified in previous steps.

---

```sql
CREATE table Outlet
(
    outletNo int          not null,
    address   varchar(50) not null,
    phoneNo  varchar(50)  not null,
    faxNo    varchar(50)  not null,
    PRIMARY KEY (outletNo)
);

CREATE TABLE Client
(
    clientNo int not null PRIMARY KEY,
    fName varchar(50) not null,
    lName varchar(50) not null,
    address varchar(50) not null,
    phoneNo varchar(50) not null,
    dob date not null,
    check ( dob < to_date('17-dec-1995') ),
    dLicenseNo varchar(50) not null
);

CREATE TABLE Staff
(
    staffNo   int         not null,
    fName     varchar(50) not null,
    lName     varchar(50) not null,
    address   varchar(50) not null,
    phoneNo   varchar(50) not null,
    dob         date      not null,
    check ( dob < to_date('17-dec-2002') ),
    sex         varchar(2),
    jobTitle  varchar(50) not null,
    dateHired date        not null,
    salary      int         not null,
        check ( salary between 45000 and 100000),
    outletNo  int         not null,
    constraint outletno
        foreign key (outletNo) references Outlet
);

CREATE TABLE Vehicle
(
   regNo int not null
      constraint vehicle_pk
         primary key,
   make varchar(50),
   model varchar(50),
   engineSize varchar(50),
       check ( engineSize in ('2l','4l','6l') ),
   capacity int,
       check ( capacity between 2 and 6),
   currentMileage int,
       check ( currentMileage <= 100000 ),
   dailyRate int,
       check ( dailyRate between 4 and 50),
   outletNo int not null,
       foreign key (outletNo) references  Outlet
);

CREATE TABLE HireAgreement
(
    hireNo         integer primary key,
    fName         VARCHAR(50),
    lName         VARCHAR(50),
    rentalStarted date,
    check ( rentalStarted > TO_DATE('19-DEC-2020') ),
    returnBy      date,
    startMileage  INT,
    endMileage   INT,
		regNo      integer default NULL,
    FOREIGN KEY(regNo)REFERENCES Vehicle
);

```

b.  Create at least 5 tuples for each for each relation in your database.

---

```sql
insert into Outlet (outletNo, address, phoneNo, faxNo) values (1, '567 Bunker Hill Park', '354-601-0457', '443-469-4360');
insert into Outlet (outletNo, address, phoneNo, faxNo) values (2, '53 Leroy Avenue', '327-933-7767', '978-207-0119');
insert into Outlet (outletNo, address, phoneNo, faxNo) values (3, '5 Lerdahl Junction', '809-840-0039', '353-785-2119');
insert into Outlet (outletNo, address, phoneNo, faxNo) values (4, '682 Dwight Court', '201-567-4740', '524-240-2887');
insert into Outlet (outletNo, address, phoneNo, faxNo) values (5, '4932 Surrey Drive', '312-585-7907', '728-625-7215');
```

![Final%20Project%202a4067fb3de3414f9a37c966055a2877/Screen_Shot_2020-12-04_at_5.33.41_PM.png](Final%20Project%202a4067fb3de3414f9a37c966055a2877/Screen_Shot_2020-12-04_at_5.33.41_PM.png)

```sql
insert into Client (clientNo, fName, lName, address, phoneNo, DOB, dLicenseNo) values (1, 'Sibylle', 'Torbard', '68 Schmedeman Pass', '769-409-0265', '03-Jun-1990', '4636relb881');
insert into Client (clientNo, fName, lName, address, phoneNo, DOB, dLicenseNo) values (2, 'Gale', 'Ganley', '4 Dapin Plaza', '299-113-5344', '27-Oct-1987', '2953evvy547');
insert into Client (clientNo, fName, lName, address, phoneNo, DOB, dLicenseNo) values (3, 'Erinn', 'Lewry', '680 Golf Street', '675-699-9816', '29-Oct-1991', '2773okhr220');
insert into Client (clientNo, fName, lName, address, phoneNo, DOB, dLicenseNo) values (4, 'Jean', 'Chevin', '1838 Derek Terrace', '625-887-6472', '12-Apr-1984', '0849voay290');
insert into Client (clientNo, fName, lName, address, phoneNo, DOB, dLicenseNo) values (5, 'Olive', 'Laight', '3707 Forest Dale Road', '774-781-4903', '23-Nov-1981', '4293syxw940');
```

![Final%20Project%202a4067fb3de3414f9a37c966055a2877/Screen_Shot_2020-12-04_at_5.32.12_PM.png](Final%20Project%202a4067fb3de3414f9a37c966055a2877/Screen_Shot_2020-12-04_at_5.32.12_PM.png)

```sql
insert into Staff (staffNo, fName, lName, address, phoneNo, dob, sex, jobTitle, dateHired, salary, outletNo) values (1, 'Genevieve', 'Ormesher', '569 Summit Crossing', '163-934-0295', '31-May-1986', 'F', 'Quality Engineer', '15-Feb-2020', 77991, 1);
insert into Staff (staffNo, fName, lName, address, phoneNo, dob, sex, jobTitle, dateHired, salary, outletNo) values (2, 'Amos', 'Myring', '5 Crest Line Lane', '690-494-2203', '21-Oct-1991', 'M', 'Tax Accountant', '26-Jun-2020', 59798, 2);
insert into Staff (staffNo, fName, lName, address, phoneNo, dob, sex, jobTitle, dateHired, salary, outletNo) values (3, 'Deni', 'Kirsche', '39 Sundown Drive', '365-554-8022', '19-Sep-1990', 'F', 'Actuary', '27-Dec-2019', 73845, 3);
insert into Staff (staffNo, fName, lName, address, phoneNo, dob, sex, jobTitle, dateHired, salary, outletNo) values (4, 'Christyna', 'Kearford', '02982 Dixon Plaza', '752-342-5785', '05-May-1992', 'F', 'Software Consultant', '19-May-2020', 78074, 4);
insert into Staff (staffNo, fName, lName, address, phoneNo, dob, sex, jobTitle, dateHired, salary, outletNo) values (5, 'Valma', 'Bromilow', '1752 Paget Junction', '262-555-1575', '28-Aug-1981', 'F', 'Operator', '07-Mar-2020', 51837, 5);
```

![Final%20Project%202a4067fb3de3414f9a37c966055a2877/Screen_Shot_2020-12-04_at_5.33.57_PM.png](Final%20Project%202a4067fb3de3414f9a37c966055a2877/Screen_Shot_2020-12-04_at_5.33.57_PM.png)

```sql
insert into Vehicle (regNo, make, model, engineSize, capacity, currentMileage, dailyRate, outletNo) values (1, 'Audi', 'TT', '2l', 5, 35019, 29, 1);
insert into Vehicle (regNo, make, model, engineSize, capacity, currentMileage, dailyRate, outletNo) values (2, 'Eagle', 'Vision', '2l', 4, 39441, 44, 2);
insert into Vehicle (regNo, make, model, engineSize, capacity, currentMileage, dailyRate, outletNo) values (3, 'Geo', 'Prizm', '2l', 6, 26925, 44, 3);
insert into Vehicle (regNo, make, model, engineSize, capacity, currentMileage, dailyRate, outletNo) values (4, 'Pontiac', 'G6', '2l', 4, 24049, 44, 4);
insert into Vehicle (regNo, make, model, engineSize, capacity, currentMileage, dailyRate, outletNo) values (5, 'Toyota', 'Tercel', '2l', 6, 28147, 34, 5);
```

![Final%20Project%202a4067fb3de3414f9a37c966055a2877/Screen_Shot_2020-12-04_at_5.36.25_PM.png](Final%20Project%202a4067fb3de3414f9a37c966055a2877/Screen_Shot_2020-12-04_at_5.36.25_PM.png)

```sql
insert into HireAgreement (hireNo, fName, lName, rentalStarted, returnBy, startMileage, endMileage, regNo) values (1, 'Cadillac', 'Escalade EXT', '27-May-2020', 2020-02-19 07:00:00 UTC, 23731, 49973, 1);
insert into HireAgreement (hireNo, fName, lName, rentalStarted, returnBy, startMileage, endMileage, regNo) values (2, 'Infiniti', 'M', '06-Jun-2020', 2020-03-27 06:27:08 UTC, 25619, 47167, 2);
insert into HireAgreement (hireNo, fName, lName, rentalStarted, returnBy, startMileage, endMileage, regNo) values (3, 'Buick', 'Century', '15-Sep-2020', 2020-05-09 03:04:33 UTC, 22488, 44008, 3);
insert into HireAgreement (hireNo, fName, lName, rentalStarted, returnBy, startMileage, endMileage, regNo) values (4, 'Volkswagen', 'Touareg', '27-May-2020', 2020-04-27 05:08:21 UTC, 24660, 31353, 4);
insert into HireAgreement (hireNo, fName, lName, rentalStarted, returnBy, startMileage, endMileage, regNo) values (5, 'Infiniti', 'M', '01-Feb-2020', 2020-07-30 11:23:29 UTC, 24876, 49189, 5);
```

c.  Develop 5 SQL queries using embedded SQL (see Python tutorial).

![Final%20Project%202a4067fb3de3414f9a37c966055a2877/Screen_Shot_2020-12-04_at_5.25.48_PM.png](Final%20Project%202a4067fb3de3414f9a37c966055a2877/Screen_Shot_2020-12-04_at_5.25.48_PM.png)

![Final%20Project%202a4067fb3de3414f9a37c966055a2877/Screen_Shot_2020-12-04_at_5.25.57_PM.png](Final%20Project%202a4067fb3de3414f9a37c966055a2877/Screen_Shot_2020-12-04_at_5.25.57_PM.png)

![Final%20Project%202a4067fb3de3414f9a37c966055a2877/Screen_Shot_2020-12-04_at_5.26.05_PM.png](Final%20Project%202a4067fb3de3414f9a37c966055a2877/Screen_Shot_2020-12-04_at_5.26.05_PM.png)

![Final%20Project%202a4067fb3de3414f9a37c966055a2877/Screen_Shot_2020-12-04_at_5.26.14_PM.png](Final%20Project%202a4067fb3de3414f9a37c966055a2877/Screen_Shot_2020-12-04_at_5.26.14_PM.png)

---

d.  Upload all the code to GitHub.

[Github.com](http://github.com)/frank8922/CSC423 located in the final project folder
