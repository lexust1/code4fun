/* Connect to sqlex database
   Exercises from w3 */

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

/* Ex. 7. 
   From the following table, write a SQL query to calculate the maximum purchase amount 
   generated by each sales person for every order date. Sort the result-set by sales 
   person id and order date in ascending order. 
   Return sales person id, order date and maximum purchase amount.  
   Sample table: orders
*/ 

/* Ex. 8. 
   From the following table, write a SQL query to find all the customers. 
   Sort the result-set in descending order on 3rd field. Return customer name, city and grade.    
   Sample table: customer
*/ 

/* Ex. 9. 
   From the following table, write a SQL query to count the unique orders, highest purchase amount for each customer. 
   Sort the result-set in descending order on 2nd field. Return customer ID, 
   number of distinct orders and highest purchase amount by each customer.   
   Sample table: orders
*/ 

/* Ex. 10. 
   From the following table, write a SQL query to calculate summation of purchase amount, 
   total commission (15% for all salesmen) by each order date. Sort the result-set on order date. 
   Return order date, summation of purchase amount and commission.   
   Sample table : orders
*/ 


 