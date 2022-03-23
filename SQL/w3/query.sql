/* Connect to sqlex database
   Exercises from w3 
   https://www.w3resource.com/sql-exercises/
*/

/* PART 1. Retrieve data from tables. */

/* Ex. 1.  
   Write a SQL statement to display all the information of all salesmen.
*/

SELECT * FROM salesman;

/* Ex. 2.  
   Write a SQL statement to display a string "This is SQL Exercise, Practice and Solution".
*/

SELECT 'This is SQL Exercise, Practice and Solution';

/* Ex. 3.  
   Write a query to display three numbers in three columns.
*/

SELECT 1, 2, 3;

SELECT 1 AS cl1, 2 AS cl2, 3 AS cl3;

/* Ex. 4.  
   Write a query to display the sum of two numbers 10 and 15 from RDMS sever.
*/

SELECT 10 + 15;

/* Ex. 5.  
   Write a query to display the result of an arithmetic expression.
*/

SELECT (10 + 15) * 20;

/* Ex. 6.  
   Write a SQL statement to display specific columns like name and commission for all the salesmen.
   Sample table: salesman
*/

SELECT name, commission FROM salesman;

/* Ex. 7.  
   Write a query to display the columns in a specific order like order date, salesman id, order number and purchase amount from for all the orders.
   Sample table: orders
*/

SELECT ord_date AS "order date", salesman_id AS "salesman id", ord_no AS "order number", purch_amt AS "purchase amount" FROM orders;

/* Ex. 8.  
   Write a query which will retrieve the value of salesman id of all salesmen, getting orders from the customers in orders table without any repeats.   
   Sample table: orders
*/

SELECT DISTINCT salesman_id FROM orders;

/* Ex. 9.  
   Write a SQL statement to display names and city of salesman, who belongs to the city of Paris.   
   Sample table: salesman
*/

SELECT name, city FROM salesman
 WHERE city = 'Paris';

/* Ex. 10.  
   Write a SQL statement to display all the information for those customers with a grade of 200.   
   Sample table: customer
*/

SELECT * 
  FROM customer
 WHERE grade = 200;

/* Ex. 11.  
    Write a SQL query to display the order number followed by order date and the purchase amount for each order which will be delivered 
	by the salesman who is holding the ID 5001.   
	Sample table: orders
*/

SELECT ord_no, ord_date, purch_amt
  FROM orders
 WHERE salesman_id = 5001;

/* Ex. 12.  
    Write a SQL query to display the Nobel prizes for 1970.
	Sample table: nobel_win
*/

SELECT *
  FROM nobel_win
 WHERE year = 1970;

/* Ex. 13.  
    Write a SQL query to know the winner of the 1971 prize for Literature.
	Sample table: nobel_win
*/

SELECT winner
  FROM nobel_win
 WHERE year = 1971
   AND subject = 'Literature';

/* Ex. 14.  
    Write a SQL query to display the year and subject that won 'Dennis Gabor' his prize.
	Sample table: nobel_win
*/

SELECT year, subject
  FROM nobel_win
 WHERE winner = 'Dennis Gabor';

/* Ex. 15.  
    Write a SQL query to give the name of the 'Physics' winners since the year 1950.   
	Sample table: nobel_win
*/

SELECT winner
  FROM nobel_win
 WHERE subject = 'Physics'
   AND year >= 1950;

/* Ex. 16.  
    Write a SQL query to Show all the details (year, subject, winner, country ) of the Chemistry prize winners between the year 1965 to 1975 inclusive.
	Sample table: nobel_win
*/

SELECT year, subject, winner, country
  FROM nobel_win
 WHERE year BETWEEN 1965 AND 1975
   AND subject = 'Chemistry';

/* Ex. 17.  
    Write a SQL query to show all details of the Prime Ministerial winners after 1972 of Menachem Begin and Yitzhak Rabin.  
	Sample table: nobel_win
*/

SELECT * 
  FROM nobel_win
 WHERE year > 1972 
   AND (winner = 'Menachem Begin' OR winner = 'Yitzhak Rabin');

/* Ex. 18.  
    Write a SQL query to show all the details of the winners with first name Louis.    
	Sample table: nobel_win
*/

SELECT *
  FROM nobel_win
 WHERE winner LIKE 'Louis %';

/* Ex. 19.  
    Write a SQL query to show all the winners in Physics for 1970 together with the winner of Economics for 1971.   
	Sample table: nobel_win
*/

SELECT winner
  FROM nobel_win
 WHERE (year = 1970 AND subject = 'Physics')
    OR (year = 1971 AND subject = 'Economics');

/* Ex. 20.  
    Write a SQL query to show all the winners of nobel prize in the year 1970 except the subject Physiology and Economics.   
	Sample table: nobel_win
*/

SELECT winner
  FROM nobel_win
 WHERE year = 1970 
  AND  subject <> 'Physiology'
  AND  subject <> 'Economics';

SELECT winner
  FROM nobel_win
 WHERE year = 1970 
   AND subject NOT IN ('Physiology', 'Economics');

/* Ex. 21.  
    Write a SQL query to show the winners of a 'Physiology' prize in an early year before 1971 together with winners of a 'Peace' prize 
	in a later year on and after the 1974. 
	Sample table: nobel_win
*/

SELECT winner
  FROM nobel_win
 WHERE (year < 1971 AND subject = 'Physiology')
    OR (year > 1974 AND subject = 'Peace');

SELECT winner
  FROM nobel_win
 WHERE (year < 1971 AND subject = 'Physiology')
 UNION (SELECT winner 
		  FROM nobel_win 
		 WHERE (year > 1974 AND subject = 'Peace'));

/* Ex. 22.  
   Write a SQL query to find all details of the prize won by Johannes Georg Bednorz. 
   Sample table: nobel_win
*/

SELECT *
  FROM nobel_win
 WHERE winner = 'Johannes Georg Bednorz';

/* Ex. 23.  
   Write a SQL query to find all the details of the nobel winners for the subject not started with the letter 'P' and 
   arranged the list as the most recent comes first, then by name in order.    
   Sample table: nobel_win
*/

SELECT *
  FROM nobel_win
 WHERE subject NOT LIKE 'P%'
 ORDER BY year DESC, winner; 

/* Ex. 24.  
   Write a SQL query to find all the details of 1970 winners by the ordered to subject and winner name; 
   but the list contain the subject Economics and Chemistry at last.    
   Sample table: nobel_win
*/

-- 1
SELECT *
  FROM nobel_win
 WHERE year = 1970
 ORDER BY 
		 CASE 
		 WHEN subject IN('Chemistry', 'Economics') THEN 1
		 ELSE 0
		 END ASC,
		 subject,
		 winner;
		 
-- 2
(SELECT *
   FROM nobel_win
  WHERE year = 1970
    AND subject NOT IN ('Chemistry', 'Economics')
  ORDER BY subject, winner)

  UNION ALL

(SELECT * 
   FROM nobel_win
  WHERE year = 1970
    AND subject IN ('Chemistry', 'Economics')
  ORDER BY  subject ASC, winner);

/* Ex. 25.  
   Write a SQL query to find all the products with a price between Rs.200 and Rs.600.    
   Sample table: item_mast
*/

SELECT pro_name 
  FROM item_mast
 WHERE pro_price BETWEEN 200 AND 600;

/* Ex. 26.  
   Write a SQL query to calculate the average price of all products of the manufacturer which code is 16.    
   Sample table: item_mast
*/

SELECT ROUND(AVG(pro_price), 2) AS avg_price
  FROM item_mast
 WHERE pro_com = 16;

/* Ex. 27.  
   Write a SQL query to find the item name and price in Rs.    
   Sample table: item_mast
*/

SELECT pro_name AS "Item name", pro_price AS "Price, Rs"
  FROM item_mast;

/* Ex. 28.  
   Write a SQL query to display the name and price of all the items with a price is equal or more than Rs.250, 
   and the list contain the larger price first and then by name in ascending order.    
   Sample table: item_mast
*/

SELECT pro_name AS "Name", pro_price AS "Price"
  FROM item_mast
 WHERE pro_price >= 250
 ORDER BY pro_price DESC, pro_name; 

/* Ex. 29.  
   Write a SQL query to display the average price of the items for each company, showing only the company code.  
   Sample table: item_mast
*/

SELECT pro_com, ROUND(AVG(pro_price), 2) 
  FROM item_mast
 GROUP BY pro_com;

/* Ex. 30.  
   Write a SQL query to find the name and price of the cheapest item(s).  
   Sample table: item_mast
*/

SELECT pro_name, pro_price
  FROM item_mast
 WHERE pro_price = (SELECT MIN(pro_price) FROM item_mast);

/* Ex. 31.  
   Write a query in SQL to find the last name of all employees, without duplicates.   
   Sample table: emp_details
*/

SELECT DISTINCT emp_lname 
  FROM emp_details;

/* Ex. 32.  
   Write a query in SQL to find the data of employees whose last name is 'Snares'.  
   Sample table: emp_details
*/

SELECT *
  FROM emp_details 
 WHERE emp_lname = 'Snares';

/* Ex. 33.  
   Write a query in SQL to display all the data of employees that work in the department 57.   
   Sample table: emp_details
*/

SELECT * 
  FROM emp_details
 WHERE emp_dept = 57;


/* PART 2. Using Boolean and Relational operators. */

/* Ex. 1.  
   Write a query to display all customers with a grade above 100.   
   Sample table: customer
*/

SELECT cust_name AS "Customer", grade AS "Grade"
  FROM customer
 WHERE grade > 100;

/* Ex. 2.  
   Write a query statement to display all customers in New York who have a grade value above 100.    
   Sample table: customer
*/

SELECT cust_name AS "Customer",
       city AS "City",
	   grade AS "Grade"
  FROM customer
 WHERE city = 'New York'
   AND grade > 100;

/* Ex. 3.  
   Write a SQL statement to display all customers, who are either belongs to the city New York or had a grade above 100.    
   Sample table: customer
*/

SELECT cust_name AS "Customer",
	   city AS "City",
	   grade AS "Grade"
  FROM customer
 WHERE city = 'New York'
    OR grade > 100;

/* Ex. 4.  
   Write a SQL statement to display all the customers, who are either belongs to the city New York or not had a grade above 100.    
   Sample table: customer
*/

-- 1
SELECT cust_name AS "Customer",
       city AS "City",
	   grade AS "Grade"
  FROM customer
 WHERE city = 'New York'
    OR grade <= 100;
	
-- 2
SELECT cust_name AS "Customer",
       city AS "City",
	   grade AS "Grade"
  FROM customer
 WHERE city = 'New York'
    OR NOT grade > 100;
 
/* Ex. 5.  
   Write a SQL query to display those customers who are neither belongs to the city New York nor grade value is more than 100.    
   Sample table: customer
*/

-- 1
SELECT cust_name AS "Customer",
       city AS "City",
	   grade AS "Grade"
  FROM customer
 WHERE city <> 'New York'
   AND grade <= 100;

-- 2 
SELECT cust_name AS "Customer",
       city AS "City",
	   grade AS "Grade"
  FROM customer
 WHERE NOT (city = 'New York' OR grade > 100);
 
/* Ex. 6.  
   Write a SQL statement to display 
   either those orders which are not issued on date 2012-09-10 and issued by the salesman whose ID is 5005 and below 
   or those orders which purchase amount is 1000.00 and below.   
   Sample table : orders
*/

SELECT *
  FROM orders
 WHERE NOT ((ord_date = '2012-09-10'
   AND salesman_id > 5005)
   OR purch_amt > 1000);

/* Ex. 7.  
   Write a SQL statement to display salesman_id, name, city and commission 
   who gets the commission within the range more than 0.10% and less than 0.12%.  
   Sample table : salesman
*/

SELECT salesman_id AS "ID", 
       name AS "Name", 
	   city AS "City", 
	   commission AS "Commission"
  FROM salesman
 WHERE commission > 0.1
   AND commission < 0.12;
   
/* Ex. 8.  
   Write a SQL query to display all orders where purchase amount less than 200 
   or exclude those orders which order date is on or greater than 10th Feb,2012 
   and customer id is below 3009. 
   Sample table : orders
*/   

SELECT *
 FROM orders
WHERE purch_amt < 200
   OR NOT (ord_date >= '2012-02-10' 
  AND customer_id < 3009);

/* Ex. 9.  
   Write a SQL statement to exclude the rows which satisfy 
   1) order dates are 2012-08-17 and purchase amount is below 1000 
   2) customer id is greater than 3005 and purchase amount is below 1000.  
   Sample table : orders
*/   

SELECT *
  FROM orders
 WHERE NOT ((ord_date = '2012-08-17' 
   AND purch_amt < 1000)
    OR (customer_id > 3005
   AND purch_amt < 1000));

/* Ex. 10.  
   Write a SQL query to display order number, purchase amount, achieved, the unachieved percentage 
   for those order which exceeds the 50% of the target value of 6000.   
   Sample table: orders
*/   

SELECT ord_no AS "Order number",
       purch_amt AS "Purchase amount",
	   ROUND(purch_amt*100/6000, 2) AS "Achieved percentage",
	   100 - ROUND(purch_amt*100/6000, 2) AS "Unachieved percentage"
  FROM orders
 WHERE purch_amt*100/6000 > 50;

/* Ex. 11.  
   Write a query in SQL to find the data of employees whose last name is Dosni or Mardy.    
   Sample table : emp_details
*/   

-- 1
SELECT *
  FROM emp_details
 WHERE emp_lname = 'Dosni'
    OR emp_lname = 'Mardy';
	
-- 2
SELECT *
  FROM emp_details
 WHERE emp_lname IN ('Dosni', 'Mardy');

/* Ex. 12.  
   Write a query in SQL to display all the data of employees that work in department 47 or department 63. 
   Sample table : emp_details
*/   

-- 1
SELECT *
  FROM emp_details
 WHERE emp_dept = 47
    OR emp_dept = 63;
	
-- 2 
SELECT *
  FROM emp_details
 WHERE emp_dept IN (47, 63);
 
/* PART 3. Wildcard and Special operators. */

/* Ex. 1.  
   Write a SQL statement to find those salesmen with all information who come from the city either Paris or Rome.   
   Sample table: salesman
*/ 

-- 1
SELECT *
  FROM salesman
 WHERE city = 'Paris'
    OR city = 'Rome';

-- 2
SELECT *
  FROM salesman
 WHERE city IN ('Paris', 'Rome');

/* Ex. 2.  
   Write a query to filter those salesmen with all information who comes from any of the cities Paris and Rome.  
   Sample table: salesman
*/ 

-- The same (Ex. 1)

/* Ex. 3.  
   Write a query to produce a list of salesman_id, name, city and commission of each salesman who live in cities other than Paris and Rome.   
   Sample table: salesman
*/ 

-- 1
SELECT *
  FROM salesman
 WHERE NOT (city = 'Paris' 
    OR city = 'Rome');
	
-- 2
SELECT *
  FROM salesman
 WHERE NOT city IN ('Paris', 'Rome');

-- 3 
SELECT *
  FROM salesman
 WHERE city NOT IN ('Paris', 'Rome');

/* Ex. 4.  
   Write a query to sort out those customers with all information whose ID value is within any of 3007, 3008 and 3009.   
   Sample table: customer
*/ 

-- 1
SELECT *
  FROM customer
 WHERE customer_id IN (3007, 3008, 3009); 

-- 2
SELECT *
  FROM customer
 WHERE customer_id BETWEEN 3007 AND 3009;

-- 3
SELECT *
  FROM customer
 WHERE customer_id <= 3009 
   AND customer_id >= 3007;

/* Ex. 5.  
   Write a SQL statement to find those salesmen with all information who gets the commission within a range of 0.12 and 0.14.    
   Sample table: salesman
*/ 

-- 1
SELECT *
  FROM salesman
 WHERE commission BETWEEN 0.12 AND 0.14;

-- 2
SELECT *
  FROM salesman
 WHERE commission >= 0.12 
   AND commission <= 0.14;

/* Ex. 6.  
   Write a query to filter all those orders with all information which purchase amount value is within the range 500 and 4000
   except those orders of purchase amount value 948.50 and 1983.43.   
   Sample table: orders
*/ 

-- 1
SELECT *
  FROM orders
 WHERE purch_amt BETWEEN 500 AND 4000
   AND purch_amt <> 948.50
   AND purch_amt <> 1983.43;
   
-- 2 
SELECT *
  FROM orders
 WHERE purch_amt BETWEEN 500 AND 4000
   AND purch_amt NOT IN (948.50, 1983.43);

-- 3
SELECT *
  FROM orders
 WHERE purch_amt BETWEEN 500 AND 4000
EXCEPT
SELECT *
  FROM orders
 WHERE purch_amt IN (948.50, 1983.43);

/* Ex. 7.  
   Write a SQL statement to find those salesmen with all other information and name started with any letter within 'A' and 'L' (not inclusive).   
   Sample table: salesman
*/ 

-- 1
SELECT *
  FROM salesman
 WHERE name BETWEEN 'A' AND 'K';

-- 2
SELECT *
  FROM salesman
 WHERE name >= 'A%'
   AND name < 'L%';

-- 3
SELECT *
  FROM salesman
 WHERE name SIMILAR TO '[A-K]%';
 
-- I. The traditional SQL LIKE operator (the fastest, work everywhere)

-- Classical LIKE operator does not have enough wildcards to execute in one expression.  

-- II. The SIMILAR TO operator (oportunities and speed between LIKE and regular expressiones, work in the most cases)

SELECT *
  FROM salesman
 WHERE name SIMILAR TO '[A-K]%';

-- III. POSIX-style regular expressiones (more flexible, slower, nuancies in work with different SQL)

SELECT *
  FROM salesman
 WHERE name ~ '^[A-K]'; 

/* Ex. 8.  
   Write a SQL statement to find those salesmen with all other information and name started with other than any latter within 'A' and 'L' (not inclusive).    
   Sample table: salesman
*/ 

