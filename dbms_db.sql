USE dbms;
CREATE TABLE rooms(room_no INT(4),room_cost INT(5));
CREATE TABLE book(booked_room INT,cust_name VARCHAR(30),booked_date DATE);
CREATE TABLE food(food_id INT(5),food_name VARCHAR(50),food_timing VARCHAR(20));