/* Connect to sqlex database
   Exercises from w3 */
   
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
FROM   nobel_win
WHERE  year = 1971
AND    subject = 'Literature';

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
FROM   nobel_win
WHERE  subject = 'Physics'
AND    year >= 1950;

/* Ex. 16.  
    Write a SQL query to Show all the details (year, subject, winner, country ) of the Chemistry prize winners between the year 1965 to 1975 inclusive.
	Sample table: nobel_win
*/

SELECT year, subject, winner, country
FROM   nobel_win
WHERE  year BETWEEN 1965 AND 1975
AND    subject = 'Chemistry';