-- 1
SELECT *
FROM salesman
WHERE name BETWEEN 'M' AND 'Z';

-- 2
SELECT *
  FROM salesman
 WHERE name >= 'M%';

-- 3
SELECT *
  FROM salesman
 WHERE name SIMILAR TO '[M-Z]%';
 
-- I. The traditional SQL LIKE operator (the fastest, work everywhere)

-- Classical LIKE operator does not have enough wildcards to execute in one expression.  

-- II. The SIMILAR TO operator (oportunities and speed between LIKE and regular expressiones, work in the most cases)
SELECT *
  FROM salesman
 WHERE name SIMILAR TO '[M-Z]%';

-- III. POSIX-style regular expressiones (more flexible, slower, nuancies in work with different SQL)
SELECT *
  FROM salesman
 WHERE name ~ '^[M-Z]';

/* Ex. 9.  
   Write a SQL statement to find that customer with all information whose name begin with the letter 'B'.   
   Sample table: customer
*/ 

-- 1 The traditional SQL LIKE operator
SELECT *
  FROM customer
 WHERE cust_name LIKE 'B%';

-- 2 The SIMILAR TO operator 
SELECT *
  FROM customer
 WHERE cust_name SIMILAR TO 'B%';

-- 3 POSIX-style regular expressiones 
SELECT *
FROM customer
WHERE cust_name ~ '^B';
 
-- 4
SELECT *
  FROM customer
 WHERE LEFT(cust_name, 1) = 'B';

/* Ex. 10.  
   Write a SQL statement to find all those customers with all information whose names are ending with the letter 'n'.   
   Sample table: customer
*/ 

-- 1
SELECT *
  FROM customer
 WHERE RIGHT(cust_name, 1) = 'n';

-- 2 LIKE 
SELECT *
  FROM customer
 WHERE cust_name LIKE '%n';

-- 3 SIMILAR TO 
SELECT *
  FROM customer
 WHERE cust_name SIMILAR TO '%n';
 
-- 4 RegEx
SELECT *
FROM customer
WHERE cust_name ~ 'n$';

/* Ex. 11.  
   Write a SQL statement to find those salesmen with all information whose name containing 
   the 1st character is 'N' and the 4th character is 'l' and rests may be any character.  
   Sample table : salesman
*/ 

-- 1 LIKE
SELECT *
  FROM salesman
 WHERE name LIKE 'N__l%';

-- 2 SIMILAR TO
SELECT *
  FROM salesman
 WHERE name SIMILAR TO 'N__l%';

-- 3 RegEx
SELECT *
  FROM salesman
 WHERE name ~ '^N.{2}l';

SELECT *
  FROM salesman
 WHERE name ~ '^N..l';
 
/* Ex. 12.  
   Write a SQL statement to find those rows from the table testtable which contain the escape character underscore ( _ ) in its column 'col1'.  
   Sample table: testtable
*/ 

-- 1 SIMILAR TO
SELECT *
  FROM testtable
 WHERE col1 SIMILAR TO '%[_]%';

-- 2 LIKE
SELECT *
  FROM testtable
 WHERE col1 LIKE '%/_%' ESCAPE '/';
 
-- 3 RegEx
SELECT *
  FROM testtable
 WHERE col1 ~ '_';
 
/* Ex. 13.  
   Write a SQL statement to find those rows from the table testtable which does not contain the character underscore ( _ ) in its column 'col1'.  
   Sample table: testtable
*/ 

-- 1 SIMILAR TO
SELECT *
  FROM testtable
 WHERE col1 NOT SIMILAR TO '%[_]%';

-- 2 LIKE
SELECT *
  FROM testtable
 WHERE col1 NOT LIKE '%/_%' ESCAPE '/';

-- 3 RegEx
SELECT *
  FROM testtable
 WHERE col1 !~ '_'; 

/* Ex. 14.  
   Write a SQL statement to find those rows from the table testtable which contain the escape character ( / ) in its column 'col1'.   
   Sample table: testtable
*/ 

SELECT * 
  FROM testtable
 LIMIT 20;

-- 1 LIKE
SELECT *
  FROM testtable
 WHERE col1 LIKE '%/%';

-- 2 SIMILAR TO
SELECT *
  FROM testtable
 WHERE col1 SIMILAR TO '%/%';

-- 3 SIMILAR TO
SELECT *
  FROM testtable
 WHERE col1 SIMILAR TO '%[/]%';
 
 -- 4 RegEx
SELECT *
  FROM testtable
 WHERE col1 ~ '/';
 
/* Ex. 15.  
   Write a SQL statement to find those rows from the table testtable which does not contain the escape character ( / ) in its column 'col1'.  
   Sample table: testtable
*/ 

-- 1 LIKE
SELECT *
  FROM testtable
 WHERE col1 NOT LIKE '%/%';

-- 2 SIMILAR TO
SELECT *
  FROM testtable
 WHERE col1 NOT SIMILAR TO '%/%';
 
-- 3 RegEx
SELECT *
  FROM testtable
 WHERE col1 !~ '/';

/* Ex. 16.  
   Write a SQL statement to find those rows from the table testtable which contain the string ( _/ ) in its column 'col1'.   
   Sample table: testtable
*/ 

-- 1 SIMILAR TO
SELECT *
  FROM testtable
 WHERE col1 SIMILAR TO '%#_/%' ESCAPE '#';

-- 2 LIKE
SELECT *
  FROM testtable
 WHERE col1 LIKE '%#_/%' ESCAPE '#';

-- 3 RegEx
SELECT *
  FROM testtable
 WHERE col1 ~ '_/'; 

/* Ex. 17.  
   From the following table, write a SQL query to find those rows where col1 does not contain the string ( _/ ). Return col1.  
   Sample table: testtable
*/ 

-- 1 LIKE
SELECT *
  FROM testtable
 WHERE col1 NOT LIKE '%#_/%' ESCAPE '#';

-- 2 SIMILAR TO
SELECT *
  FROM testtable
 WHERE col1 NOT SIMILAR TO '%#_/%' ESCAPE '#';

-- 3 RegEx
SELECT *
  FROM testtable
 WHERE col1 !~ '_/';

/* Ex. 18.  
   From the following table, write a SQL query to find those rows where col1 contains the character percent ( % ). Return col1.   
   Sample table: testtable
*/ 

SELECT *
FROM testtable
LIMIT 20;

-- 1 LIKE TO
SELECT *
  FROM testtable
 WHERE col1 LIKE '%#%%' ESCAPE '#';

-- 2 SIMILAR TO
SELECT *
  FROM testtable
 WHERE col1 SIMILAR TO '%#%%' ESCAPE '#';

-- 3 RegEx
SELECT *
  FROM testtable
 WHERE col1 ~ '%';

/* Ex. 19.  
   From the following table, write a SQL query to find those rows where col1 does not contain the character percent ( % ). Return col1.  
   Sample table: testtable
*/ 

-- 1 LIKE 
SELECT * 
  FROM testtable
  WHERE col1 NOT LIKE '%#%%' ESCAPE '#';

-- 2 SIMILAR TO
SELECT *
  FROM testtable
 WHERE col1 NOT SIMILAR TO '%#%%' ESCAPE '#';

-- 3 RegEx
SELECT *
  FROM testtable
 WHERE col1 !~ '%';

/* Ex. 20.  
   From the following table, write a SQL query to find all those customers who does not have any grade. 
   Return customer_id, cust_name, city, grade, salesman_id.
   Sample table: customer
*/ 

SELECT *
  FROM customer
 WHERE grade IS NULL;

/* Ex. 21.  
   From the following table, write a SQL query to find all those customers whose grade value exists. 
   Return customer_id, cust_name, city, grade, salesman_id.   
   Sample table: customer
*/ 

SELECT *
  FROM customer
 WHERE grade IS NOT NULL;

/* Ex. 22.  
   From the following table, write a SQL query to find the employees whose last name begins with the character 'D'. 
   Return emp_idno, emp_fname, emp_lname and emp_dept. 
   Sample table: emp_details
*/ 

SELECT *
FROM emp_details
LIMIT 20;

-- 1 LIKE
SELECT *
  FROM emp_details
 WHERE emp_lname LIKE 'D%';

-- 2 SIMILAR TO
SELECT *
  FROM emp_details
 WHERE emp_lname SIMILAR TO 'D%';

-- 3 REGEX
SELECT *
  FROM emp_details
 WHERE emp_lname ~ '^D';

/* PART 4. Aggregate Functions. */

/* Ex. 1. 
   From the following table, write a SQL query to calculate total purchase amount of all orders. Return total purchase amount.   
   Sample table: orders  
*/ 
SELECT SUM(purch_amt) AS total_purch_amt
  FROM orders;

/* Ex. 2. 
   From the following table, write a SQL query to calculate average purchase amount of all orders. Return average purchase amount.   
   Sample table: orders 
*/ 

SELECT AVG(purch_amt) AS avg_purch_amt
  FROM orders;

/* Ex. 3. 
   From the following table, write a SQL query to count the number of unique salespeople. Return number of salespeople.   
   Sample table: orders 
*/ 

SELECT COUNT(DISTINCT salesman_id) AS count_salesman
  FROM orders;

/* Ex. 4. 
   From the following table, write a SQL query to count the number of customers. Return number of customers.   
   Sample table: customer 
*/ 

-- 1
SELECT COUNT(customer_id) AS count_customer
  FROM customer;
  
-- 2
SELECT COUNT(DISTINCT cust_name) AS count_customer
  FROM customer;

-- 3
SELECT COUNT(*) AS count_customer
  FROM customer;

/* Ex. 5. 
   From the following table, write a SQL query to find the number of customers who got at least a gradation for his/her activity.   
   Sample table: customer 
*/ 

-- 1
SELECT COUNT(*) AS count_cust_with_grade
  FROM customer
 WHERE grade is NOT NULL;

-- 2 
SELECT COUNT(ALL grade) AS count_cust_with_grade
  FROM customer;

/* Ex. 6. 
   From the following table, write a SQL query to find the maximum purchase amount.    
   Sample table: orders 
*/ 

SELECT MAX(purch_amt) AS max_purch_amt
  FROM orders;

/* Ex. 7. 
   From the following table, write a SQL query to find the minimum purchase amount.   
   Sample table: orders
*/ 

SELECT MIN(purch_amt) AS min_purch_amt
  FROM orders;

/* Ex. 8. 
   From the following table, write a SQL query to find the highest grade of the customers for each of the city. 
   Return city, maximum grade.    
   Sample table: customer
*/ 

SELECT city, MAX(grade) AS max_grade_city
  FROM customer
 GROUP BY city
 ORDER BY city;

/* Ex. 9. 
   From the following table, write a SQL query to find the highest purchase amount ordered by each customer. 
   Return customer ID, maximum purchase amount.   
   Sample table: orders
*/ 

SELECT customer_id, MAX(purch_amt) AS max_purch_amt_cust
  FROM orders
 GROUP BY customer_id
 ORDER BY customer_id;

/* Ex. 10. 
   From the following table, write a SQL query to find the highest purchase amount ordered by each customer on a particular date. 
   Return, order date and highest purchase amount.   
   Sample table: orders
*/ 

SELECT customer_id AS "Customer",
       ord_date AS "Date",
	   MAX(purch_amt) AS "Maximum Purch. amt."
  FROM orders
 GROUP BY customer_id, ord_date
 ORDER BY customer_id;

/* Ex. 11. 
   From the following table, write a SQL query to find the highest purchase amount on '2012-08-17' by each salesperson. 
   Return salesperson ID, purchase amount.   
   Sample table: orders
*/ 

SELECT salesman_id AS "Salesperson ID",
	   MAX(purch_amt) AS "Max Amount"
  FROM orders
 WHERE ord_date = '2012-08-17'
 GROUP BY salesman_id;
 
/* Ex. 12. 
   From the following table, write a SQL query to find highest order (purchase) amount by each customer in a particular order date. 
   Filter the result by highest order (purchase) amount above 2000.00. 
   Return customer id, order date and maximum purchase amount.   
   Sample table: orders
*/ 

-- 1
SELECT customer_id AS "Customer",
       ord_date AS "Order Date",
	   MAX(purch_amt) AS "Max Amount"
  FROM orders
 WHERE purch_amt > 2000
 GROUP BY customer_id, ord_date
 ORDER BY ord_date;

-- 2
SELECT customer_id AS "Customer",
       ord_date AS "Order Date",
	   MAX(purch_amt) AS "Max Amount"
  FROM orders
 GROUP BY customer_id, ord_date
HAVING MAX(purch_amt) > 2000
 ORDER BY ord_date;


/* Ex. 13. 
   From the following table, write a SQL query to find the maximum order (purchase) amount in the range 2000, 6000 
   (Begin and end values are included.) by combination of each customer and order date. 
   Return customer id, order date and maximum purchase amount.  
   Sample table: orders
*/ 

SELECT *
FROM orders
LIMIT 20;

SELECT customer_id AS "Customer",
       ord_date AS "Order_date",
	   MAX(purch_amt) AS "Max Amount"
FROM orders
GROUP BY customer_id, ord_date
HAVING MAX(purch_amt) BETWEEN 2000 AND 6000;

/* Ex. 14. 
   From the following table, write a SQL query to find the maximum order (purchase) amount by the combination 
   of each customer and order date. Filter the rows for maximum order (purchase) amount is either 2000, 3000, 5760, 6000. 
   Return customer id, order date and maximum purchase amount.  
   Sample table: orders
*/ 

-- 1
SELECT customer_id AS "Customer",
       ord_date AS "Date",
	   MAX(purch_amt) AS "Max Amount"
  FROM orders
 GROUP BY customer_id, ord_date
HAVING MAX(purch_amt) IN (2000, 3000, 5760, 6000);

-- 2
SELECT customer_id AS "Customer",
       ord_date AS "Date",
	   MAX(purch_amt) AS "Max Amount"
  FROM orders
 WHERE purch_amt IN (2000, 3000, 5760, 6000)
 GROUP BY customer_id, ord_date;

/* Ex. 15. 
   From the following table, write a SQL query to find the maximum order (purchase) amount by each customer. 
   The customer ID should be in the range 3002 and 3007(Begin and end values are included.). 
   Return customer id and maximum purchase amount.  
   Sample table: orders
*/ 

-- 1
SELECT customer_id AS "Customer",
       MAX(purch_amt) AS "Max Amount"
  FROM orders
 GROUP BY customer_id
HAVING customer_id BETWEEN 3002 AND 3007;

-- 2
SELECT customer_id AS "Customer",
       MAX(purch_amt) AS "Max Amount"
  FROM orders
 WHERE customer_id BETWEEN 3002 AND 3007
 GROUP BY customer_id;


/* Ex. 16. 
   From the following table, write a SQL query to find the maximum order (purchase) amount for each customer. 
   The customer ID should be in the range 3002 and 3007(Begin and end values are included.). 
   Filter the rows for maximum order (purchase) amount is higher than 1000. Return customer id and maximum purchase amount.  
   Sample table: orders
*/ 

-- 1
SELECT customer_id AS "Customer",
       MAX(purch_amt) AS "Max Amount"
  FROM orders
 WHERE customer_id BETWEEN 3002 AND 3007
 GROUP BY customer_id
HAVING MAX(purch_amt) > 1000;

-- 2
SELECT customer_id AS "Customer",
       MAX(purch_amt) AS "Max Amount"
  FROM orders
 WHERE (customer_id BETWEEN 3002 AND 3007)
       AND purch_amt > 1000
 GROUP BY customer_id;

/* Ex. 17. 
   From the following table, write a SQL query to find the maximum order (purchase) amount generated by each salesperson. 
   Filter the rows for the salesperson ID is in the range 5003 and 5008 (Begin and end values are included.). 
   Return salesperson id and maximum purchase amount.  
   Sample table: orders
*/ 

-- 1
SELECT salesman_id AS "Salesperson",
       MAX(purch_amt) AS "Max Amount"
  FROM orders
 WHERE salesman_id BETWEEN 5003 AND 5008
 GROUP BY salesman_id;

-- 2
SELECT salesman_id AS "Salesperson",
       MAX(purch_amt) AS "Max Amount"
  FROM  orders
 GROUP BY salesman_id
HAVING salesman_id BETWEEN 5003 AND 5008;

/* Ex. 18. 
   From the following table, write a SQL query to count all the orders generated on '2012-08-17'. Return number of orders.   
   Sample table: orders
*/ 

SELECT COUNT(*) AS "Number of orders"
  FROM orders
 WHERE ord_date = '2012-08-17';

/* Ex. 19. 
   From the following table, write a SQL query to count number of salespeople who belongs to a city. Return number of salespeople.   
   Sample table: salesman
*/ 

SELECT COUNT(*) AS "Salespeople from city"
  FROM salesman
 WHERE city IS NOT NULL;

/* Ex. 20. 
   From the following table, write a SQL query to count number of orders by the combination of each order date and salesperson. 
   Return order date, salesperson id.  
   Sample table: orders
*/ 

SELECT COUNT(*) AS "Number of orders",
       ord_date AS "Date",
	   salesman_id AS "Salesperson"
  FROM orders
 GROUP BY ord_date, salesman_id;
 
/* Ex. 21. 
   From the following table, write a SQL query to calculate the average product price. 
   Return average product price.  
   Sample table: item_mast
*/ 

SELECT AVG(pro_price) AS "Average price"
  FROM item_mast;

/* Ex. 22. 
   From the following table, write a SQL query to count number of products where product price is higher than or equal to 350. 
   Return number of products.  
   Sample table: item_mast
*/ 

SELECT COUNT(*) AS "Num of products"
  FROM item_mast
 WHERE pro_price >= 350;

/* Ex. 23. 
   From the following table, write a SQL query to compute the average price for unique companies. 
   Return average price and company id.  
   Sample table: item_mast
*/ 

