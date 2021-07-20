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



