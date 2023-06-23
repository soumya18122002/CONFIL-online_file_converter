-- Active: 1666901497263@@127.0.0.1@3306@confil_register

CREATE DATABASE confil_register;

CREATE TABLE
    visitor_details(
        Visitor_ID INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        Visitor_Name VARCHAR(100) NOT NULL,
        Email VARCHAR(100) NOT NULL,
        Passwords VARCHAR(50) NOT NULL,
        Confirm_passwords VARCHAR(50) NOT NULL,
        Phone_Number VARCHAR(15) NOT NULL,
        Dob DATE NOT NULL,
        Gender VARCHAR(50) NOT NULL,
        Street_address VARCHAR(1000) NOT NULL,
        Street_address2 VARCHAR(1000) NOT NULL,
        Country VARCHAR(200) NOT NULL,
        City VARCHAR(200) NOT NULL,
        Region VARCHAR(200) NOT NULL,
        Postal_Code VARCHAR(200) NOT NULL
    );

DESC visitor_details;

SELECT * FROM visitor_details;