SELECT pro_com AS "Company",
       AVG(pro_price) AS "Average price"
  FROM item_mast
 GROUP BY pro_com;
 
/* Ex. 24. 
   From the following table, write a SQL query to compute the sum of the allotment amount of all departments. 
   Return sum of the allotment amount.   
   Sample table: emp_department
*/ 

SELECT SUM(dpt_allotment) AS "Sum of allotment"
FROM emp_department;

/* Ex. 25. 
   From the following table, write a SQL query to find the number of employees in each department. 
   Return department code and number of employees.  
   Sample table: emp_details
*/ 

SELECT emp_dept AS "Department code",
       COUNT(*) AS "Num of empoyees"
  FROM emp_details
 GROUP BY emp_dept;


/* PART 5. Formatting Output. */

/* Ex. 1. 
   From the following table, write a SQL query to select all the salespeople. 
   Return salesman_id, name, city, commission with the percent sign (%).   
   Sample table: salesman
*/ 

-- 1
SELECT salesman_id AS "Salesman",
	   name AS "Name",
	   city AS "City",
	   commission * 100 AS "Commission, %"
  FROM salesman;

-- 2
SELECT salesman_id AS "Salesman",
	   name AS "Name",
	   city AS "City",
	   commission * 100 AS "Commission",
	   '%' AS "Measurement units"
  FROM salesman;

/* Ex. 2. 
   From the following table, write a SQL query to find the number of orders booked for each day. 
   Return the result in a format like "For 2001-10-10 there are 15 orders".".   
   Sample table: orders
*/ 

SELECT 'For',  
       ord_date,
	   'there are',
	   COUNT(*),
       'orders.'
  FROM orders
 GROUP BY ord_date;

/* Ex. 3. 
   From the following table, write a SQL query to find all the orders. Sort the result-set in ascending order by ord_no. 
   Return all fields.    
   Sample table: orders
*/ 

SELECT ord_no AS "Orders",
       purch_amt AS "Purchase Amount",
	   ord_date AS "Date",
	   customer_id AS "Customer",
	   salesman_id AS "Salesman"
  FROM orders
 ORDER BY ord_no ASC;

/* Ex. 4. 
   From the following table, write a SQL query to find all the orders. 
   Sort the result-set in descending order by ord_date. Return all fields.   
   Sample table: orders
*/ 

SELECT ord_no AS "Orders",
       purch_amt AS "Purchase Amount",
	   ord_date AS "Date",
	   customer_id AS "Customer",
	   salesman_id AS "Salesman"
  FROM orders
 ORDER BY ord_date DESC;

/* Ex. 5. 
   From the following table, write a SQL query to find all the orders. 
   Sort the result-set in descending order by ord_date and purch_amt. Return all fields.    
   Sample table: orders
*/ 

SELECT ord_no AS "Orders",
       purch_amt AS "Purchase Amount",
	   ord_date AS "Date",
	   customer_id AS "Customer",
	   salesman_id AS "Salesman"
  FROM orders
 ORDER BY ord_date, purch_amt DESC;

/* Ex. 6. 
   From the following table, write a SQL query to find all the customers. 
   Sort the result-set by customer_id. Return cust_name, city, grade.   
   Sample table: customer
*/ 
SELECT cust_name AS "Customer",
       city AS "City",
	   grade AS "Grade"
  FROM customer
 ORDER BY customer_id;

/* Ex. 7. 
   From the following table, write a SQL query to calculate the maximum purchase amount 
   generated by each sales person for every order date. Sort the result-set by sales 
   person id and order date in ascending order. 
   Return sales person id, order date and maximum purchase amount.  
   Sample table: orders
*/ 

SELECT salesman_id AS "ID",
       ord_date AS "Date",
	   MAX(purch_amt) AS "Max Amount"
  FROM orders
 GROUP BY salesman_id, ord_date
 ORDER BY salesman_id;

/* Ex. 8. 
   From the following table, write a SQL query to find all the customers. 
   Sort the result-set in descending order on 3rd field. Return customer name, city and grade.    
   Sample table: customer
*/ 

-- 1
SELECT cust_name AS "Customer",
       city AS "City",
	   grade AS "Grade"
  FROM customer
 ORDER BY 3 DESC;

-- 2
SELECT cust_name AS "Customer",
       city AS "City",
	   grade AS "Grade"
  FROM customer
 ORDER BY grade DESC;

/* Ex. 9. 
   From the following table, write a SQL query to count the unique orders, highest purchase amount for each customer. 
   Sort the result-set in descending order on 2nd field. Return customer ID, 
   number of distinct orders and highest purchase amount by each customer.   
   Sample table: orders
*/ 

SELECT customer_id AS "ID",
       COUNT(*) AS "Num of orders",
	   MAX(purch_amt) AS "Max Amount"
  FROM orders
 GROUP BY customer_id
 ORDER BY 2 DESC;

/* Ex. 10. 
   From the following table, write a SQL query to calculate summation of purchase amount, 
   total commission (15% for all salesmen) by each order date. Sort the result-set on order date. 
   Return order date, summation of purchase amount and commission.   
   Sample table : orders
*/ 

SELECT ord_date AS "Date",
       SUM(purch_amt) AS "Sum Amount",
	   0.15 * SUM(purch_amt) AS "15% Commision"
  FROM orders
 GROUP BY ord_date
 ORDER BY ord_date;

/* PART 6. Query on Multiple Tables. */

/* Ex. 1. 
   From the following tables, write a SQL query to find the salespersons and customers who live in same city. 
   Return customer name, salesperson name and salesperson city.  
   Sample table: salesman
   Sample table: customer
*/ 

-- 1 JOIN
SELECT c.cust_name AS "Customer name",
       s.name AS "Salesperson name",
	   s.city AS "City"
  FROM salesman AS s
  JOIN customer AS c
    ON s.city = c.city;

-- 2 WHERE
SELECT customer.cust_name AS "Customer name",
       salesman.name AS "Salesperson name",
	   salesman.city AS "Salesperson city"
  FROM customer, salesman
 WHERE salesman.city = customer.city;
       
/* Ex. 2. 
   From the following tables, write a SQL query to find all the customers along with the salesperson who works for them. 
   Return customer name, and salesperson name.   
   Sample table: customer
   Sample table: salesman
*/ 

-- 1 JOIN
SELECT customer.cust_name AS "Customer name",
       salesman.name AS "Salesperson name"
  FROM customer
  JOIN salesman
    ON customer.salesman_id = salesman.salesman_id;

-- 2 WHERE
SELECT customer.cust_name AS "Customer name",
       salesman.name AS "Salesperson name"
  FROM customer, salesman
 WHERE salesman.salesman_id = customer.salesman_id;

/* Ex. 3. 
   From the following tables, write a SQL query to find those sales people who generated orders for their customers 
   but not located in the same city. 
   Return ord_no, cust_name, customer_id (orders table), salesman_id (orders table).   
   Sample table: salesman
   Sample table: customer
   Sample table: orders
*/ 

-- 1 JOIN+WHERE
SELECT orders.ord_no AS "Order number",
       customer.cust_name AS "Customer name",
	   orders.customer_id AS "Customer ID",
	   orders.salesman_id AS "Salesman ID"
  FROM orders
       JOIN salesman
       ON orders.salesman_id = salesman.salesman_id
       JOIN customer
       ON orders.customer_id = customer.customer_id
 WHERE salesman.city != customer.city;

-- 2 JOIN
SELECT orders.ord_no AS "Order number",
       customer.cust_name AS "Customer name",
	   orders.customer_id AS "Customer ID",
	   orders.salesman_id AS "Salesman ID"
  FROM orders
  JOIN salesman
    ON orders.salesman_id = salesman.salesman_id
  JOIN customer
    ON orders.customer_id = customer.customer_id
   AND salesman.city != customer.city;

-- 3 WHERE
SELECT orders.ord_no AS "Order number",
       customer.cust_name AS "Customer name",
	   orders.customer_id AS "Customer ID",
	   orders.salesman_id AS "Salesman ID"
  FROM orders, customer, salesman
 WHERE orders.salesman_id = salesman.salesman_id
   AND orders.customer_id = customer.customer_id  
   AND salesman.city != customer.city;

/* Ex. 4. 
   From the following tables, write a SQL query to find those orders made by customers. 
   Return order number, customer name.   
   Sample table: orders
   Sample table: customer
*/ 

-- JOIN
SELECT o.ord_no AS "Order number",
       c.cust_name AS "Customer name"
  FROM orders AS o
  JOIN customer AS c
    ON o.customer_id = c.customer_id;

-- WHERE
SELECT o.ord_no AS "Order number",
       c.cust_name AS "Customer name"
  FROM orders AS o,
       customer AS c
 WHERE o.customer_id = c.customer_id;

/* Ex. 5. 
   From the following tables, write a SQL query to find those customers where each customer has 
   a grade and served by at least a salesperson who belongs to a city. 
   Return cust_name as "Customer", grade as "Grade".    
   Sample table: salesman
   Sample table: customer
   Sample table: orders
*/ 

-- JOIN + WHERE

SELECT c.cust_name AS "Customer",
       c.grade AS "Grade"
  FROM customer AS c
  JOIN salesman AS s
    ON c.salesman_id = s.salesman_id
 WHERE c.grade IS NOT NULL
   AND s.city IS NOT NULL;	

-- WHERE

SELECT c.cust_name AS "Customer",
	   c.grade AS "Grade"
  FROM customer AS c,
       salesman AS s
 WHERE c.salesman_id = s.salesman_id
   AND c.grade IS NOT NULL
   AND s.city IS NOT NULL;

/* Ex. 6. 
   From the following table, write a SQL query to find those customers who served by a salesperson 
   and the salesperson works at the commission in the range 12% to 14% (Begin and end values are included.). 
   Return cust_name AS "Customer", city AS "City".  
   Sample table: salesman
   Sample table: customer
*/ 

-- JOIN
SELECT c.cust_name AS "Customer",
	   c.city AS "City",
	   s.commission AS "Commision"
  FROM customer AS c
  JOIN salesman AS s
    ON c.salesman_id = s.salesman_id
 WHERE s.commission BETWEEN 12/100.0 AND 14/100.0;

-- WHERE
SELECT c.cust_name AS "Customer",
	   c.city AS "City",
	   s.commission AS "Commision"
  FROM customer AS c,
       salesman AS s
 WHERE c.salesman_id = s.salesman_id
   AND s.commission BETWEEN 12/100.0 AND 14/100.0;

/* Ex. 7. 
   From the following tables, write a SQL query to find those orders executed by the salesperson, 
   ordered by the customer whose grade is greater than or equal to 200. Compute purch_amt*commission as "Commission". 
   Return customer name, commission as "Commission%" and Commission.  
   Sample table: salesman
   Sample table: customer
   Sample table: orders
*/ 

-- JOIN
SELECT c.cust_name AS "Customer",
       o.ord_no AS "Order",
       o.purch_amt * s.commission AS "Commission"
  FROM orders AS o
  JOIN salesman AS s
    ON o.salesman_id = s.salesman_id
  JOIN customer AS c
    ON o.customer_id = c.customer_id
 WHERE c.grade >= 200
   AND c.grade IS NOT NULL;

-- WHERE
SELECT c.cust_name AS "Customer",
       o.ord_no AS "Order",
       o.purch_amt * s.commission AS "Commission"
  FROM orders AS o,
       salesman AS s,
	   customer AS c
 WHERE o.salesman_id = s.salesman_id
   AND o.customer_id = c.customer_id
   AND c.grade >= 200
   AND c.grade IS NOT NULL;

/* Ex. 8. 
   From the following table, write a SQL query to find those customers who made orders on October 5, 2012. 
   Return customer_id, cust_name, city, grade, salesman_id, ord_no, purch_amt, ord_date, customer_id and salesman_id.  
   Sample table: salesman
   Sample table: customer
   Sample table: orders
*/ 

-- JOIN
SELECT * 
  FROM customer AS c
  JOIN orders AS o
    ON c.customer_id = o.customer_id
 WHERE o.ord_date = '2012-10-05';

-- WHERE
SELECT * 
  FROM customer AS c,
       orders AS o
 WHERE c.customer_id = o.customer_id
   AND o.ord_date = '2012-10-05';
 
/* PART 7. JOINS. */

/* Ex. 1. 
   From the following tables write a SQL query to find the salesperson and customer who belongs to same city. 
   Return Salesman, cust_name and city.  
   Sample table: salesman
   Sample table: customer
*/ 

-- JOIN
SELECT s.name AS "Salesman Name",
	   c.cust_name AS "Customer Name",
	   c.city AS "City"
  FROM salesman AS s
  JOIN customer AS c
    ON s.city = c.city;
   
-- WHERE
SELECT s.name AS "Salesman Name",
	   c.cust_name AS "Customer Name",
	   c.city AS "City"
  FROM salesman AS s,
       customer AS c
 WHERE s.city = c.city;
  
/* Ex. 2. 
   From the following tables write a SQL query to find those orders where order amount exists between 500 and 2000. 
   Return ord_no, purch_amt, cust_name, city.  
   Sample table: orders
   Sample table: customer
*/

-- JOIN
SELECT o.ord_no AS "Order Number",
       o.purch_amt AS "Purch Amount",
       c.cust_name AS "Customer Name",
       c.city AS "City"
  FROM orders AS o
  JOIN customer AS c
    ON o.customer_id = c.customer_id 
 WHERE o.purch_amt BETWEEN 500 AND 2000;

-- WHERE
SELECT o.ord_no AS "Order Number",
       o.purch_amt AS "Purch Amount",
       c.cust_name AS "Customer Name",
       c.city AS "City"
  FROM orders AS o, customer AS c
 WHERE o.customer_id = c.customer_id 
   AND o.purch_amt BETWEEN 500 AND 2000;

/* Ex. 3. 
   From the following tables write a SQL query to find the salesperson(s) and the customer(s) he handle. 
   Return Customer Name, city, Salesman, commission.  
   Sample table: customer
   Sample table: salesman
*/ 

-- JOIN
SELECT c.cust_name AS "Customer Name",
       c.city AS "City",
       s.name AS "Salesman Name",
       s.commission AS "Commission"
  FROM customer AS c
  JOIN salesman AS s
    ON c.salesman_id = s.salesman_id; 

-- WHERE
SELECT c.cust_name AS "Customer Name",
       c.city AS "City",
       s.name AS "Salesman Name",
       s.commission AS "Commission"
  FROM customer AS c, salesman AS s
 WHERE c.salesman_id = s.salesman_id; 
 
/* Ex. 4. 
   From the following tables write a SQL query to find those salespersons who received a commission from the company more than 12%. 
   Return Customer Name, customer city, Salesman, commission.   
   Sample table: customer
   Sample table: salesman
*/ 

-- JOIN
SELECT c.cust_name AS "Customer Name",
       c.city AS "City",
       s.name AS "Salesman Name",
       s.commission AS "Commission"
  FROM customer AS c
  JOIN salesman AS s
    ON c.salesman_id = s.salesman_id
 WHERE s.commission > 12/100.0;

-- WHERE
SELECT c.cust_name AS "Customer Name",
       c.city AS "City",
       s.name AS "Salesman Name",
       s.commission AS "Commission"
  FROM customer AS c, salesman AS s
 WHERE c.salesman_id = s.salesman_id
   AND s.commission > 12/100.0;

/* Ex. 5. 
   From the following tables write a SQL query to find those salespersons do not live in the same city 
   where their customers live and received a commission from the company more than 12%. 
   Return Customer Name, customer city, Salesman, salesman city, commission.   
   Sample table: customer
   Sample table: salesman
*/ 

-- JOIN
SELECT c.cust_name AS "Customer Name",
       c.city AS "Customer City",
       s.name AS "Salesman Name",
       s.city AS "Salesman City",
       s.commission AS "Commission"
  FROM customer AS c
  JOIN salesman AS s 
    ON c.salesman_id = s.salesman_id
 WHERE c.city != s.city 
   AND s.commission > 12/100.00;

-- WHERE 
SELECT c.cust_name AS "Customer Name",
       c.city AS "Customer City",
       s.name AS "Salesman Name",
       s.city AS "Salesman City",
       s.commission AS "Commission"
  FROM customer AS c,
       salesman AS s 
 WHERE c.salesman_id = s.salesman_id
   AND c.city != s.city 
   AND s.commission > 12/100.00;

/* Ex. 6. 
   From the following tables write a SQL query to find the details of an order. 
   Return ord_no, ord_date, purch_amt, Customer Name, grade, Salesman, commission. 
   Sample table: orders
   Sample table: customer
   Sample table: salesman
*/ 

-- JOIN
SELECT o.ord_no AS "Order num",
       o.ord_date AS "Order date",
       o.purch_amt AS "Purch amount",
       c.cust_name AS "Customer name",
       c.grade AS "Grade",
       s.name AS "Salesman name",
       s.commission AS "Commission"
  FROM orders AS o
  JOIN customer AS c
    ON o.customer_id = c.customer_id 
  JOIN salesman AS s
    ON o.salesman_id  = s.salesman_id;

-- WHERE
SELECT o.ord_no AS "Order num",
       o.ord_date AS "Order date",
       o.purch_amt AS "Purch amount",
       c.cust_name AS "Customer name",
       c.grade AS "Grade",
       s.name AS "Salesman name",
       s.commission AS "Commission"
  FROM orders AS o,
       customer AS c,
       salesman AS s
 WHERE o.customer_id = c.customer_id 
   AND o.salesman_id  = s.salesman_id;     

/* Ex. 7. 
   Write a SQL statement to make a join on the tables salesman, customer and orders in such a form 
   that the same column of each table will appear once and only the relational rows will come.  
   Sample table: orders
   Sample table: customer
   Sample table : salesman
*/ 

SELECT *
  FROM orders 
NATURAL JOIN customer
NATURAL JOIN salesman;

