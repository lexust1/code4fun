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