/* Ex. 8. 
   From the following tables write a SQL query to display the cust_name, customer city, grade, Salesman, salesman city. 
   The result should be ordered by ascending on customer_id.
   Sample table: customer
   Sample table: salesman
*/ 

SELECT c.cust_name AS "Customer Name",
       c.city AS "Customer City",
       c.grade AS "Grade",
       s.name AS "Salesman Name",
       s.city AS "Salesman City"
  FROM customer AS c
  LEFT JOIN salesman AS s 
    ON c.salesman_id = s.salesman_id 
 ORDER BY c.customer_id;

/* Ex. 9. 
   From the following tables write a SQL query to find those customers whose grade less than 300. 
   Return cust_name, customer city, grade, Salesman, saleman city. The result should be ordered by ascending customer_id.  
   Sample table: customer
   Sample table: salesman
*/ 

SELECT c.cust_name AS "Customer Name",
       c.city AS "Customer City",
       c.grade AS "Grade",
       s.name AS "Salesman Name",
       s.city AS "Salesman City",
       c.customer_id 
  FROM customer AS c
  LEFT JOIN salesman AS s 
    ON c.salesman_id = s.salesman_id 
 WHERE c.grade < 300
 ORDER BY c.customer_id;

/* Ex. 10. 
   Write a SQL statement to make a report with customer name, city, order number, order date, and order amount 
   in ascending order according to the order date to find that either any of the existing customers have placed 
   no order or placed one or more orders.  
   Sample table: orders
   Sample table: customer
*/ 

SELECT c.cust_name AS "Customer Name",
       c.city AS "City",
       o.ord_no AS "Order Number",
       o.ord_date AS "Order Date",
       o.purch_amt AS "Order Amount"
  FROM customer AS c
  LEFT JOIN orders AS o 
    ON c.customer_id = o.customer_id 
 ORDER BY o.ord_date;

 /* Ex. 11. 
   Write a SQL statement to make a report with customer name, city, order number, order date, order amount salesman name 
   and commission to find that either any of the existing customers have placed no order or placed one or more orders 
   by their salesman or by own.  
   Sample table: customer
   Sample table: orders
   Sample table: salesman
*/ 

SELECT c.cust_name AS "Customer Name",
       c.city AS "Customer City",
       o.ord_no AS "Order number",
       o.ord_date AS "Order Date",
       o.purch_amt AS "Purch_amt",
       s.commission AS "Commission"
  FROM customer AS c
  LEFT JOIN orders AS o 
    ON c.customer_id  = o.customer_id
  LEFT JOIN salesman AS s 
    ON c.salesman_id = s.salesman_id;

/* Ex. 12. 
   Write a SQL statement to make a list in ascending order for the salesmen who works either for one or more customer 
   or not yet join under any of the customers.  
   Sample table: customer
   Sample table: salesman
*/ 

-- 1   
SELECT name AS "Salesman Name"
  FROM salesman AS s
 ORDER BY name;

-- 2
SELECT DISTINCT s.name AS "Salesman Name"
  FROM salesman AS s
  LEFT JOIN customer AS c
    ON s.salesman_id = c.salesman_id
 ORDER BY s.name;

-- 3 
SELECT DISTINCT s.name AS "Salesman Name"
  FROM customer AS c
 RIGHT JOIN salesman AS s 
    ON c.salesman_id = s.salesman_id 
 ORDER BY s.name;
   
/* Ex. 13. 
   From the following tables write a SQL query to list all salespersons along with customer name, city, grade, order number, date, and amount.  
   Sample table: customer
   Sample table: salesman
   Sample table: orders
*/ 

SELECT s.name AS "Salesman Name",
       c.cust_name AS "Customer Name",
       c.city AS "City",
       c.grade AS "Grade",
       o.ord_no AS "Order number",
       o.ord_date AS "Order date",
       o.purch_amt AS "Purchase amount"
  FROM salesman AS s
  LEFT JOIN customer AS c 
    ON s.salesman_id = c.salesman_id 
  LEFT JOIN orders AS o 
    ON c.customer_id = o.customer_id; 
   

/* Ex. 14. 
   Write a SQL statement to make a list for the salesmen who either work for one or more customers or yet to join any of the customer. 
   The customer may have placed, either one or more orders on or above order amount 2000 
   and must have a grade, or he may not have placed any order to the associated supplier.  
   Sample table: customer
   Sample table: salesman
   Sample table: orders
*/ 

SELECT s.name AS "Salesman Name",
       c.cust_name AS "Customer Name",
       o.purch_amt AS "Purchase Amount",
       c.grade AS "Customer Grade"
  FROM salesman AS s
  LEFT JOIN customer AS c 
    ON s.salesman_id = c.salesman_id 
  LEFT JOIN orders AS o 
    ON c.customer_id = o.customer_id
 WHERE o.purch_amt >= 2000
   AND c.grade IS NOT NULL;

/* Ex. 15. 
   Write a SQL statement to make a report with customer name, city, order no. order date, purchase amount for those customers 
   from the existing list who placed one or more orders or which order(s) have been placed by the customer who is not on the list.  
   Sample table: customer
   Sample table: orders
*/ 
   
SELECT c.cust_name AS "Customer Name",
	   c.city AS "Customer City",
	   o.ord_no AS "Order Number",
	   o.ord_date AS "Order Date",
	   o.purch_amt AS "Purchase amount"
  FROM customer AS c
  FULL OUTER JOIN orders AS o
    ON c.customer_id = o.customer_id;        
  
  
/* Ex. 16. 
   Write a SQL statement to make a report with customer name, city, order no. order date, purchase amount for only those customers 
   on the list who must have a grade and placed one or more orders or which order(s) have been placed 
   by the customer who is neither in the list nor have a grade.  
   Sample table: customer
   Sample table: orders
*/ 

SELECT c.cust_name AS "Customer Name",
	   c.city AS "Customer City",
	   o.ord_no AS "Order Number",
	   o.ord_date AS "Date",
	   o.purch_amt AS "Purchase Amount"
  FROM customer AS c
  FULL OUTER JOIN orders AS o 
    ON c.customer_id = o.customer_id
 WHERE c.grade IS NOT NULL;

/* Ex. 17. 
   Write a SQL query to combine each row of salesman table with each row of customer table.  
   Sample table: salesman
   Sample table: customer
*/ 

SELECT *
  FROM salesman AS s
 CROSS JOIN customer AS c; 

/* Ex. 18. 
   Write a SQL statement to make a cartesian product between salesman and customer i.e. each salesman will appear for all customer 
   and vice versa for that salesman who belongs to a city.  
   Sample table: salesman
   Sample table: customer
*/ 

SELECT *
  FROM salesman as s
 CROSS JOIN customer AS c
 WHERE s.city IS NOT NULL;

/* Ex. 19. 
   Write a SQL statement to make a cartesian product between salesman and customer i.e. each salesman will appear for all customer 
   and vice versa for those salesmen who belongs to a city and the customers who must have a grade.  
   Sample table: salesman
   Sample table: customer
*/ 

SELECT * 
  FROM salesman AS s
 CROSS JOIN customer AS c 
 WHERE s.city IS NOT NULL 
   AND c.grade IS NOT NULL;

/* Ex. 20.
   Write a SQL statement to make a cartesian product between salesman and customer i.e. each salesman will appear for all customer 
   and vice versa for those salesmen who must belong a city which is not the same as his customer and the customers should have an own grade.  
   Sample table: salesman
   Sample table: customer  
*/ 
  
SELECT *
  FROM salesman AS s
 CROSS JOIN customer AS c 
 WHERE s.city != c.city 
   AND c.grade IS NOT NULL
   AND s.city IS NOT NULL
   AND c.city IS NOT NULL;
  
/* Ex. 21. 
   From the following tables write a SQL query to select all rows from both participating tables as long as there 
   is a match between pro_com and com_id. 
   Sample table: company_mast
   Sample table: item_mast
*/ 

SELECT *
  FROM company_mast AS c
  JOIN item_mast AS i
    ON c.com_id = i.pro_com;

/* Ex. 22. 
   Write a SQL query to display the item name, price, and company name of all the products.  
   Sample table: company_mast
   Sample table: item_mast
*/ 

SELECT i.pro_name AS "Item Name",
       i.pro_price AS "Item Price",
       c.com_name AS "Company Name"
FROM item_mast AS i
JOIN company_mast AS c 
ON i.pro_com = c.com_id;

/* Ex. 23. 
   From the following tables write a SQL query to calculate the average price of items of each company. Return average value and company name.  
   Sample table: company_mast
   Sample table: item_mast
*/ 

SELECT c.com_name AS "Company Name",
       AVG(i.pro_price) AS "Average price"
  FROM company_mast AS c
  JOIN item_mast AS i 
    ON c.com_id = i.pro_com 
 GROUP BY c.com_name; 

       
/* Ex. 24. 
   From the following tables write a SQL query to calculate and find the average price of items of each company higher than or equal to Rs. 350. 
   Return average value and company name.  
   Sample table: company_mast
   Sample table: item_mast
*/ 

SELECT c.com_name AS "Company Name",
       AVG(i.pro_price) AS "Average Price"
  FROM company_mast AS c
  JOIN item_mast AS i 
    ON c.com_id = i.pro_com 
 GROUP BY c.com_name
HAVING AVG(i.pro_price) >= 350;

/* Ex. 25. 
   From the following tables write a SQL query to find the most expensive product of each company. Return pro_name, pro_price and com_name. 
   Sample table: company_mast
   Sample table: item_mast
*/                                           
  
-- 1 WITH
WITH cte AS (SELECT pro_com, 
  		            MAX(pro_price) AS max_pro_price
	   		   FROM item_mast AS i 
      		  GROUP BY pro_com)
SELECT i.pro_name AS "Product Name",
       i.pro_price AS "Product Price",
       c.com_name AS "Company Name"
  FROM item_mast AS i
  JOIN company_mast AS c 
    ON i.pro_com = c.com_id
  JOIN cte AS cte
    ON i.pro_com = cte.pro_com
 WHERE i.pro_price = cte.max_pro_price;
   		      

-- 2 subquiery/derived table
SELECT i.pro_name AS "Product Name",
       i.pro_price AS "Product Price",
       c.com_name AS "Company Name"
  FROM item_mast AS i
  JOIN company_mast AS c 
    ON i.pro_com = c.com_id 
  JOIN (SELECT pro_com, 
  		       MAX(pro_price) AS max_pro_price
	      FROM item_mast AS i 
         GROUP BY pro_com) AS q 
    ON i.pro_com = q.pro_com
 WHERE i.pro_price = q.max_pro_price;

-- 3 subquiery/derived table
SELECT i.pro_name AS "Product Name",
       i.pro_price AS "Product Price",
       c.com_name AS "Company Name"
  FROM item_mast AS i
  JOIN company_mast AS c 
    ON i.pro_com = c.com_id
   AND i.pro_price = (SELECT MAX(i.pro_price) 
                        FROM item_mast AS i
                       WHERE i.pro_com = c.com_id);    


-- 4 two subquiries 
SELECT q1.pro_name AS "Product Name",
       q1.pro_price AS "Product Price",
       c.com_name AS "Company Name"
  FROM company_mast AS c 
  JOIN (SELECT i.pro_name, 
               i.pro_price, 
               i.pro_com
  		  FROM item_mast AS i
  		  JOIN (SELECT pro_com, 
  		               MAX(pro_price) AS max_pro_price
	              FROM item_mast AS i 
                 GROUP BY pro_com) AS q
            ON i.pro_com = q.pro_com
         WHERE i.pro_price = q.max_pro_price) AS q1
    ON c.com_id = q1.pro_com;                        

/* Ex. 26.
   From the following tables write a SQL query to display all the data of employees including their department.  
   Sample table: emp_department
   Sample table: emp_details    
*/ 

SELECT *
  FROM emp_department AS dep 
  JOIN emp_details AS emp
    ON dep.dpt_code = emp.emp_dept;
   
/* Ex. 27. 
   From the following tables write a SQL to display the first name and last name of each employee, along with the name 
   and sanction amount for their department.  
   Sample table: emp_department
   Sample table: emp_details
*/ 

SELECT emp.emp_fname AS "First Name",
	   emp.emp_lname AS "Last Name",
	   dep.dpt_name AS "Department Name",
	   dep.dpt_allotment AS "Allotment"
  FROM emp_department AS dep
  JOIN emp_details AS emp 
    ON dep.dpt_code = emp.emp_dept;

/* Ex. 28. 
   From the following tables write a SQL query to find the departments with a budget more than Rs. 50000 and display 
   the first name and last name of employees.  
   Sample table: emp_department
   Sample table: emp_details
*/ 
   

SELECT emp.emp_fname AS "First Name",
	   emp.emp_lname AS "Last Name"
  FROM emp_department AS dep
  JOIN emp_details AS emp
    ON dep.dpt_code = emp.emp_dept 
 WHERE dep.dpt_allotment > 50000;
   
/* Ex. 29. 
   From the following tables write a SQL query to find the names of departments where more than two employees are working. Return dpt_name.  
   Sample table: emp_department
   Sample table: emp_details
*/ 

SELECT dep.dpt_name
  FROM emp_department AS dep
  JOIN emp_details AS emp
    ON dep.dpt_code = emp.emp_dept
 GROUP BY dep.dpt_name
HAVING COUNT(*) > 2;    


/* PART 8. SUBQUERIES. */  

/* Ex. 1. 
   From the following tables, write a SQL query to find all the orders issued by the salesman 'Paul Adam'. 
   Return ord_no, purch_amt, ord_date, customer_id and salesman_id.  
   Sample table: Salesman
   Sample table: Orders
*/

-- Subquery
SELECT ord_no AS "Order Number",
	   purch_amt AS "Purchase Amount",
	   ord_date AS "Order Date",
	   customer_id AS "Customer ID",
	   salesman_id AS "Salesman ID"
  FROM orders 
 WHERE salesman_id = (SELECT salesman_id   
 						FROM salesman
 					   WHERE name = 'Paul Adam');

-- WITH+WHERE
WITH cte AS (SELECT salesman_id AS sal_id   
 			   FROM salesman
 		      WHERE name = 'Paul Adam')
SELECT ord_no AS "Order Number",
	   purch_amt AS "Purchase Amount",
	   ord_date AS "Order Date",
	   customer_id AS "Customer ID",
	   salesman_id AS "Salesman ID"
  FROM orders, cte
 WHERE salesman_id = sal_id;

-- JOIN
SELECT o.ord_no AS "Order Number",
	   o.purch_amt AS "Purchase Amount",
	   o.ord_date AS "Order Date",
	   o.customer_id AS "Customer ID",
	   s.salesman_id AS "Salesman ID"
  FROM orders AS o
  JOIN salesman AS s 
    ON o.salesman_id = s.salesman_id 
 WHERE s.name = 'Paul Adam';    


/* Ex. 2. 
   From the following tables, write a SQL query to find all the orders, which are generated by those salespeople, who live in the city of London.
   Return ord_no, purch_amt, ord_date, customer_id, salesman_id.  
   Sample table: Salesman
   Sample table: Orders
*/

-- Subquery 
SELECT ord_no AS "Order Number",
	   purch_amt AS "Purchase Amount",
	   ord_date AS "Order Date",
	   customer_id AS "Customer ID",
	   salesman_id AS "Salesman ID"
  FROM orders	
 WHERE salesman_id = (SELECT salesman_id 
						FROM salesman 
					   WHERE city = 'London');  
					  
-- Join
SELECT o.ord_no AS "Order Number",
	   o.purch_amt AS "Purchase Amount",
	   o.ord_date AS "Order Date",
	   o.customer_id AS "Customer ID",
	   s.salesman_id AS "Salesman ID"
  FROM orders AS o
  JOIN salesman AS s
    ON o.salesman_id = s.salesman_id 
 WHERE s.city = 'London';    			  

/* Ex. 3. 
   From the following tables, write a SQL query to find the orders generated by the salespeople who may work for customers whose id is 3007. 
   Return ord_no, purch_amt, ord_date, customer_id, salesman_id.  
   Sample table: Salesman
   Sample table: Orders
*/

SELECT ord_no AS "Order Number",
	   purch_amt AS "Purchase Amount",
	   ord_date AS "Order Date",
	   customer_id AS "Customer ID",
	   salesman_id AS "Salesman ID"
  FROM orders 
 WHERE customer_id = 3007;  

/* Ex. 4. 
   From the following tables, write a SQL query to find the order values greater than the average order value of 10th October 2012. 
   Return ord_no, purch_amt, ord_date, customer_id, salesman_id.  
   Sample table: Salesman
   Sample table: Orders
*/

-- Subquery 
SELECT ord_no AS "Order Number",
	   purch_amt AS "Purchase Amount",
	   ord_date AS "Order Date",
	   customer_id AS "Customer ID",
	   salesman_id AS "Salesman ID"
  FROM orders
 WHERE purch_amt > (SELECT AVG(purch_amt) 
					FROM orders 
				   WHERE ord_date = '2012-10-10');  
  
/* Ex. 5. 
   From the following tables, write a SQL query to find all the orders generated in New York city. 
   Return ord_no, purch_amt, ord_date, customer_id and salesman_id.  
   Sample table: Salesman
   Sample table: Orders
*/

-- Subquery
SELECT ord_no AS "Order Number",
	   purch_amt AS "Purchase Amount",
	   ord_date AS "Order Date",
	   customer_id AS "Customer ID",
	   salesman_id AS "Salesman ID"
  FROM orders 
 WHERE salesman_id = (SELECT salesman_id 
   					    FROM salesman 
   					   WHERE city = 'New York'); 
				  				  
-- JOIN
SELECT o.ord_no AS "Order Number",
	   o.purch_amt AS "Purchase Amount",
	   o.ord_date AS "Order Date",
	   o.customer_id AS "Customer ID",
	   s.salesman_id AS "Salesman ID"
  FROM orders AS o
  JOIN salesman AS s
    ON o.salesman_id = s.salesman_id
 WHERE s.city = 'New York';   

-- WITH
WITH cte AS (SELECT salesman_id AS sal_id 
			   FROM salesman 
			  WHERE city = 'New York')
SELECT ord_no AS "Order Number",
	   purch_amt AS "Purchase Amount",
	   ord_date AS "Order Date",
	   customer_id AS "Customer ID",
	   salesman_id AS "Salesman ID"
  FROM orders, cte 
 WHERE salesman_id = sal_id; 
 
/* Ex. 6. 
   From the following tables, write a SQL query to find the commission of the salespeople work in Paris City. 
   Return commission.  
   Sample table: Salesman
   Sample table : Customer
*/

SELECT commission AS "Commission"
  FROM salesman 
 WHERE city = 'Paris';

/* Ex. 7. 
   Write a query to display all the customers whose id is 2001 bellow the salesman ID of Mc Lyon.  
   Sample table: Salesman
   Sample table : Customer
*/

-- 1 
SELECT cust_name AS "Customer Name"
  FROM customer 
 WHERE customer_id = (SELECT salesman_id 
						FROM salesman 
					   WHERE name = 'Mc Lyon') - 2001;
					  
-- 2 
SELECT cust_name AS "Customer Name"
  FROM customer 
 WHERE customer_id = (SELECT salesman_id - 2001
						FROM salesman 
					   WHERE name = 'Mc Lyon'); 					  

/* Ex. 8. 
   From the following tables, write a SQL query to count number of customers with grades above the average grades of New York City. 
   Return grade and count.   
   Sample table: Customer
*/

SELECT grade, COUNT(*) AS "Num of customers"
  FROM customer
 WHERE grade > (SELECT AVG(grade) 
 				  FROM customer 
 				 WHERE city = 'New York')
 GROUP BY grade;  

/* Ex. 9. 
   From the following tables, write a SQL query to find those salespeople who earned the maximum commission. 
   Return ord_no, purch_amt, ord_date, and salesman_id.  
   Sample table: Customer
   Sample table: Orders
   Sample table: salesman
*/

-- Subquery 
SELECT ord_no AS "Order Number",
	   purch_amt AS "Purchase Amount",
	   ord_date AS "Order Date",
	   salesman_id AS "Salesman ID"
  FROM orders
 WHERE salesman_id IN (SELECT salesman_id 
					  	 FROM salesman 
					    WHERE commission = (SELECT MAX(commission) 
					  						  FROM salesman)); 

-- JOIN + Subquery 

SELECT o.ord_no AS "Order Number",
	   o.purch_amt AS "Purchase Amount",
	   o.ord_date AS "Order Date",
	   o.salesman_id AS "Salesman ID"
  FROM orders AS o
  JOIN salesman AS s
    ON o.salesman_id = s.salesman_id 
 WHERE s.commission IN (SELECT MAX(commission) -- OR '='
						  FROM salesman);   
						 
-- CTE
  WITH cte AS (SELECT MAX(commission) AS max_com  
			   FROM salesman)						 
SELECT o.ord_no AS "Order Number",
	   o.purch_amt AS "Purchase Amount",
	   o.ord_date AS "Order Date",
	   o.salesman_id AS "Salesman ID"
  FROM orders AS o
  JOIN salesman AS s
    ON o.salesman_id = s.salesman_id 
  JOIN cte
    ON s.commission = cte.max_com;   
						 						 
					  						
/* Ex. 10. 
   From the following tables, write a SQL query to find the customers whose orders issued on 17th August, 2012. 
   Return ord_no, purch_amt, ord_date, customer_id, salesman_id and cust_name.  
   Sample table: Orders
   Sample table: Customer
*/

SELECT o.ord_no AS "Order Number",
	   o.purch_amt AS "Purchase Amount",
	   o.ord_date AS "Order Date",
	   o.customer_id AS "Customer ID",
	   o.salesman_id AS "Salesman ID",
	   c.cust_name AS "Customer Name"
  FROM orders AS o 
  JOIN customer AS c  
    ON o.customer_id = c.customer_id 
 WHERE o.ord_date = '2012-08-17';   
	   
/* Ex. 11. 
   From the following tables, write a SQL query to find the salespeople who had more than one customer. 
   Return salesman_id and name.  
   Sample table: Customer
   Sample table: Salesman
*/

SELECT salesman_id AS "Salesman ID",
	   name AS "Salesman Name"
  FROM salesman 
 WHERE salesman_id IN (SELECT salesman_id 
  						 FROM customer 
  						GROUP BY salesman_id 
  					   HAVING COUNT(*) > 1);  
  
/* Ex. 12. 
   From the following tables, write a SQL query to find those orders, which are higher than average amount of the orders. 
   Return ord_no, purch_amt, ord_date, customer_id and salesman_id.  
   Sample table: Orders
   Sample table: Customer
*/

SELECT ord_no AS "Order Number",
	   purch_amt AS "Purchase Amount",
	   ord_date AS "Order Date",
	   customer_id AS "Customer ID",
	   salesman_id AS "Salesman ID"
  FROM orders 
 WHERE purch_amt > (SELECT AVG(purch_amt) 
					FROM orders);
					  
/* Ex. 13. 
   From the following tables, write a SQL query to find those orders, which are equal or higher than average amount of the orders.
   Return ord_no, purch_amt, ord_date, customer_id and salesman_id.  
   Sample table: Orders
   Sample table: Customer
*/
				
SELECT ord_no AS "Order Number",
	   purch_amt AS "Purchase Amount",
	   ord_date AS "Order Date",
	   customer_id AS "Customer ID",
	   salesman_id AS "Salesman ID"
  FROM orders 
 WHERE purch_amt >= (SELECT AVG(purch_amt) 
					FROM orders);			
			
/* Ex. 14. 
   Write a query to find the sums of the amounts from the orders table, grouped by date, eliminating all those dates 
   where the sum was not at least 1000.00 above the maximum order amount for that date.  
   Sample table: Orders
   Sample table: Customer
*/

SELECT SUM(purch_amt) AS "Sum Purchase Amount",
	   ord_date AS "Order Date"
  FROM orders 
 GROUP BY ord_date
HAVING SUM(purch_amt) > MAX(purch_amt) + 1000;  
				
/* Ex. 15. 
   Write a query to extract all data from the customer table if and only if one or more of the customers in the customer table are located in London. 
   Sample table: Customer
*/

SELECT *
  FROM customer
 WHERE EXISTS (SELECT * 
				 FROM customer 
				WHERE city = 'London');

/* Ex. 16. 
   From the following tables, write a SQL query to find the salespeople who deal multiple customers. 
   Return salesman_id, name, city and commission. 
   Sample table: Customer
   Sample table: Salesman
*/

SELECT salesman_id AS "Salesman ID",
	   name AS "Salesman Name",
	   city AS "Salesman City",
	   commission AS "Commission"
  FROM salesman	 
 WHERE salesman_id IN (SELECT salesman_id 
						 FROM customer 
						GROUP BY salesman_id 
					   HAVING COUNT(*) > 1); 
 					
/* Ex. 17. 
   From the following tables, write a SQL query to find the salespeople who deal a single customer. 
   Return salesman_id, name, city and commission.
   Sample table: Customer
   Sample table: Salesman
*/

SELECT salesman_id AS "Salesman ID",
	   name AS "Salesman Name",
	   city AS "Salesman City",
	   commission AS "Commission"
  FROM salesman	 
 WHERE salesman_id IN (SELECT salesman_id 
						 FROM customer 
						GROUP BY salesman_id 
					   HAVING COUNT(*) = 1); 

/* Ex. 18. 
   From the following tables, write a SQL query to find the salespeople who deal the customers with more than one order. 
   Return salesman_id, name, city and commission.
   Sample table: Salesman
   Sample table: Orders
   Sample table: Customer
*/

-- Subquery				  
SELECT salesman_id AS "Salesman ID",
	   name AS "Salesman Name",
	   city AS "Salesman City",
	   commission AS "Commission"
  FROM salesman
 WHERE salesman_id IN (SELECT salesman_id 
 					     FROM orders 
 					    WHERE customer_id IN (SELECT customer_id 
 					    						FROM orders 
 					    					   GROUP BY customer_id 
 					    					  HAVING COUNT(*) > 1));  

-- JOIN 					    					 
SELECT DISTINCT s.salesman_id AS "Salesman ID",
	   s.name AS "Salesman Name",
	   s.city AS "Salesman City",
	   s.commission AS "Commission"
  FROM salesman AS s
  JOIN orders AS o
    ON s.salesman_id = o.salesman_id 
 WHERE o.customer_id IN (SELECT customer_id 
						 FROM orders 
						GROUP BY customer_id 
					   HAVING COUNT(*) > 1); 
					  
-- CTE
WITH cte AS (SELECT customer_id 
			    FROM orders 
			   GROUP BY customer_id 
			  HAVING COUNT(*) > 1)	
SELECT DISTINCT s.salesman_id AS "Salesman ID",
	   s.name AS "Salesman Name",
	   s.city AS "Salesman City",
	   s.commission AS "Commission"
  FROM salesman AS s
  JOIN orders AS o
    ON s.salesman_id = o.salesman_id
  JOIN cte
    ON o.customer_id = cte.customer_id;
					  					  
/* Ex. 19. 
   From the following tables, write a SQL query to find the salespeople who deals those customers who live in the same city. 
   Return salesman_id, name, city and commission. 
   Sample table: Salesman
   Sample table: customer
*/

-- 1
SELECT salesman_id AS "Salesman ID",
	   name AS "Salesman Name",
	   city AS "Salesman City",
	   commission AS "Commission"	
  FROM salesman AS s
 WHERE city IN (SELECT city FROM customer AS c WHERE s.salesman_id = c.salesman_id); 

-- 2
SELECT DISTINCT s.salesman_id AS "Salesman ID",
	   s.name AS "Salesman Name",
	   s.city AS "Salesman City",
	   s.commission AS "Commission"	
  FROM salesman AS s
  JOIN customer AS c
    ON s.salesman_id = c.salesman_id
 WHERE s.city = c.city; 

/* Ex. 20. 
   From the following tables, write a SQL query to find the salespeople whose place of living (city) matches 
   with any of the city where customers live. 
   Return salesman_id, name, city and commission.
   Sample table: Salesman
   Sample table: customer
*/

SELECT salesman_id AS "Salesman ID",
	   name AS "Salesman Name",
	   city AS "Salesman City",
	   commission AS "Commission"	
  FROM salesman AS s
 WHERE city IN (SELECT city FROM customer); 

/* Ex. 21. 
   From the following tables, write a SQL query to find all those salespeople whose name exist alphabetically after the customer’s name. 
   Return salesman_id, name, city, commission. 
   Sample table: Salesman
   Sample table: Customer
*/

SELECT salesman_id AS "Salesman ID",
	   name AS "Salesman Name",
	   city AS "Salesman City",
	   commission AS "Commission"
  FROM salesman AS s
 WHERE EXISTS (SELECT * 
				 FROM customer AS c 
				WHERE s.name < c.cust_name);

/* Ex. 22. 
   From the following table, write a SQL query to find all those customers who have a greater grade than any customer 
   who belongs to the alphabetically lower than the city of New York. 
   Return customer_id, cust_name, city, grade, salesman_id 
   Sample table: Customer
*/

SELECT customer_id AS "Customer ID",
	   cust_name AS "Customer Name",
	   grade AS "Grade",
	   salesman_id AS "Salesman ID"
  FROM customer
 WHERE grade > ANY (SELECT grade 
   					  FROM customer 
   					 WHERE city < 'New York'); 

/* Ex. 23. 
   From the following table, write a SQL query to find all those orders whose order amount greater than at least one 
   of the orders of September 10th 2012. 
   Return ord_no, purch_amt, ord_date, customer_id and salesman_id. 
   Sample table: Orders
*/

SELECT ord_no AS "Order Number",
	   purch_amt AS "Purchase Amount",
	   ord_date AS "Order Date",
	   customer_id AS "Customer ID",
	   salesman_id AS "Salesman ID"
  FROM orders
 WHERE purch_amt > ANY (SELECT purch_amt 
						  FROM orders 
						 WHERE ord_date = '2012-09-10');  
   					
/* Ex. 24. 
   From the following tables, write a SQL query to find those orders where an order amount less than any order amount 
   of a customer lives in London City. 
   Return ord_no, purch_amt, ord_date, customer_id and salesman_id.  
   Sample table: Orders
   Sample table: Customer
*/

-- 1
SELECT ord_no AS "Order Number",
	   purch_amt AS "Purchase Amount",
	   ord_date AS "Order Date",
	   customer_id AS "Customer ID",
	   salesman_id AS "Salesman ID"
  FROM orders
 WHERE purch_amt < ANY (SELECT purch_amt 
						  FROM orders 
						 WHERE customer_id IN (SELECT customer_id 
												 FROM customer 
												WHERE city = 'London'));  
-- 2
SELECT ord_no AS "Order Number",
	   purch_amt AS "Purchase Amount",
	   ord_date AS "Order Date",
	   customer_id AS "Customer ID",
	   salesman_id AS "Salesman ID"
  FROM orders
 WHERE purch_amt < ANY (SELECT purch_amt 
						  FROM orders AS o
						  JOIN customer AS c
						    ON o.customer_id = c.customer_id  
						 WHERE c.city = 'London');											
											
				
/* Ex. 25. 
   From the following tables, write a SQL query to find those orders where every order amount less than the maximum order 
   amount of a customer lives in London City. 
   Return ord_no, purch_amt, ord_date, customer_id and salesman_id.
   Sample table: Orders
   Sample table: Customer
*/

-- 1						
SELECT ord_no AS "Order Number",
	   purch_amt AS "Purchase Amount",
	   ord_date AS "Order Date",
	   customer_id AS "Customer ID",
	   salesman_id AS "Salesman ID"
  FROM orders
 WHERE purch_amt < (SELECT MAX(purch_amt) 
					  FROM orders 
					 WHERE customer_id IN (SELECT customer_id 
										     FROM customer 
										    WHERE city = 'London')); 

-- 2
SELECT ord_no AS "Order Number",
	   purch_amt AS "Purchase Amount",
	   ord_date AS "Order Date",
	   customer_id AS "Customer ID",
	   salesman_id AS "Salesman ID"
  FROM orders
 WHERE purch_amt < (SELECT MAX(purch_amt) 
				      FROM orders AS o
					  JOIN customer AS c
					    ON o.customer_id = c.customer_id  
					 WHERE c.city = 'London');											
																					   
/* Ex. 26. 
   From the following tables, write a SQL query to find those customers whose grade are higher than customers living in New York City. 
   Return customer_id, cust_name, city, grade and salesman_id. 
   Sample table: Customer
*/

-- ALL					
SELECT customer_id AS "Customer ID",
	   cust_name AS "Customer Name",
	   city AS "Customer City",
	   grade AS "Grade",
	   salesman_id AS "Salesman ID"
  FROM customer
 WHERE grade > ALL (SELECT grade 
					  FROM customer 
					 WHERE city = 'New York');
					
-- MAX 
SELECT customer_id AS "Customer ID",
	   cust_name AS "Customer Name",
	   city AS "Customer City",
	   grade AS "Grade",
	   salesman_id AS "Salesman ID"
  FROM customer
 WHERE grade > (SELECT MAX(grade) 
				  FROM customer 
				 WHERE city = 'New York');			
				
/* Ex. 27. 
   From the following tables, write a SQL query to calculate the total order amount generated by a salesman. 
   The salesman should belong to the cities where any of the customer living. 
   Return salesman name, city and total order amount. 
   Sample table: Orders
   Sample table: Salesman
   Sample table: Customer
*/				 

-- Subquery
SELECT s.name AS "Salesman Name",
	   s.city AS "Selesman City",
	   SUM(o.purch_amt) AS "Total Purchase Amount"
  FROM salesman AS s	   
  JOIN orders AS o
    ON s.salesman_id = o.salesman_id
 WHERE s.city = ANY (SELECT c.city 
 					   FROM customer AS c 
 					  WHERE c.city = s.city)
 GROUP BY s.name, s.city;  	

/* Ex. 28. 
   From the following tables, write a SQL query to find those customers whose grade doesn't same of those customers live in London City. 
   Return customer_id, cust_name, city, grade and salesman_id.
   Sample table: Customer
*/

-- ALL
SELECT customer_id AS "Customer ID",
	   cust_name AS "Customer Name",
	   city AS "Customer City",
	   grade AS "Grade",
	   salesman_id AS "Salesman ID"
  FROM customer
 WHERE grade != ALL (SELECT grade 
					   FROM customer 
					  WHERE city = 'London' 
					    AND grade IS NOT NULL);  

-- NOT IN					   
SELECT customer_id AS "Customer ID",
	   cust_name AS "Customer Name",
	   city AS "Customer City",
	   grade AS "Grade",
	   salesman_id AS "Salesman ID"
  FROM customer
 WHERE grade NOT IN (SELECT grade 
					   FROM customer 
					  WHERE city = 'London' 
					    AND grade IS NOT NULL);  
					   
/* Ex. 29. 
   From the following tables, write a SQL query to find those customers whose grade are not same of those customers living in Paris. 
   Return customer_id, cust_name, city, grade and salesman_id. 
   Sample table: Customer
*/
					   
-- ALL
SELECT customer_id AS "Customer ID",
	   cust_name AS "Customer Name",
	   city AS "Customer City",
	   grade AS "Grade",
	   salesman_id AS "Salesman ID"
  FROM customer
 WHERE grade != ALL (SELECT grade 
					   FROM customer 
					  WHERE city = 'Paris' 
					    AND grade IS NOT NULL);     
  
-- NOT IN
SELECT customer_id AS "Customer ID",
	   cust_name AS "Customer Name",
	   city AS "Customer City",
	   grade AS "Grade",
	   salesman_id AS "Salesman ID"
  FROM customer
 WHERE grade NOT IN (SELECT grade 
					   FROM customer 
					  WHERE city = 'Paris' 
					    AND grade IS NOT NULL); 					   
					   
/* Ex. 30. 
   From the following tables, write a SQL query to find all those customers who have different grade than any customer lives in Dallas City. 
   Return customer_id, cust_name,city, grade and salesman_id. 
   Sample table: Customer
*/

SELECT customer_id AS "Customer ID",
	   cust_name AS "Customer Name",
	   city AS "Customer City",
	   grade AS "Grade",
	   salesman_id AS "Salesman ID"
  FROM customer
 WHERE grade != ANY (SELECT grade 
					   FROM customer 
					  WHERE city = 'Dallas');  
					 					   					   
/* Ex. 31. 
   From the following tables, write a SQL query to find the average price of each manufacturer's product along with their name. 
   Return Average Price and Company.
   Sample table: company_mast
   Sample table: item_mast
*/

					 
-- Subquery
SELECT AVG(pro_price) AS "Avg. Price",
  	   (SELECT com_name FROM company_mast WHERE com_id = pro_com) AS "Company Name"
  FROM item_mast 
 GROUP BY pro_com;					 

-- JOIN					 
SELECT AVG(im.pro_price) AS "Avg. Price",
  	   cm.com_name AS "Company Name"
  FROM item_mast AS im
  JOIN company_mast AS cm
    ON im.pro_com = cm.com_id
 GROUP BY cm.com_name;    
					 
/* Ex. 32. 
   From the following tables, write a SQL query to calculate the average price of the products and find price which are more than or equal to 350. 
   Return Average Price and Company.
   Sample table: company_mast
   Sample table: item_mast
*/

SELECT AVG(im.pro_price) AS "Avg. Price",
   	   cm.com_name AS "Company Name"
  FROM item_mast AS im
  JOIN company_mast AS cm
    ON im.pro_com = cm.com_id
 GROUP BY cm.com_name
HAVING AVG(pro_price) >= 350; 

/* Ex. 33. 
   From the following tables, write a SQL query to find the most expensive product of each company. 
   Return Product Name, Price and Company.
   Sample table: company_mast
   Sample table: item_mast
*/

SELECT im.pro_name AS "Product Name",
	   im.pro_price AS "Price",
       cm.com_name AS "Company Name"
  FROM item_mast AS im
  JOIN (SELECT MAX(pro_price) as max_pro_price, 
  			   pro_com 
  		  FROM item_mast 
  		 GROUP BY pro_com) AS mp
    ON im.pro_com = mp.pro_com 
   AND im.pro_price = mp.max_pro_price
  JOIN company_mast AS cm
    ON im.pro_com = cm.com_id;
       
/* Ex. 34. 
   From the following tables, write a SQL query to find those employees whose last name is 'Gabriel' or 'Dosio'. 
   Return emp_idno, emp_fname, emp_lname and emp_dept.
   Sample table: emp_details
*/
-- 1
SELECT emp_idno AS "ID No",
	   emp_fname AS "First Name",
	   emp_lname AS "Last Name",
	   emp_dept AS "Department Name"
  FROM emp_details	
 WHERE emp_lname = 'Gabriel' 
    OR emp_lname = 'Dosio'; 

-- 2  
SELECT emp_idno AS "ID No",
	   emp_fname AS "First Name",
	   emp_lname AS "Last Name",
	   emp_dept AS "Department Name"
  FROM emp_details	
 WHERE emp_lname IN ('Gabriel', 'Dosio'); 
   
/* Ex. 35. 
   From the following tables, write a SQL query to find the employees who work in department 89 or 63. 
   Return emp_idno, emp_fname, emp_lname and emp_dept.
   Sample table: emp_department
   Sample table: emp_details
*/

SELECT emp_idno AS "ID Number",
       emp_fname AS "First Name",
       emp_lname AS "Last Name",
       emp_dept AS "Department Name"
  FROM emp_details 
 WHERE emp_dept IN (89, 63);

/* Ex. 36. 
   From the following tables, write a SQL query to find those employees who work for the department 
   where the department allotment amount is more than Rs. 50000. 
   Return emp_fname and emp_lname.
   Sample table: emp_department
   Sample table: emp_details
*/

SELECT emp_fname AS "First Name",
	   emp_lname AS "Last Name"
  FROM emp_details 
 WHERE emp_dept IN (SELECT dpt_code 
					  FROM emp_department 
					 WHERE dpt_allotment > 50000);  
					
/* Ex. 37. 
   From the following tables, write a SQL query to find the departments where the sanction amount is higher 
   than the average sanction amount of all the departments. 
   Return dpt_code, dpt_name and dpt_allotment.
   Sample table: emp_department
*/

SELECT dpt_code AS "Depatment Code",
       dpt_name AS "Department Name",
       dpt_allotment AS "Department Allotment"
  FROM emp_department 
 WHERE dpt_allotment > (SELECT AVG(dpt_allotment) 
						  FROM emp_department); 
								
/* Ex. 38. 
   From the following tables, write a SQL query to find the departments where more than two employees work. 
   Return dpt_name.
   Sample table: emp_department
   Sample table: emp_details
*/

SELECT dpt_name AS "Department Name"
  FROM emp_department 
 WHERE dpt_code IN (SELECT emp_dept 
					  FROM emp_details 
					 GROUP BY emp_dept 
					HAVING COUNT(*) > 2);
						 
/* Ex. 39. 
   From the following tables, write a SQL query to find the departments where the sanction amount is second lowest. 
   Return emp_fname and emp_lname.
   Sample table: emp_department
   Sample table: emp_details
*/

SELECT emp_fname AS "First Name",
	   emp_lname AS "Last Name"
  FROM emp_details 
 WHERE emp_dept IN (SELECT dpt_code 
					  FROM emp_department 
					 WHERE dpt_allotment = (SELECT MIN(dpt_allotment) 
											  FROM emp_department 
											 WHERE dpt_allotment > (SELECT MIN(dpt_allotment) 
																	  FROM emp_department))); 

																	 
/* PART 9. FILTERING and SORTING on HR Database. */  

/* Ex. 1. 
   From the following table, write a SQL query to find those employees whose salary is less than 6000. 
   Return full name (first and last name), and salary.  
   Sample table: employees
*/

SELECT CONCAT(first_name, ' ', last_name) AS "Full Name",
       salary AS "Salary"
  FROM employees
 WHERE salary < 6000;
																	 
/* Ex. 2. 
   From the following table, write a SQL query to find those employees whose salary is higher than 8000. 
   Return first name, last name and department number and salary.  
   Sample table: employees
*/

SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   department_id AS "Department ID",
	   salary AS "Salary"
  FROM employees
 WHERE salary > 8000;

/* Ex. 3. 
   From the following table, write a SQL query to find those employees whose last name is "McEwen". 
   Return first name, last name and department ID.  
   Sample table: employees
*/
	
SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   department_id AS "Department ID"
  FROM employees
 WHERE last_name = 'McEwen';  

/* Ex. 4. 
   From the following table, write a SQL query to find those employees who have no department number. 
   Return employee_id, first_name, last_name, email,phone_number,hire_date, job_id, salary,commission_pct,manager_id and department_id.  
   Sample table: employees
*/

SELECT *
  FROM employees
 WHERE department_id IS NULL;
  
/* Ex. 5. 
   From the following table, write a SQL query to find the details of 'Marketing' department. 
   Return all fields.  
   Sample table: departments
*/

SELECT *
  FROM departments
 WHERE department_name = 'Marketing';  

/* Ex. 6. 
   From the following table, write a SQL query to find those employees whose first name does not contain the letter ‘M’. 
   Sort the result-set in ascending order by department ID. Return full name (first and last name together), hire_date, salary and department_id.  
   Sample table: employees
*/

-- LIKE
SELECT CONCAT(first_name, ' ', last_name) AS "Full Name",
	   hire_date AS "Hire Date",
	   salary AS "Salary",
	   department_id AS "Department ID"
  FROM employees
 WHERE first_name NOT LIKE '%M%' 
 ORDER BY department_id; 

-- SIMILAR TO
SELECT CONCAT(first_name, ' ', last_name) AS "Full Name",
	   hire_date AS "Hire Date",
	   salary AS "Salary",
	   department_id AS "Department ID"
  FROM employees
 WHERE first_name NOT SIMILAR TO '%M%'
 ORDER BY department_id; 

-- RegEx
SELECT CONCAT(first_name, ' ', last_name) AS "Full Name",
	   hire_date AS "Hire Date",
	   salary AS "Salary",
	   department_id AS "Department ID"
  FROM employees
 WHERE first_name !~ '[M]'
 ORDER BY department_id; 
 
  /* Ex. 7. 
   From the following table, write a SQL query to find those employees who falls in the following criteria : 
   1. whose salary is in the range of 8000, 12000 (Begin and end values are included.) and get some commission. 
   2. : those employees who joined before ‘2003-06-05’ and not included in the department number 40, 120 and 70. 
   Return all fields. 
   Sample table: employees
*/

SELECT *
  FROM employees
 WHERE (salary BETWEEN 8000 AND 12000
   AND commission_pct > 0)
    OR (hire_date < '2003-06-05'
   AND department_id NOT IN (40, 120, 70));  

/* Ex. 8. 
   From the following table, write a SQL query to find those employees who do not earn any commission.
   Return full name (first and last name), and salary.  
   Sample table: employees
*/

SELECT CONCAT(first_name, ' ', last_name) AS "Full Name",
	   salary AS "Salary",
	   commission_pct
  FROM employees
 WHERE commission_pct = 0.0;
     
/* Ex. 9. 
   From the following table, write a SQL query to find those employees whose salary is in the range 9000,17000 (Begin and end values are included). 
   Return full name, contact details and salary.  
   Sample table: employees
*/

SELECT CONCAT(first_name, ' ', last_name) AS "Full Name",
	   email AS "Email",
	   phone_number AS "Phone Number",
	   salary AS "Salary"
  FROM employees
 WHERE salary BETWEEN 9000 AND 17000;  
	    
/* Ex. 10. 
   From the following table, write a SQL query to find those employees whose first name ends with the letter ‘m’. 
   Return the first and last name, and salary.  
   Sample table: employees
*/	

-- LIKE
SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   salary AS "Salary"
  FROM employees
 WHERE first_name LIKE '%m';
  
-- SIMILAR TO
SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   salary AS "Salary"
  FROM employees
 WHERE first_name SIMILAR TO '%m';  

-- RegEx
SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   salary AS "Salary"
  FROM employees
 WHERE first_name ~ 'm$';
  
/* Ex. 11. 
   From the following table, write a SQL query to find those employees whose salary is not in the range 7000 and 15000 (Begin and end values are included). 
   Sort the result-set in ascending order by the full name (first and last). Return full name and salary.  
   Sample table: employees
*/

SELECT CONCAT(first_name, ' ', last_name) AS "Full Name",
	   salary AS "Salary"
  FROM employees 
 WHERE salary NOT BETWEEN 7000 AND 15000
 ORDER BY "Full Name";  
  
/* Ex. 12. 
   From the following table, write a SQL query to find those employees who were hired during November 5th, 2007 and July 5th, 2009. 
   Return full name (first and last), job id and hire date. 
   Sample table: employees
*/

SELECT CONCAT(first_name, ' ', last_name) AS "Full Name",
	   job_id AS "Job ID",
	   hire_date AS "Hire Date"
  FROM employees
 WHERE hire_date BETWEEN '2007-11-05' AND '2009-07-05';  
  
/* Ex. 13. 
   From the following table, write a SQL query to find those employees who works either in department 70 or 90. 
   Return full name (first and last name), department id. 
   Sample table: employees
*/

SELECT CONCAT(first_name, ' ', last_name) AS "Full Name",
	   department_id AS "Department ID"
  FROM employees 
 WHERE department_id IN (70, 90); 

/* Ex. 14. 
   From the following table, write a SQL query to find those employees who work under a manager. 
   Return full name (first and last name), salary, and manager ID.  
   Sample table: employees
*/

SELECT CONCAT(first_name, ' ', last_name) AS "Full Name",
	   salary AS "Salary",
	   manager_id AS "Manager ID"
  FROM employees
 WHERE manager_id != 0;

/* Ex. 15. 
   From the following table, write a SQL query to find those employees who were hired before June 21st, 2002. 
   Return all fields.  
   Sample table: employees
*/

SELECT *
  FROM employees
 WHERE hire_date < '2002-06-21';

/* Ex. 16. 
   From the following table, write a SQL query to find those employees whose managers hold the ID 120 or 103 or 145. 
   Return first name, last name, email, salary and manager ID.  
   Sample table: employees
*/

SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   email AS "Email",
	   salary AS "Salary",
	   manager_ID AS "Manager ID"
  FROM employees
 WHERE manager_id IN (120, 103, 145);  

/* Ex. 17. 
   From the following table, write a SQL query to find those employees whose first name contains the letters D, S, or N. 
   Sort the result-set in descending order by salary. Return all fields.  
   Sample table: employees
*/

-- LIKE
SELECT *
  FROM employees
 WHERE first_name LIKE '%D%' 
    OR first_name LIKE '%S%'
    OR first_name LIKE '%N%'
 ORDER BY salary DESC;
   
-- SIMILAR TO 
SELECT *
  FROM employees
 WHERE first_name SIMILAR TO '%(D|S|N)%'
 ORDER BY salary DESC;
 
-- REGEX
SELECT *
  FROM employees
 WHERE first_name ~ '[DSN]'   
 ORDER BY salary DESC;

/* Ex. 18. 
   From the following table, write a SQL query to find those employees who earn above 11000 or the seventh character in their phone number is 3. 
   Sort the result-set in descending order by first name. 
   Return full name (first name and last name), hire date, commission percentage, email, and telephone separated by '-', and salary.  
   Sample table: employees
*/

-- LIKE
SELECT CONCAT(first_name, ' ', last_name) AS "Full Name",
	   hire_date AS "Hire Date",
	   commission_pct AS "Commission, %",
	   email AS "Email",
	   REPLACE(phone_number, '.', '-') AS "Phone Number",
	   salary AS "Salary"
  FROM employees
 WHERE salary > 11000
    OR phone_number LIKE '______3%'
 ORDER BY first_name DESC;  

-- SIMILAR TO
SELECT CONCAT(first_name, ' ', last_name) AS "Full Name",
	   hire_date AS "Hire Date",
	   commission_pct AS "Commission, %",
	   email AS "Email",
	   REPLACE(phone_number, '.', '-') AS "Phone Number",
	   salary AS "Salary"
  FROM employees
 WHERE salary > 11000
    OR phone_number SIMILAR TO '_{6}3%'
 ORDER BY first_name DESC;  

-- REGEX
SELECT CONCAT(first_name, ' ', last_name) AS "Full Name",
	   hire_date AS "Hire Date",
	   commission_pct AS "Commission, %",
	   email AS "Email",
	   REPLACE(phone_number, '.', '-') AS "Phone Number",
	   salary AS "Salary"
  FROM employees
 WHERE salary > 11000
    OR phone_number ~ '^.{6}3'
 ORDER BY first_name DESC;  

/* Ex. 19. 
   From the following table, write a SQL query to find those employees whose first name contains a character ‘s’ in 3rd position. 
   Return first name, last name and department id. 
   Sample table : employees
*/

-- LIKE
SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   department_id AS "Department ID"
  FROM employees
 WHERE first_name LIKE '__s%';  

-- SIMILAR TO
SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   department_id AS "Department ID"
  FROM employees
 WHERE first_name SIMILAR TO '_{2}s%';  

-- REGEX
SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   department_id AS "Department ID"
  FROM employees
 WHERE first_name ~ '^.{2}s';  
  
/* Ex. 20. 
   From the following table, write a SQL query to find those employees who are working in the departments, 
   which are not included in the department number 50 or 30 or 80. 
   Return employee_id, first_name, job_id, department_id.  
   Sample table : employees
*/	

SELECT employee_id AS "Employee ID",
	   first_name AS "First Name",
	   job_id AS "Job ID",
	   department_id AS "Department ID"
  FROM employees
 WHERE department_id NOT IN (50, 30, 80);  
  
/* Ex. 21. 
   From the following table, write a SQL query to find those employees whose department numbers are included in 30 or 40 or 90. 
   Return employee id, first name, job id, department id.  
   Sample table : employees
*/

SELECT employee_id AS "Employee ID",
	   first_name AS "First Name",
	   job_id AS "Job ID",
	   department_id AS "Department ID"
  FROM employees
 WHERE department_id IN (30, 40, 90);  
  
/* Ex. 22. 
   From the following table, write a SQL query to find those employees who worked more than two jobs in the past. 
   Return employee id.  
   Sample table : job_history
*/

SELECT employee_id AS "Employee ID"
  FROM job_history
 GROUP BY employee_id
HAVING COUNT(*) > 2;  
																	 
/* Ex. 23. 
   From the following table, write a SQL query to count the number of employees, sum of all salary, 
   and difference between the highest salary and lowest salary by each job id. 
   Return job_id, count, sum, salary_difference.  
   Sample table : employees
*/

SELECT job_id AS "Job ID",
       COUNT(*) AS "Num of employees",
       SUM(salary) AS "Sum Salary",
       MAX(salary) - MIN(salary) AS "Difference in salary"
  FROM employees
 GROUP BY job_id;  
       
/* Ex. 24. 
   From the following table, write a SQL query to find each job ids where two or more employees worked for more than 300 days. 
   Return job id. 
   Sample table : job_history
*/

SELECT job_id AS "Job ID"
  FROM job_history 
 WHERE end_date - start_date > 300
 GROUP BY job_id
HAVING COUNT(*) >= 2;  

/* Ex. 25. 
   From the following table, write a SQL query to count the number of cities in each country has. 
   Return country ID and number of cities.  
   Sample table : locations
*/

SELECT country_id AS "Country ID",
	   COUNT(city) AS "Num of cities"
  FROM locations
 GROUP BY country_id;

/* Ex. 26. 
   From the following table, write a SQL query to count the number of employees worked under each manager. 
   Return manager ID and number of employees.  
   Sample table : employees
*/

SELECT manager_id AS "Manager ID",
	   COUNT(*) AS "Num of employees"
  FROM employees
 GROUP BY manager_id;  

/* Ex. 27. 
   From the following table, write a SQL query to find all jobs. Sort the result-set in descending order by job title. 
   Return all fields. 
   Sample table : jobs
*/

SELECT *
  FROM jobs
 ORDER BY job_title DESC;

/* Ex. 28. 
   From the following table, write a SQL query to find all those employees who are either Sales Representative or Salesman. 
   Return first name, last name and hire date.  
   Sample table : employees
*/

SELECT first_name AS "First Name",
       last_name AS "Last Name",
       hire_date AS "Hire Date"
  FROM employees
 WHERE job_id IN ('SA_MAN', 'SA_REP');  

/* Ex. 29. 
   From the following table, write a SQL query to calculate average salary of those employees for each department who get a commission percentage. 
   Return department id, average salary.  
   Sample table : employees
*/

SELECT department_id AS "Department ID",
       AVG(salary) AS "Avg. salary"
  FROM employees
 WHERE commission_pct > 0.0
 GROUP BY department_id;

/* Ex. 30. 
   From the following table, write a SQL query to find those departments where a manager can manage four or more employees. 
   Return department_id.  
   Sample table : employees
*/	

SELECT department_id AS "Department ID"
  FROM employees
 GROUP BY department_id
HAVING COUNT(*) >= 4; 
  
/* Ex. 31. 
   From the following table, write a SQL query to find those departments where more than ten employees work, who got a commission percentage. 
   Return department id.  
   Sample table : employees
*/

SELECT department_id AS "Department ID"
  FROM employees
 WHERE commission_pct > 0  
 GROUP BY department_id
HAVING COUNT(*) > 10; 
 
/* Ex. 32. 
   From the following table, write a SQL query to find those employees who have completed their previous jobs. 
   Return employee ID, end_date.  
   Sample table : job_history
*/

SELECT employee_id AS "Employee ID",
	   MAX(end_date) AS "End Date"
  FROM job_history
 GROUP BY employee_id
HAVING COUNT(*) > 1;

/* Ex. 33. 
   From the following table, write a SQL query to find those employees who have no commission percentage 
   and salary within the range 7000, 12000 (Begin and end values are included.) and works in the department number 50. 
   Return all the fields of employees.  
   Sample table : employees
*/

SELECT *
  FROM employees
 WHERE commission_pct = 0
   AND salary BETWEEN 7000 AND 12000
   AND department_id =50;
  
/* Ex. 34. 
   From the following table, write a SQL query to compute the average salary of each job ID. 
   Exclude those records where average salary is higher than 8000. 
   Return job ID, average salary.  
   Sample table : employees
*/

SELECT job_id AS "Job ID",
	   AVG(salary) AS "Average Salary"
  FROM employees
 GROUP BY job_id
HAVING AVG(salary) > 8000;
   
/* Ex. 35. 
   From the following table, write a SQL query to find those job titles where the difference between minimum and maximum salaries is 
   in the range the range 12000, 18000 (Begin and end values are included.). 
   Return job_title, max_salary-min_salary.  
   Sample table : jobs
*/


SELECT job_title AS "Job title",
       max_salary - min_salary AS "Difference in salary"
  FROM jobs
 WHERE max_salary - min_salary BETWEEN 12000 AND 18000;
 
/* Ex. 36. 
   From the following table, write a SQL query to find those employees whose first name or last name starts with the letter ‘D’. 
   Return first name, last name.  
   Sample table : employees
*/

-- LIKE
SELECT first_name AS "First Name",
	   last_name AS "Last Name"
  FROM employees
 WHERE first_name LIKE 'D%'
    OR last_name LIKE 'D%';

-- SIMILAR TO
SELECT first_name AS "First Name",
	   last_name AS "Last Name"
  FROM employees
 WHERE first_name SIMILAR TO 'D%'
    OR last_name SIMILAR TO 'D%';
   
-- REGEX
SELECT first_name AS "First Name",
	   last_name AS "Last Name"
  FROM employees
 WHERE first_name ~ '^D'
    OR last_name ~ '^D';   
   
/* Ex. 37. 
   From the following table, write a SQL query to find details of those jobs where minimum salary exceeds 9000. 
   Return all the fields of jobs.  
   Sample table : jobs
*/

SELECT *
  FROM jobs
 WHERE min_salary > 9000;

/* Ex. 38. 
   From the following table, write a SQL query to find those employees who joined after 7th September 1987. 
   Return all the fields.  
   Sample table : employees
*/

SELECT *
  FROM employees
 WHERE hire_date > '1987-09-07';  
 
/* PART 10. Subqueries on HR Database. */  

/* Ex. 1. 
   From the following table, write a SQL query to find those employees who get higher salary than the employee whose ID is 163. 
   Return first name, last name.  
   Sample table: employees
*/

SELECT first_name AS "First Name",
	   last_name AS "Last Name"
  FROM employees
 WHERE salary > (SELECT salary 
				   FROM employees 
				  WHERE employee_id = 163);  

/* Ex. 2. 
   From the following table, write a SQL query to find those employees whose designation is the same 
   as the employee whose ID is 169. 
   Return first name, last name, department ID and job ID.   
   Sample table: employees
*/

SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   job_id AS "Job ID"
  FROM employees
 WHERE job_id = (SELECT job_id 
				   FROM employees 
				  WHERE employee_id = 169);  
 
/* Ex. 3. 
   From the following table, write a SQL query to find those employees whose salary matches the smallest salary 
   of any of the departments. 
   Return first name, last name and department ID.   
   Sample table: employees
*/

SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   department_id AS "Department ID"
  FROM employees
 WHERE salary IN (SELECT MIN(salary) 
					FROM employees 
				   GROUP BY department_id);  	 
				 
/* Ex. 4. 
   From the following table, write a SQL query to find those employees who earn more than the average salary. 
   Return employee ID, first name, last name.   
   Sample table: employees
*/

SELECT employee_id AS "Employee ID",
	   first_name AS "First Name",
	   last_name AS "Last Name"
  FROM employees
 WHERE salary > (SELECT AVG(salary) 
				   FROM employees);  
				    
/* Ex. 5. 
   From the following table, write a SQL query to find those employees who report that manager whose first name is ‘Payam’. 
   Return first name, last name, employee ID and salary.   
   Sample table: employees
*/

SELECT first_name AS "First Name",
       last_name AS "Last Name",
       employee_id AS "Employee ID",
       salary AS "Salary"
  FROM employees
 WHERE manager_id = (SELECT employee_id 
					   FROM employees 
					  WHERE first_name = 'Payam');  
				  		  
/* Ex. 6. 
   From the following tables, write a SQL query to find all those employees who work in the Finance department. 
   Return department ID, name (first), job ID and department name.   
   Sample table: employees
   Sample table: departments
*/

SELECT e.department_id AS "Department ID",
	   e.first_name AS "First Name",
	   e.job_id AS "Job ID",
	   d.department_name AS "Department Name"
  FROM employees AS e
  JOIN departments AS d
    ON e.department_id = d.department_id 
 WHERE department_name = 'Finance';    
	 
/* Ex. 7. 
   From the following table, write a SQL query to find the employee whose salary is 3000 and reporting person’s ID is 121. 
   Return all fields.   
   Sample table : employees
*/

SELECT *
  FROM employees
 WHERE salary > 3000
   AND manager_id = 121;
 			
/* Ex. 8. 
   From the following table, write a SQL query to find those employees whose ID matches any of the number 134, 159 and 183. 
   Return all the fields.    
   Sample table: employees
*/

SELECT *
  FROM employees
 WHERE employee_id IN (134, 159, 183); 
   
/* Ex. 9. 
   From the following table, write a SQL query to find those employees whose salary is in the range 1000, and 3000 (Begin and end values have included.). 
   Return all the fields.   
   Sample table: employees
*/

SELECT *
  FROM employees
 WHERE salary BETWEEN 1000 AND 3000;  

/* Ex. 10. 
   From the following table and write a SQL query to find those employees whose salary is in the range of smallest salary, and 2500. 
   Return all the fields.   
   Sample table: employees
*/

SELECT *
  FROM employees
 WHERE salary <= 2500;

/* Ex. 11. 
   From the following tables, write a SQL query to find those employees who do not work in those departments where manager ids 
   are in the range 100, 200 (Begin and end values are included.) 
   Return all the fields of the employees.   
   Sample table: employees
   Sample table: departments
*/

SELECT *
  FROM employees
 WHERE manager_id NOT BETWEEN 100 AND 200; 

/* Ex. 12. 
   From the following table, write a SQL query to find those employees who get second-highest salary. 
   Return all the fields of the employees.   
   Sample table: employees
*/ 

-- Subquery
SELECT * 
  FROM employees
 WHERE salary IN (SELECT MAX(salary) 
 				    FROM employees 
 				   WHERE salary < (SELECT MAX(salary) 
 				                     FROM employees));  
-- Subquery + EXCEPT 				                    
SELECT *
  FROM employees
 WHERE salary IN (SELECT MAX(salary) 
 					FROM (SELECT salary 
 				            FROM employees 
 				          EXCEPT 
 				          SELECT MAX(salary) 
 				            FROM employees) AS col);                     
                    
-- OFFSET and LIMIT
SELECT * 
  FROM employees
 ORDER BY salary DESC
OFFSET 1
 LIMIT 2;

-- RANK 
SELECT *
  FROM (SELECT *, 
               RANK () OVER (ORDER BY salary DESC) AS salary_rank
  		  FROM employees) AS employee_rank
 WHERE salary_rank = 2;

/* Ex. 13. 
   From the following tables, write a SQL query to find those employees who work in the same department where ‘Clara’ works. 
   Exclude all those records where first name is ‘Clara’. 
   Return first name, last name and hire date.   
   Sample table: employees
*/

SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   hire_date AS "Hire Date"
  FROM employees
 WHERE department_id = (SELECT department_id 
						  FROM employees 
						 WHERE first_name = 'Clara');

/* Ex. 14. 
   From the following tables, write a SQL query to find those employees who work in a department where the employee’s first name contains a letter 'T'. 
   Return employee ID, first name and last name.  
   Sample table: employees
*/

-- LIKE
SELECT employee_id AS "Employee ID",
	   first_name AS "First Name",
	   last_name AS "Last Name"
  FROM employees
 WHERE department_id IN (SELECT department_id 
					       FROM employees 
					      WHERE first_name LIKE '%T%');

-- SIMILAT TO
SELECT employee_id AS "Employee ID",
	   first_name AS "First Name",
	   last_name AS "Last Name"
  FROM employees
 WHERE department_id IN (SELECT department_id 
					       FROM employees 
					      WHERE first_name SIMILAR TO '%T%');

--REGEX 
SELECT employee_id AS "Employee ID",
	   first_name AS "First Name",
	   last_name AS "Last Name"
  FROM employees
 WHERE department_id IN (SELECT department_id 
					       FROM employees 
					      WHERE first_name ~ 'T');
	   				
/* Ex. 15. 
   From the following tables, write a SQL query to find those employees who earn more than the average salary and work 
   in a department with any employee whose first name contains a character a 'J'. 
   Return employee ID, first name and salary.   
   Sample table: employees
*/
 
SELECT employee_id AS "Employee ID",
	   first_name AS "First Name",
	   salary AS "Salary"
  FROM employees
 WHERE department_id IN (SELECT department_id 
 						   FROM employees 
 						  WHERE first_name LIKE '%J%')
   AND salary > (SELECT AVG(salary) 
  				   FROM employees);
								     
/* Ex. 16. 
   From the following table, write a SQL query to find those employees whose department located at 'Toronto'. 
   Return first name, last name, employee ID, job ID.   
   Sample table: employees
   Sample table: departments
   Sample table: locations
*/

SELECT e.first_name AS "First Name",
	   e.last_name AS "Last Name",
	   e.employee_id AS "Employee ID",
	   e.job_id AS "Job ID"
  FROM employees AS e
  JOIN departments AS d
    ON e.department_id = d.department_id
  JOIN locations AS l
    ON d.location_id = l.location_id
 WHERE l.city = 'Toronto';    
  				  

/* Ex. 17. 
   From the following table, write a SQL query to find those employees whose salary is lower than any salary of those employees whose job title is ‘MK_MAN’. 
   Return employee ID, first name, last name, job ID.   
   Sample table: employees
*/

SELECT employee_id AS "Employee ID",
	   first_name AS "First Name",
       last_name AS "Last Name",
       job_id AS "Job ID"
  FROM employees
 WHERE salary < ANY (SELECT salary 
					   FROM employees 
					  WHERE job_id = 'MK_MAN'); 
	
 
/* Ex. 18. 
   From the following table, write a SQL query to find those employees whose salary is lower than any salary of those employees whose job title is 'MK_MAN'. 
   Exclude employees of Job title ‘MK_MAN’. Return employee ID, first name, last name, job ID.   
   Sample table: employees
*/

SELECT employee_id AS "Employee ID",
	   first_name AS "First Name",
       last_name AS "Last Name",
       job_id AS "Job ID"
  FROM employees
 WHERE salary < ANY (SELECT salary 
 					   FROM employees 
 					   WHERE job_id = 'MK_MAN')
   AND job_id != 'MK_MAN';  

/* Ex. 19. 
   From the following table, write a SQL query to find those employees whose salary is more than any salary of those employees whose job title is 'PU_MAN'. 
   Exclude job title 'PU_MAN'. Return employee ID, first name, last name, job ID.   
   Sample table: employees
*/

SELECT employee_id AS "Employee ID",
	   first_name AS "First Name",
       last_name AS "Last Name",
       job_id AS "Job ID"
  FROM employees
 WHERE salary > ANY (SELECT salary 
 					   FROM employees 
 					  WHERE job_id = 'PU_MAN')
   AND job_id != 'PU_MAN';  

/* Ex. 20. 
   From the following table, write a SQL query to find those employees whose salary is more than average salary of any department. 
   Return employee ID, first name, last name, job ID.   
   Sample table: employees
*/

SELECT employee_id AS "Employee ID",
	   first_name AS "First Name",
       last_name AS "Last Name",
       job_id AS "Job ID"
  FROM employees
 WHERE salary > ANY (SELECT AVG(salary) 
					   FROM employees 
					  GROUP BY department_id);  
  
/* Ex. 21. 
   From the following table, write a SQL query to find any existence of those employees whose salary exceeds 3700. 
   Return first name, last name and department ID.   
   Sample table: employees
*/
-- 1
SELECT first_name AS "First Name",
       last_name AS "Last Name",
       department_id AS "Department ID"
  FROM employees
 WHERE salary > 3700; 

-- 2
SELECT first_name AS "First Name",
       last_name AS "Last Name",
       department_id AS "Department ID"
  FROM employees
 WHERE EXISTS (SELECT * FROM employees WHERE salary > 3700); 
  				 
/* Ex. 22. 
   From the following table, write a SQL query to find total salary of those departments where at least one employee works. 
   Return department ID, total salary.   
   Sample table: employees
   Sample table: departments
*/

-- 
SELECT department_id AS "Department ID",
       SUM(salary) AS "Total Salary"
  FROM employees 
 GROUP BY department_id;

/* Ex. 23. 
   Write a query to display the employee id, name ( first name and last name ) and the job id column with a modified title SALESMAN 
   for those employees whose job title is ST_MAN and DEVELOPER for whose job title is IT_PROG.   
   Sample table: employees
*/

SELECT employee_id AS "Employee ID",
	   CONCAT(first_name, ' ', last_name) AS "Name",
	   CASE job_id
	       WHEN 'ST_MAN' THEN 'SALESMAN'
	       WHEN 'IT_PROG' THEN 'DEVELOPER'
	       ELSE job_id
	   END AS "Job ID"
FROM employees;

/* Ex. 24. 
   Write a query to display the employee id, name ( first name and last name ), salary and the SalaryStatus column with a title HIGH and LOW 
   respectively for those employees whose salary is more than and less than the average salary of all employees.   
   Sample table: employees
*/  

SELECT employee_id AS "Employee ID",
	   CONCAT(first_name, ' ', last_name) AS "Name",
	   salary AS "Salary",
	   CASE 
	       WHEN salary > (SELECT AVG(salary) FROM employees) THEN 'HIGH'
	       ELSE 'LOW'
	   END AS "SalaryStatus"
  FROM employees;
   
/* Ex. 25. 
   Write a query to display the employee id, name ( first name and last name ), SalaryDrawn, AvgCompare (salary - the average salary of all employees) 
   and the SalaryStatus column with a title HIGH and LOW respectively for those employees whose salary is more than and less than the average salary of all employees.   
   Sample table: employees
*/

SELECT employee_id AS "Employye ID",
	   CONCAT(first_name, ' ', last_name) AS "Name",
	   salary AS "SalaryDrawn",
	   salary - (SELECT AVG(salary) FROM employees) AS "AvgCompare",
	   CASE
	       WHEN salary > (SELECT AVG(salary) FROM employees) THEN 'HIGH'
	       ELSE 'LOW'
	   END AS "SalaryStatus"
  FROM employees;
 
/* Ex. 26. 
   From the following table, write a SQL query to find all those departments where at least one or more employees work.
   Return department name.   
   Sample table: employees
   Sample table: departments
*/

SELECT d.department_name AS "Department Name"
  FROM departments AS d
  JOIN employees AS e
    ON d.department_id = e.department_id 
 GROUP BY department_name
HAVING COUNT(*) >= 1; 

/* Ex. 27. 
   From the following tables, write a SQL query to find those employees who work in departments located at 'United Kingdom'. 
   Return first name.   
   Sample table: employees
   Sample table: departments
   Sample table: locations
   Sample table: countries
*/

SELECT e.first_name AS "First Name"
  FROM employees AS e
  JOIN departments AS d
    ON e.department_id = d.department_id
  JOIN locations AS l
    ON d.location_id = l.location_id
  JOIN countries AS c
    ON l.country_id = c.country_id 
 WHERE c.country_name = 'United Kingdom';     

/* Ex. 28. 
   From the following table, write a SQL query to find those employees who earn more than average salary and who work in any of the 'IT' departments. 
   Return last name.   
   Sample table: employees
   Sample table: departments
*/

-- LIKE
SELECT last_name AS "Last Name"
  FROM employees
 WHERE salary > (SELECT AVG(salary) 
 				   FROM employees)
   AND department_id IN (SELECT department_id 
  						   FROM departments 
  						  WHERE department_name LIKE '%IT%');
  						 
-- REGEX
SELECT last_name AS "Last Name"
  FROM employees
 WHERE salary > (SELECT AVG(salary) 
 				   FROM employees)
   AND department_id IN (SELECT department_id 
  						   FROM departments 
  						  WHERE department_name ~ 'IT');

/* Ex. 29. 
   From the following table, write a SQL query to find all those employees who earn more than an employee whose last name is 'Ozer'. 
   Sort the result in ascending order by last name. 
   Return first name, last name and salary.   
   Sample table: employees
*/

SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   salary AS "Salary"
  FROM employees
 WHERE salary > (SELECT salary 
 				   FROM employees 
 				  WHERE last_name = 'Ozer')
 ORDER BY last_name;  

/* Ex. 30. 
   From the following tables, write a SQL query to find those employees who work under a manager based in ‘US’. 
   Return first name, last name.   
   Sample table: employees
   Sample table: departments
   Sample table: locations
*/

-- JOIN
SELECT e.first_name AS "First Name",
	   e.last_name AS "Last Name"
  FROM employees AS e	
  JOIN departments AS d
    ON e.department_id = d.department_id
  JOIN locations AS l
    ON d.location_id = l.location_id 
 WHERE country_id = 'US';    

-- Subquery
SELECT first_name AS "First Name",
 	   last_name AS "Last Name"
  FROM employees
 WHERE employee_id IN (SELECT employee_id 
  						 FROM employees 
  						WHERE department_id IN (SELECT department_id 
  											      FROM departments 
  											     WHERE location_id IN (SELECT location_id 
  											  						     FROM locations 
  											  						    WHERE country_id = 'US')));  

/* Ex. 31. 
   From the following tables, write a SQL query to find those employees whose salary is greater than 50% of their department's total salary bill. 
   Return first name, last name.   
   Sample table : employees
*/

SELECT first_name AS "First Name",
	   last_name AS "Last Name"
  FROM employees AS e1
  JOIN (SELECT department_id, 
  			   0.5 * SUM(salary) AS sum_05
  	      FROM employees 
  	     GROUP BY department_id) AS e2
    ON e1.department_id = e2.department_id
 WHERE e1.salary > sum_05;
 											  						   
/* Ex. 32. 
   From the following tables, write a SQL query to find those employees who are managers. 
   Return all the fields of employees table.   
   Sample table: employees
   Sample table: departments
*/

-- JOIN
SELECT *
  FROM employees AS e
  JOIN departments AS d
    ON e.department_id = d.department_id
 WHERE e.employee_id = d.manager_id;

-- Subquery
SELECT *
  FROM employees 
 WHERE employee_id IN (SELECT manager_id 
						 FROM departments);
 
/* Ex. 33. 
   From the following table, write a SQL query to find those employees who manage a department. 
   Return all the fields of employees table.   
   Sample table: employees
   Sample table: departments
*/

SELECT *
  FROM employees AS e
  JOIN departments AS d
    ON e.department_id = d.department_id
 WHERE e.employee_id = d.manager_id
   AND d.manager_id != 0;

/* Ex. 34. 
   From the following table, write a SQL query to find those employees who get such a salary, which is the maximum of salaried employee, 
   joining within January 1st, 2002 and December 31st, 2003. 
   Return employee ID, first name, last name, salary, department name and city.   
   Sample table: employees
   Sample table: departments
   Sample table: locations
*/
 
SELECT e.employee_id AS "Employee ID",
	   e.first_name AS "First Name",
	   e.last_name AS "Last Name",
	   e.salary AS "Salary",
	   d.department_name AS "Department name",
	   l.city AS "City"
  FROM employees AS e
  JOIN departments AS d
    ON e.department_id = d.department_id
  JOIN locations AS l
    ON d.location_id = l.location_id 
 WHERE salary = (SELECT MAX(salary) 
				   FROM employees 
				  WHERE hire_date BETWEEN '2002-01-01' AND '2003-12-31');

/* Ex. 35. 
   From the following tables, write a SQL query to find those departments, located in the city ‘London’. 
   Return department ID, department name.   
   Sample table: departments
   Sample table: locations
*/

SELECT department_id AS "Department ID",
	   department_name AS "Department Name"
  FROM departments
 WHERE location_id = (SELECT location_id 
						FROM locations
					   WHERE city = 'London');  

/* Ex. 36. 
   From the following table, write a SQL query to find those employees who earn more than the average salary. Sort the result-set in descending order by salary. 
   Return first name, last name, salary, and department ID.   
   Sample table: employees
*/

SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   salary AS "Salary",
	   department_id AS "Department ID"
  FROM employees
 WHERE salary > (SELECT AVG(salary) FROM employees)
 ORDER BY salary DESC;  
 					  
/* Ex. 37. 
   From the following table, write a SQL query to find those employees who earn more than the maximum salary of a department of ID 40. 
   Return first name, last name and department ID.   
   Sample table: employees
*/

SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   department_id AS "Department ID"
  FROM employees
 WHERE salary > (SELECT MAX(salary) 
				   FROM employees 
				  WHERE department_id = 40);

/* Ex. 38. 
   From the following table, write a SQL query to find departments for a particular location. The location matches the location of the department of ID 30. 
   Return department name and department ID.  
   Sample table: departments
*/

SELECT department_name AS "Department Name",
       department_id AS "Department ID"
  FROM departments
 WHERE location_id = (SELECT location_id 
						FROM departments 
					   WHERE department_id = 30);

/* Ex. 39. 
   From the following table, write a SQL query to find those employees who work in that department where the employee works of ID 201. 
   Return first name, last name, salary, and department ID.   
   Sample table: employees
*/

SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   salary AS "Salary",
	   department_id AS "Department ID"
  FROM employees
 WHERE department_id = (SELECT department_id 
					      FROM employees 
					     WHERE employee_id = 201);
			  
/* Ex. 40. 
   From the following table, write a SQL query to find those employees whose salary matches to the salary of the employee who works in that department of ID 40. 
   Return first name, last name, salary, and department ID.   
   Sample table: employees
*/

SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   salary AS "Salary",
	   department_id AS "Department ID"
  FROM employees
 WHERE salary = (SELECT salary 
				   FROM employees 
				  WHERE department_id = 40);					    

/* Ex. 41. 
   From the following table, write a SQL query to find those employees who work in the department 'Marketing'. 
   Return first name, last name and department ID.   
   Sample table: employees
   Sample table: departments
*/

SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   department_id AS "Department ID"
  FROM employees
 WHERE department_id = (SELECT department_id 
						  FROM departments 
						 WHERE department_name = 'Marketing'); 

/* Ex. 42. 
   From the following table, write a SQL query to find those employees who earn more than the minimum salary of a department of ID 40. 
   Return first name, last name, salary, and department ID.   
   Sample table: employees
*/

SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   salary AS "Salary",
	   department_id AS "Department ID"
  FROM employees
 WHERE salary > (SELECT MIN(salary) 
				   FROM employees 
				  WHERE department_id = 40);

	
/* Ex. 43. 
   From the following table, write a SQL query to find those employees who joined after the employee whose ID is 165. 
   Return first name, last name and hire date.   
   Sample table: employees
*/ 

SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   hire_date AS "Hire Date"
  FROM employees
 WHERE hire_date > (SELECT hire_date 
					  FROM employees 
					 WHERE employee_id = 165);  
									 
/* Ex. 44. 
   From the following table, write a SQL query to find those employees who earn less than the minimum salary of a department of ID 70. 
   Return first name, last name, salary, and department ID.   
   Sample table: employees
*/

SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   salary AS "Salary",
	   department_id AS "Department ID"
  FROM employees
 WHERE salary < (SELECT MIN(salary) 
				   FROM employees 
				  WHERE department_id = 70);

/* Ex. 45. 
   From the following table, write a SQL query to find those employees who earn less than the average salary, and 
   work at the department where the employee 'Laura' (first name) works. 
   Return first name, last name, salary, and department ID.   
   Sample table: employees
*/

SELECT first_name AS "First Name",
	   last_name AS "Last Name",
	   salary AS "Salary",
	   department_id AS "Department ID"
  FROM employees
 WHERE salary < (SELECT AVG(salary) 
 				   FROM employees)
   AND department_id = (SELECT department_id 
  						  FROM employees 
  						 WHERE first_name = 'Laura'); 
				 
/* Ex. 46. 
   From the following tables, write a SQL query to find those employees whose department is located in the city 'London'. 
   Return first name, last name, salary, and department ID.   
   Sample table: employees
   Sample table: locations
   Sample table: departments
*/
 
SELECT e.first_name AS "First Name",
	   e.last_name AS "Last Name",
	   e.salary AS "Salary",
	   e.department_id AS "Department ID"  
  FROM employees AS e
  JOIN departments AS d
    ON e.department_id = d.department_id
  JOIN locations AS l
    ON d.location_id = l.location_id
 WHERE l.city = 'London';   

/* Ex. 47. 
   From the following tables, write a SQL query to find the city of the employee of ID 134. Return city.   
   Sample table: locations
   Sample table: departments
   Sample table: employees
*/

SELECT l.city AS "City" 
  FROM employees AS e
  JOIN departments AS d
    ON e.department_id = d.department_id
  JOIN locations AS l
    ON d.location_id = l.location_id
 WHERE e.employee_id = 134; 
  					  				 
/* Ex. 48. 
   From the following tables, write a SQL query to find those departments where maximum salary is 7000 and above. 
   The employees worked in those departments have already completed one or more jobs. 
   Return all the fields of the departments.   
   Sample table: departments
   Sample table: employees
   Sample table: job_history
*/
-- JOIN
SELECT DISTINCT d.*
  FROM departments AS d
  JOIN (SELECT department_id 
  		  FROM employees 
  		 GROUP BY department_id 
  		HAVING MAX(salary) >= 7000) AS e
    ON d.department_id = e.department_id
  JOIN (SELECT department_id 
  		  FROM job_history 
  		  WHERE employee_id IN (SELECT employee_id 
  		     					  FROM employees 
  		     					  GROUP BY employee_id 
  		     					  HAVING COUNT(*) >= 1)) AS j 
    ON d.department_id = j.department_id;

-- Subquery   			 
SELECT departments.*
  FROM departments
 WHERE department_id IN (SELECT department_id 
 						   FROM employees 
 						  GROUP BY department_id 
 						 HAVING MAX(salary) >= 7000)
   AND department_id IN (SELECT department_id 
  						   FROM job_history 
  						  WHERE employee_id IN (SELECT employee_id 
  						 						  FROM employees 
  						 						 GROUP BY employee_id 
  						 						HAVING COUNT(*) >= 1));
  						 					
-- JOIN + CTE 						 					
WITH e AS (SELECT department_id 
  		     FROM employees 
  	        GROUP BY department_id 
  	       HAVING MAX(salary) >= 7000),  
     j AS (SELECT department_id 
  		 	 FROM job_history 
  		    WHERE employee_id IN (SELECT employee_id 
  		     	  			        FROM employees 
  		     			           GROUP BY employee_id 
  		     				      HAVING COUNT(*) >= 1))  	
SELECT DISTINCT d.*
  FROM departments AS d
  JOIN e
    ON d.department_id = e.department_id
  JOIN j 
    ON d.department_id = j.department_id;
   
/* Ex. 49. 
   From the following tables, write a SQL query to find those departments where starting salary is at least 8000. 
   Return all the fields of departments.   
   Sample table: departments
   Sample table: employees
*/
 
SELECT *
  FROM departments
 WHERE department_id IN (SELECT department_id 
						   FROM employees 
						  GROUP BY department_id 
						 HAVING MIN(salary) >= 8000);
						
/* Ex. 50. 
   From the following table, write a SQL query to find those managers who supervise four or more employees. 
   Return manager name, department ID.   
   Sample table : employees
*/
						
SELECT CONCAT(e1.first_name, ' ', last_name) AS "Manager Name",
	   department_id AS "Department ID"
  FROM employees AS e1
  JOIN (SELECT manager_id 
          FROM employees 
         GROUP BY manager_id 
        HAVING COUNT(*) >= 4) AS e2
    ON e1.employee_id = e2.manager_id;

/* Ex. 51. 
   From the following table, write a SQL query to find those employees who worked as a 'Sales Representative' in the past. 
   Return all the fields of jobs.   
   Sample table: jobs
   Sample table: employees
   Sample table: job_history
*/

-- It's a strange question because we shoud find employes but select columns from the job-table. It is more logical to show 
-- the employee-table. Otherwise we don't need to use the job-history table and employees-table.

SELECT *
  FROM employees 
 WHERE employee_id IN (SELECT employee_id 
						 FROM job_history 
						WHERE job_id = (SELECT job_id 
										  FROM jobs 
										 WHERE job_title = 'Sales Representative'));
-- 
SELECT *
  FROM jobs 
 WHERE job_title = 'Sales Representative';

-- 
SELECT j.*
  FROM jobs AS j
  JOIN job_history AS jh
    ON j.job_id = jh.job_id
  JOIN employees AS e
    ON j.job_id = e.job_id
 WHERE e.employee_id IN (SELECT employee_id 
						 FROM job_history 
						WHERE job_id = (SELECT job_id 
										  FROM jobs 
										 WHERE job_title = 'Sales Representative'));
										
/* Ex. 52. 
   From the following table, write a SQL query to find those employees who earn second-lowest salary of all the employees. 
   Return all the fields of employees.   
   Sample table : employees
*/  
 
-- Rank 1
SELECT *
  FROM (SELECT *, 
               DENSE_RANK () OVER (ORDER BY salary) AS salary_rank
          FROM employees) AS emp_rank
  WHERE salary_rank = 2;  	
 
 -- Rank 2
SELECT *
  FROM (SELECT *, 
               RANK () OVER (ORDER BY salary) AS salary_rank
          FROM employees) AS emp_rank
  WHERE salary_rank = 2;   

-- Subquery 1
SELECT *
  FROM employees
 WHERE salary > (SELECT MIN(salary) FROM employees)
 ORDER BY salary
 LIMIT 2; 
										
-- Subquery 2									
SELECT *
  FROM employees
 WHERE salary = (SELECT MIN(salary) 
				   FROM (SELECT salary 
				           FROM employees 
				          WHERE salary != (SELECT MIN(salary) 
				                             FROM employees)) AS e1);			                            
  
-- Offset 1
SELECT *
  FROM employees
 ORDER BY salary
OFFSET 1
 LIMIT 2;

-- Offset 2
SELECT * 
  FROM employees 
 WHERE salary = (SELECT DISTINCT salary 
				   FROM employees 
				  ORDER BY salary 
				 OFFSET 1 
				  LIMIT 1);  
         
/* Ex. 53. 
   From the following table, write a SQL query to find those departments managed by ‘Susan’. 
   Return all the fields of departments.  
   Sample table: departments
   Sample table: employees
*/

-- Subquery				 
SELECT *
  FROM departments
 WHERE department_id IN (SELECT department_id 
						   FROM employees 
						  WHERE first_name = 'Susan');
-- JOIN						 
SELECT *
  FROM departments AS d
  JOIN employees AS e
    ON d.department_id = e.department_id
 WHERE e.first_name = 'Susan';
  
/* Ex. 54. 
   From the following table, write a SQL query to find those employees who earn highest salary in a department. 
   Return department ID, employee name, and salary.   
   Sample table: employees
*/

-- Subquery
SELECT department_id AS "Department_ID",
	   CONCAT(e.first_name, ' ', e.last_name) AS "Employee Name",
	   salary AS "Salary"
  FROM employees AS e
 WHERE salary = (SELECT MAX(salary) 
                   FROM employees 
                  WHERE e.department_id = department_id);
 
SELECT MAX(salary), department_id FROM employees GROUP BY department_id;  

-- JOIN
  WITH max_sal AS (SELECT MAX(salary) AS max_salary, 
  						  department_id 
  				     FROM employees 
  				    GROUP BY department_id)
SELECT e.department_id AS "Department_ID",
	   CONCAT(e.first_name, ' ', e.last_name) AS "Employee Name",
	   e.salary AS "Salary"
  FROM employees AS e
  JOIN max_sal
    ON e.department_id = max_sal.department_id
   AND e.salary = max_sal.max_salary;
 
/* Ex. 55. 
   From the following table, write a SQL query to find those employees who did not have any job in the past. 
   Return all the fields of employees.   
   Sample table: employees
   Sample table: job_history
*/  

SELECT *
  FROM employees
 WHERE employee_id NOT IN (SELECT employee_id 
						     FROM job_history); 
  
SELECT *
  FROM employees;
 --LIMIT 20; 
 					 
SELECT *
  FROM departments;	
 
SELECT *
  FROM locations;

SELECT *
  FROM countries; 
 
SELECT *
  FROM job_history;
 
SELECT *
  FROM jobs;   


