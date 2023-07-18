SELECT * 
  FROM aircrafts;

SELECT *
  FROM airports;
  

 SELECT *
  FROM aircrafts
 WHERE model LIKE 'Airbus%'; 


SELECT *
  FROM aircrafts
 WHERE model NOT LIKE 'Airbus%'
   AND model NOT LIKE 'Boeing%';
 
  
SELECT *
  FROM airports
 WHERE airport_name LIKE '___'; 
 

SELECT *
  FROM aircrafts 
 WHERE model ~ '^Airbus'; 
 
SELECT *
  FROM aircrafts 
 WHERE model ~ '^(Airbus|Boeing)'; 
 

SELECT *
  FROM aircrafts
 WHERE model !~ '300$'; 
 

SELECT *
  FROM aircrafts
 WHERE range BETWEEN 3000 AND 6000; 
 

SELECT range AS "Range, km",
	   ROUND(range / 1.609, 0) AS "Range, ml"
  FROM aircrafts;	
 
SELECT *
  FROM aircrafts 
 ORDER BY range DESC; 


SELECT DISTINCT timezone
  FROM airports;

 
SELECT airport_name AS "Airport",
	   city AS "City",
	   longitude AS "Longitude"
  FROM airports
 ORDER BY longitude DESC
 LIMIT 3;
 
SELECT airport_name AS "Airport",
	   city AS "City",
	   longitude AS "Longitude"
  FROM airports
 ORDER BY "Longitude" DESC
 LIMIT 3;
 
SELECT airport_name AS "Airport",
	   city AS "City",
	   longitude AS "Longitude"
  FROM airports
 ORDER BY longitude DESC
 LIMIT 3
OFFSET 3;


SELECT model AS "Model",
	   range AS "Range",
	   CASE 
	       WHEN range < 2000 THEN 'Ближнемагистральный'
	       WHEN range < 5000 THEN 'Среднемагистральный'
	       ELSE 'Дальнемагистральный'
	   END AS "Type"   
  FROM aircrafts
 ORDER BY model;
  


SELECT *
  FROM aircrafts;
  
SELECT *
  FROM seats;
 
SELECT a.aircraft_code AS "Aircraft Code",
	   a.model AS "Model",
	   s.seat_no AS "Seat number",
	   s.fare_conditions AS "Fare conditions"
  FROM aircrafts AS a 
  JOIN seats AS s
    ON a.aircraft_code = s.aircraft_code
 WHERE a.model ~ '^Cessna'
 ORDER BY s.seat_no;

 
SELECT a.aircraft_code AS "Aircraft Code",
	   a.model AS "Model",
	   s.seat_no AS "Seat number",
	   s.fare_conditions AS "Fare conditions"
  FROM aircrafts AS a, seats AS s
 WHERE a.aircraft_code = s.aircraft_code
   AND a.model ~ '^Cessna'
 ORDER BY s.seat_no;


SELECT *
  FROM routes;
 
SELECT * 
  FROM aircrafts;

SELECT r.aircraft_code, a.model, COUNT(*) AS num_routes
  FROM routes AS r
  JOIN aircrafts AS a 
    ON r.aircraft_code = a.aircraft_code
 GROUP BY 1, 2
 ORDER BY 3 DESC;

SELECT r.aircraft_code, a.model, COUNT(*) AS num_routes
  FROM routes AS r
  FULL OUTER JOIN aircrafts AS a 
    ON r.aircraft_code = a.aircraft_code
 GROUP BY 1, 2
 ORDER BY 3 DESC;

SELECT r.aircraft_code, a.model, COUNT(r.aircraft_code) AS num_routes
  FROM routes AS r
 RIGHT OUTER JOIN aircrafts AS a 
    ON r.aircraft_code = a.aircraft_code
 GROUP BY 1, 2
 ORDER BY 3 DESC;


SELECT f.flight_no,
       f.scheduled_departure,
       f.flight_id,
       f.departure_airport,
       f.arrival_airport,
       f.aircraft_code,
       t.passenger_name,
       tf.fare_conditions AS fc_to_be,
       s.fare_conditions AS fc_fact,
       b.seat_no
  FROM boarding_passes b
  JOIN ticket_flights tf
    ON b.ticket_no = tf.ticket_no AND b.flight_id = tf.flight_id
  JOIN tickets t ON tf.ticket_no = t.ticket_no
  JOIN flights f ON tf.flight_id = f.flight_id
  JOIN seats s
    ON b.seat_no = s.seat_no AND f.aircraft_code = s.aircraft_code
 WHERE tf.fare_conditions <> s.fare_conditions
 ORDER BY f.flight_no, f.scheduled_departure;



SELECT r.min_sum, r.max_sum, count( b.* )
  FROM bookings b
  RIGHT OUTER JOIN
   ( VALUES (       0,  100000 ), (  100000,  200000 ),
            (  200000,  300000 ), (  300000,  400000 ),
            (  400000,  500000 ), (  500000,  600000 ),
            (  600000,  700000 ), (  700000,  800000 ),
            (  800000,  900000 ), (  900000, 1000000 ),
            ( 1000000, 1100000 ), ( 1100000, 1200000 ),
            ( 1200000, 1300000 )
   ) AS r ( min_sum, max_sum )
   ON b.total_amount >= r.min_sum AND b.total_amount < r.max_sum
  GROUP BY r.min_sum, r.max_sum
  ORDER BY r.min_sum;



SELECT *
  FROM routes;
 
SELECT arrival_city 
  FROM routes
 WHERE departure_city = 'Москва'
 
 UNION 
 
SELECT arrival_city
  FROM routes
 WHERE departure_city = 'Санкт-Петербург'
 ORDER BY arrival_city; 
 
SELECT arrival_city 
  FROM routes
 WHERE departure_city = 'Москва'
 
INTERSECT

SELECT arrival_city
  FROM routes
 WHERE departure_city = 'Санкт-Петербург'
 ORDER BY arrival_city; 
 

SELECT arrival_city 
  FROM routes
 WHERE departure_city = 'Санкт-Петербург'
 
EXCEPT 
 
SELECT arrival_city
  FROM routes
 WHERE departure_city = 'Москва'
 ORDER BY arrival_city; 
 
SELECT arrival_city, COUNT(*)
  FROM routes
 WHERE departure_city = 'Москва'
 GROUP BY arrival_city
 ORDER BY count DESC;

SELECT *
  FROM routes;

SELECT array_length( days_of_week, 1 ) AS days_per_week,
       count(*) AS num_routes
  FROM routes
  GROUP BY days_per_week
  ORDER BY 1 desc;

SELECT departure_city, count(*)
  FROM routes
  GROUP BY departure_city
  HAVING count(*) >= 15
  ORDER BY count DESC; 
 
 SELECT city, count(*)
  FROM airports
  GROUP BY city
  HAVING count(*) > 1;

 
SELECT b.book_ref,
       b.book_date,
       extract( 'month' from b.book_date ) AS month,
       extract( 'day'   from b.book_date ) AS day,
       count( * ) OVER (
         PARTITION BY date_trunc( 'month', b.book_date )
         ORDER BY b.book_date
       ) AS count
  FROM ticket_flights tf
  JOIN tickets  t ON tf.ticket_no = t.ticket_no
  JOIN bookings b ON t.book_ref = b.book_ref
  WHERE tf.flight_id = 1
  ORDER BY b.book_date; 
  
 
SELECT airport_name,
       city,
       round( latitude::numeric, 2 ) AS ltd,
       timezone,
       rank() OVER (
         PARTITION BY timezone
         ORDER BY latitude DESC
       )
  FROM airports
  WHERE timezone IN ( 'Asia/Irkutsk', 'Asia/Krasnoyarsk' )
  ORDER BY timezone, rank;
 
 
SELECT airport_name, city, timezone, latitude,
       first_value( latitude )            OVER tz AS first_in_timezone,
       latitude - first_value( latitude ) OVER tz AS delta,
       rank()                             OVER tz
  FROM airports
  WHERE timezone IN ( 'Asia/Irkutsk', 'Asia/Krasnoyarsk' )
  WINDOW tz AS ( PARTITION BY timezone ORDER BY latitude DESC )
  ORDER BY timezone, rank;
  
 
SELECT flight_no, departure_city, arrival_city
  FROM routes
  WHERE departure_city IN (
      SELECT city
        FROM airports
        WHERE timezone ~ 'Krasnoyarsk'
    )
    AND arrival_city IN (
      SELECT city
        FROM airports
        WHERE timezone ~ 'Krasnoyarsk'
); 

SELECT airport_name, city, longitude
  FROM airports
  WHERE longitude IN (
   ( SELECT max( longitude ) FROM airports ),
   ( SELECT min( longitude ) FROM airports )
  )
  ORDER BY longitude;
  
SELECT DISTINCT a.city
  FROM airports a
  WHERE NOT EXISTS (
    SELECT * FROM routes r
      WHERE r.departure_city = 'Москва'
        AND r.arrival_city = a.city
    )
    AND a.city <> 'Москва'
  ORDER BY city;
 
SELECT a.model,
  ( SELECT count( * )
      FROM seats s
      WHERE s.aircraft_code = a.aircraft_code
        AND s.fare_conditions = 'Business'
  ) AS business,
  ( SELECT count( * )
      FROM seats s
      WHERE s.aircraft_code = a.aircraft_code
        AND s.fare_conditions = 'Comfort'
  ) AS comfort,
  ( SELECT count( * )
      FROM seats s
      WHERE s.aircraft_code = a.aircraft_code
        AND s.fare_conditions = 'Economy'
  ) AS economy
  FROM aircrafts a
  ORDER BY 1; 
 
 
SELECT s2.model,
  string_agg(
     s2.fare_conditions || ' (' || s2.num || ')',
', ' )
  FROM (
    SELECT a.model,
        s.fare_conditions,
        count( * ) AS num
      FROM aircrafts a
      JOIN seats s ON a.aircraft_code = s.aircraft_code
      GROUP BY 1, 2
      ORDER BY 1, 2
  ) AS s2
  GROUP BY s2.model
  ORDER BY s2.model; 
 
 
SELECT aa.city, aa.airport_code, aa.airport_name
  FROM (
    SELECT city, count( * )
      FROM airports
      GROUP BY city
      HAVING count( * ) > 1
    ) AS a
  JOIN airports AS aa ON a.city = aa.city
  ORDER BY aa.city, aa.airport_name;
 
 
 SELECT departure_airport, departure_city, count( * )
  FROM routes
  GROUP BY departure_airport, departure_city
  HAVING departure_airport IN (
    SELECT airport_code
      FROM airports
      WHERE longitude > 150
  )
  ORDER BY count DESC;
 
 
SELECT ts.flight_id,
       ts.flight_no,
       ts.scheduled_departure_local,
       ts.departure_city,
       ts.arrival_city,
       a.model,
       ts.fact_passengers,
       ts.total_seats,
       round( ts.fact_passengers::numeric /
              ts.total_seats::numeric, 2 ) AS fraction
  FROM (
    SELECT f.flight_id,
           f.flight_no,
           f.scheduled_departure_local,
           f.departure_city,
           f.arrival_city,
           f.aircraft_code,
           count( tf.ticket_no ) AS fact_passengers,
           ( SELECT count( s.seat_no )
FROM seats s
               WHERE s.aircraft_code = f.aircraft_code
           ) AS total_seats
      FROM flights_v f
      JOIN ticket_flights tf ON f.flight_id = tf.flight_id
      WHERE f.status = 'Arrived'
      GROUP BY 1, 2, 3, 4, 5, 6
  ) AS ts
  JOIN aircrafts AS a ON ts.aircraft_code = a.aircraft_code
  ORDER BY ts.scheduled_departure_local;
 
 
 WITH ts AS
( SELECT f.flight_id,
         f.flight_no,
         f.scheduled_departure_local,
         f.departure_city,
         f.arrival_city,
         f.aircraft_code,
         count( tf.ticket_no ) AS fact_passengers,
         ( SELECT count( s.seat_no )
FROM seats s
             WHERE s.aircraft_code = f.aircraft_code
         ) AS total_seats
    FROM flights_v f
    JOIN ticket_flights tf ON f.flight_id = tf.flight_id
    WHERE f.status = 'Arrived'
    GROUP BY 1, 2, 3, 4, 5, 6
)
SELECT ts.flight_id,
       ts.flight_no,
       ts.scheduled_departure_local,
       ts.departure_city,
       ts.arrival_city,
       a.model,
       ts.fact_passengers,
       ts.total_seats,
       round( ts.fact_passengers::numeric /
              ts.total_seats::numeric, 2 ) AS fraction
  FROM ts
  JOIN aircrafts AS a ON ts.aircraft_code = a.aircraft_code
  ORDER BY ts.scheduled_departure_local;
  
 
 WITH RECURSIVE ranges ( min_sum, max_sum ) AS
  ( VALUES ( 0, 100000 )
    UNION ALL
    SELECT min_sum + 100000, max_sum + 100000
      FROM ranges
      WHERE max_sum <
       ( SELECT max( total_amount ) FROM bookings )
  )
SELECT * FROM ranges;


WITH RECURSIVE ranges ( min_sum, max_sum ) AS
  ( VALUES( 0, 100000 )
    UNION ALL
    SELECT min_sum + 100000, max_sum + 100000
      FROM ranges
      WHERE max_sum <
        ( SELECT max( total_amount ) FROM bookings )
  )
SELECT r.min_sum, r.max_sum, count( b.* )
  FROM bookings b
  RIGHT OUTER JOIN ranges r
    ON b.total_amount >= r.min_sum
    AND b.total_amount < r.max_sum
  GROUP BY r.min_sum, r.max_sum
  ORDER BY r.min_sum;
 
  
 /*--------------------------------------------------------------------*/
 
 
/* 1. В документации сказано, что служебный символ «%» в шаблоне оператора LIKE соответствует 
любой последовательности символов, в том числе и пустой после- довательности, однако ничего 
не сказано насчет правил обработки пробелов.

В таблице «Билеты» (tickets) столбец passenger_name содержит имя и фамилию пассажира, записанные 
заглавными латинскими буквами и разделенные одним пробелом.

Выясните правила обработки пробелов самостоятельно, выполнив следующие команды и сравнив 
полученные результаты:

     SELECT count( * ) FROM tickets;
     SELECT count( * ) FROM tickets WHERE passenger_name LIKE '% %';
     SELECT count( * ) FROM tickets WHERE passenger_name LIKE '% % %';
     SELECT count( * ) FROM tickets WHERE passenger_name LIKE '% %%';
*/ 
 
SELECT *
  FROM tickets;
 
SELECT COUNT(*) FROM tickets;
 
SELECT COUNT(*)
  FROM tickets
 WHERE passenger_name LIKE '% %'; 
 
SELECT COUNT(*)
  FROM tickets
 WHERE passenger_name LIKE '% % %'; 
  
SELECT COUNT(*)
  FROM tickets
 WHERE passenger_name LIKE '% %%'; 
 
/* 
2. Этот запрос выбирает из таблицы «Билеты» (tickets) всех пассажиров с именами, состоящими из трех букв
 (в шаблоне присутствуют три символа «_»):
   SELECT passenger_name
     FROM tickets
     WHERE passenger_name LIKE '___ %';
Предложите шаблон поиска в операторе LIKE для выбора из этой таблицы всех пассажиров с фамилиями, 
состоящими из пяти букв.
*/ 
SELECT passenger_name
  FROM tickets;

SELECT passenger_name
  FROM tickets
 WHERE passenger_name LIKE '% _____';
 
 
/*
 3. В разделе документации 9.7.2 «Регулярные выражения SIMILAR TO» рассматривается оператор SIMILAR TO. 
 Он работает аналогично оператору LIKE, но использует шаблоны, соответствующие определению регулярных выражений, 
 приведенному в стандарте SQL. Регулярные выражения SQL представляют собой комбинацию синтаксиса LIKE с синтаксисом 
 обычных регулярных выражений. Самостоятельно ознакомьтесь с оператором SIMILAR TO. 
 */
  
SELECT passenger_name
  FROM tickets
 WHERE passenger_name SIMILAR TO '% _____';

SELECT passenger_name
  FROM tickets
 WHERE passenger_name SIMILAR TO '% _{5}';

SELECT passenger_name
  FROM tickets
 WHERE passenger_name ~ '^.{5}$';

SELECT passenger_name
  FROM tickets
 WHERE passenger_name ~ '^.+ .{5}$';


/*
 4. В разделе документации 9.2 «Функция и операторы сравнения» представлены различные предикаты сравнения, кроме предиката BETWEEN, 
 рассмотренного в этой главе. Самостоятельно ознакомьтесь с ними.
*/

/*
Equal to (=): This predicate checks if two values are equal.
Not equal to (<> or !=): This predicate checks if two values are not equal.
Greater than (>), Greater than or equal to (>=): These predicates compare if one value is greater than or equal to another.
Less than (<), Less than or equal to (<=): These predicates compare if one value is less than or equal to another.
LIKE: This predicate is used to perform pattern matching using wildcards, such as % and _.
IN: This predicate checks if a value is included in a specified list of values.
IS NULL, IS NOT NULL: These predicates check if a value is NULL or not NULL, respectively.
EXISTS: This predicate checks for the existence of rows in a subquery.
ANY/SOME, ALL: These predicates are used in combination with a comparison operator to compare a value with a set of values returned by a subquery.
 */
 

/* 
 
5. В разделе документации 9.17 «Условные выражения» представлены услов- ные выражения, которые поддерживаются в PostgreSQL. 
В тексте главы была рассмотрена конструкция CASE. Самостоятельно ознакомьтесь с функциями COALESCE, NULLIF, GREATEST и LEAST.
 */

/*
COALESCE: The COALESCE function allows you to return the first non-null expression from a list of expressions. 
It takes multiple arguments and returns the first non-null value. If all the arguments are null, it returns null. Here's an example:


SELECT COALESCE(column_name, 'Default Value') AS result
FROM your_table;

NULLIF: The NULLIF function compares two expressions and returns null if they are equal; otherwise, it returns the first expression. 
It is useful when you want to handle a specific value as null. Here's an example:

SELECT NULLIF(column_name, 'Value to compare') AS result
FROM your_table;

GREATEST: The GREATEST function returns the greatest (maximum) value from a list of expressions. 
It can take two or more arguments and returns the highest value. Here's an example:


SELECT GREATEST(column1, column2, column3) AS result
FROM your_table;

LEAST: The LEAST function returns the smallest (minimum) value from a list of expressions. Similar to GREATEST, 
it can take two or more arguments and returns the lowest value. Here's an example:


SELECT LEAST(column1, column2, column3) AS result
FROM your_table;
*/

/*
6. Выясните, на каких маршрутах используются самолеты компании Boeing. В выборке вместо кода модели должно выводиться ее наименование, 
например, вместо кода 733 должно быть Boeing 737-300.
Указание: можно воспользоваться соединением представления «Маршруты» (routes) и таблицы «Самолеты» (aircrafts).
*/

SELECT * 
  FROM aircrafts;
 
SELECT *
  FROM routes;
 
SELECT r.departure_city AS "Departure city",
	   r.arrival_city AS "Arrival city",
	   a.model AS "Model"
  FROM aircrafts AS a
  JOIN routes AS r
    ON a.aircraft_code = r.aircraft_code
 WHERE a.model LIKE 'Boeing%';  

/*
7. Самые крупные самолеты в нашей авиакомпании — это Boeing 777-300. Выяс- нить, между какими парами городов они летают, поможет запрос:
SELECT DISTINCT departure_city, arrival_city
  FROM routes r
  JOIN aircrafts a ON r.aircraft_code = a.aircraft_code
  WHERE a.model = 'Boeing 777-300'
  ORDER BY 1;
 departure_city | arrival_city
----------------+--------------
 Екатеринбург
 Москва
 Москва
 Москва
 Москва
 Новосибирск
 Пермь
 Сочи
(8 строк)
| Москва
| Екатеринбург
| Новосибирск
| Пермь
| Сочи
| Москва
| Москва
| Москва
К сожалению, в этой выборке информация дублируется. Пары городов приведены по два раза: для рейса «туда» и для рейса «обратно». 
Модифицируйте запрос таким образом, чтобы каждая пара городов была выведена только один раз:
 departure_city | arrival_city
----------------+--------------
 Москва
 Новосибирск
 Пермь
 Сочи
(4 строки)
| Екатеринбург
| Москва
| Москва
| Москва

*/

SELECT DISTINCT departure_city, arrival_city
  FROM routes r
  JOIN aircrafts a ON r.aircraft_code = a.aircraft_code
 WHERE a.model = 'Boeing 777-300'
 ORDER BY 1;

SELECT DISTINCT LEAST(departure_city, arrival_city) AS "City A", 
	   GREATEST(departure_city, arrival_city) AS "City B"
  FROM routes r
  JOIN aircrafts a ON r.aircraft_code = a.aircraft_code
 WHERE a.model = 'Boeing 777-300'
 ORDER BY 1;
 
/*
8. В тексте главы мы рассматривали различные примеры использования левого и правого внешних соединений: LEFT OUTER JOIN и RIGHT OUTER JOIN. 
Напишите запрос, в котором использовалось бы полное внешнее соединение — FULL OUTER JOIN.
*/

SELECT a.aircraft_code AS a_code,
       a.model,
       r.aircraft_code AS r_code,
       count( r.aircraft_code ) AS num_routes
  FROM aircrafts a
  FULL OUTER JOIN routes r ON r.aircraft_code = a.aircraft_code
  GROUP BY 1, 2, 3
  ORDER BY 4 DESC;
  
 /*
 9. Для ответа на вопрос, сколько рейсов выполняется из Москвы в Санкт-Петер- бург, можно написать совсем простой запрос:
   SELECT count( * )
     FROM routes
     WHERE departure_city = 'Москва'
         AND arrival_city = 'Санкт-Петербург';
      count
     -------
12
(1 строка)

А с помощью какого запроса можно получить результат в таком виде?
     departure_city |  arrival_city   | count
    ----------------+-----------------+-------
     Москва         | Санкт-Петербург |    12
(1 строка)
 */
 
SELECT departure_city,
	   arrival_city,
	   COUNT(*)
  FROM routes
 WHERE departure_city = 'Москва'
   AND arrival_city = 'Санкт-Петербург'
 GROUP BY departure_city, arrival_city; 
 

/*
10. Выяснить, сколько различных рейсов выполняется из каждого города, без учета частоты рейсов в неделю, 
можно с помощью обращения к представлению «Маршруты» (routes):
    SELECT departure_city, count( * )
      FROM routes
      GROUP BY departure_city
      ORDER BY count DESC;
         departure_city       | count
    --------------------------+-------
 Москва
 Санкт-Петербург
 Новосибирск
 ...
 Благовещенск
 Братск
(101 строка)
| 154 | 35 | 19
| 1 | 1
Модифицируйте этот запрос так, чтобы он выводил число направлений, по которым летают самолеты из каждого города. 
Например, из Москвы в Санкт-Петербург летает несколько различных рейсов, но все эти рейсы относятся к одному направлению.

Указание: нужно передать параметр в функцию count.
 */
SELECT departure_city, COUNT(DISTINCT arrival_city)
  FROM routes
 GROUP BY departure_city
 ORDER BY COUNT DESC;


/* 
11. В материализованном представлении «Маршруты» (routes) имеется столбец days_of_week, который содержит списки (массивы) 
номеров дней недели, когда выполняется каждый рейс.
Для оптимизации расписания вылетов из Москвы нужно выявить пять городов, в которые из столицы отправляется наибольшее 
число ежедневных рейсов (маршрутов). Строки в выборке следует расположить в убывающем порядке числа выполняемых рейсов.

Указание: воспользуйтесь функцией array_length.
 */
SELECT *
  FROM routes;
 
SELECT arrival_city,
	   COUNT(*) AS daily_flights
  FROM routes	   
 WHERE departure_city = 'Москва'
   AND array_length(days_of_week, 1) = 7
 GROUP BY arrival_city 
 ORDER BY daily_flights DESC
 LIMIT 5;
 
/*
12.* Предположим, что служба материального снабжения нашей авиакомпании за- просила информацию о числе рейсов, 
выполняющихся из Москвы в каждый день недели.
Результат можно получить путем выполнения семи аналогичных запросов: по одному для каждого дня недели. Начнем с понедельника:
     SELECT 'Понедельник' AS day_of_week, count( * ) AS num_flights
       FROM routes
       WHERE departure_city = 'Москва'
         AND days_of_week @> '{ 1 }'::integer[];

В этом запросе используется оператор @>, который проверяет, содержатся ли все элементы массива, стоящего справа от него, 
в том массиве, который находится слева. В правом массиве всего один элемент — номер интересующего нас дня недели.
      day_of_week | num_flights
     -------------+-------------
      Понедельник |         131
(1 строка)

Запрос для вторника отличается лишь номером дня недели в массиве.
     SELECT 'Вторник' AS day_of_week, count( * ) AS num_flights
       FROM routes
       WHERE departure_city = 'Москва'
         AND days_of_week @> '{ 2 }'::integer[];
      day_of_week | num_flights
     -------------+-------------
      Вторник     |         134
(1 строка)

Нужно выполнить еще пять аналогичных команд, чтобы получить результаты для всех дней недели. Очевидно, что это нерациональный способ.
Получить требуемый результат можно с помощью одного запроса:
     SELECT unnest( days_of_week ) AS day_of_week,
            count( * ) AS num_flights
       FROM routes
       WHERE departure_city = 'Москва'
       GROUP BY day_of_week
       ORDER BY day_of_week;
       
  day_of_week | num_flights
-------------+-------------
1| 131 2| 134 3| 126 4| 136 5| 124 6| 133 7| 124
(7 строк)

Задание 1. Самостоятельно разберитесь, как работает приведенный запрос. Выясните, что делает функция unnest. Для того чтобы найти ее описание, 
можно воспользоваться теми разделами документации, которые были указа- ны в главе 4. Однако можно воспользоваться и предметным указателем (Index), 
ссылка на который находится в самом низу оглавления документации.
В качестве вспомогательного запроса, проясняющего работу функции unnest, можно выполнить следующий:
SELECT flight_no, unnest( days_of_week ) AS day_of_week
  FROM routes
  WHERE departure_city = 'Москва'
  ORDER BY flight_no;
  
Задание 2. Использование номеров дней недели в предыдущей выборке не должно вызывать затруднений. Но все-таки предположим, что нас попросили 
модифицировать запрос, чтобы результат выводился в таком виде:
 name_of_day | num_flights
-------------+-------------
 Пн.         |         131
 Вт.         |         134
 Ср.         |         126
 Чт.         |         136
 Пт.         |         124
 Сб.         |         133
 Вс.         |         124
(7 строк)

Покажем одно из возможных решений задачи. Оно основано на использовании специальной табличной функции unnest в предложении FROM. Подробно об 
этом написано в документации в разделе 7.2.1.4 «Табличные функции». Функция может принимать любое число параметров-массивов, а возвращает набор
строк, которые могут использоваться в запросах как обычные таблицы. В этих наборах строк столбцы формируются из значений, содержащихся в массивах.
    SELECT dw.name_of_day, count( * ) AS num_flights
      FROM (
        SELECT unnest( days_of_week ) AS num_of_day
          FROM routes
          WHERE departure_city = 'Москва'
        ) AS r,
        unnest( '{ 1, 2, 3, 4, 5, 6, 7 }'::integer[],
          '{ "Пн.", "Вт.", "Ср.", "Чт.", "Пт.", "Сб.", "Вс."}'::text[]
        ) AS dw( num_of_day, name_of_day )
      WHERE r.num_of_day = dw.num_of_day
      GROUP BY r.num_of_day, dw.name_of_day
      ORDER BY r.num_of_day;
Этот запрос можно упростить. Предложение WITH ORDINALITY позволяет в нашем примере избавиться от массива целых чисел, обозначающих дни недели, 
поскольку автоматически формируется столбец целых чисел, нумерующих строки результирующего набора. По умолчанию этот столбец 
называется ordinality. Это имя можно использовать в запросе. Самостоятельно модифицируйте запрос с применением предложения WITH ORDINALITY.

 */
  
SELECT *
  FROM routes;

SELECT 'Понедельник' AS day_of_week, 
	   COUNT(*) AS num_flights
  FROM routes
 WHERE departure_city = 'Москва'
   AND days_of_week @> '{ 1 }'::integer[]; 

  
SELECT 'Вторник' AS day_of_week, 
	   COUNT(*) AS num_flights
  FROM routes
 WHERE departure_city = 'Москва'
   AND days_of_week @> '{ 2 }'::integer[];   
   
  
 SELECT UNNEST(days_of_week) AS day_of_week,
        COUNT(*) AS num_flights
   FROM routes
  WHERE departure_city = 'Москва'
  GROUP BY day_of_week
  ORDER BY day_of_week;
 
SELECT flight_no, 
	   UNNEST(days_of_week) AS day_of_week
  FROM routes
 WHERE departure_city = 'Москва'
 ORDER BY flight_no;

SELECT dw.name_of_day, count( * ) AS num_flights
      FROM (
        SELECT unnest( days_of_week ) AS num_of_day
          FROM routes
          WHERE departure_city = 'Москва'
        ) AS r,
        unnest( '{ 1, 2, 3, 4, 5, 6, 7 }'::integer[],
          '{ "Пн.", "Вт.", "Ср.", "Чт.", "Пт.", "Сб.", "Вс."}'::text[]
        ) AS dw( num_of_day, name_of_day )
      WHERE r.num_of_day = dw.num_of_day
      GROUP BY r.num_of_day, dw.name_of_day
      ORDER BY r.num_of_day;
 
SELECT dw.name_of_day, count(*) AS num_flights
FROM (
  SELECT unnest(days_of_week) AS num_of_day, ROW_NUMBER() OVER () AS row_num
  FROM routes
  WHERE departure_city = 'Москва'
) AS r
JOIN unnest('{Пн., Вт., Ср., Чт., Пт., Сб., Вс.}'::text[]) WITH ORDINALITY AS dw(name_of_day, num_of_day)
ON r.num_of_day = dw.num_of_day::integer
GROUP BY dw.name_of_day, r.num_of_day
ORDER BY r.num_of_day;

/*
Ответить на вопрос о том, каковы максимальные и минимальные цены билетов на все направления, может такой запрос:
    SELECT f.departure_city, f.arrival_city,
        max( tf.amount ), min( tf.amount )
      FROM flights_v f
      JOIN ticket_flights tf ON f.flight_id = tf.flight_id
      GROUP BY 1, 2
      ORDER BY 1, 2;
       departure_city    |     arrival_city    |    max    |   min
    ---------------------+---------------------+-----------+----------
      Абакан
      Абакан
      Абакан
      Анадырь
      Анадырь
      ...
      Якутск
      Якутск
(367 строк) 

А как выявить те направления, на которые не было продано ни одного билета? Один из вариантов решения такой: если на рейсы, 
отправляющиеся по какому-то направлению, не было продано ни одного билета, то максимальная и минимальная цены будут равны NULL. 
Нужно получить выборку в таком виде:

   departure_city    |    arrival_city     |    max    |    min
---------------------+---------------------+-----------+----------
Абакан
Абакан
Абакан
Абакан
Абакан
...
| Архангельск
| Грозный
| Кызыл
| Москва
| Новосибирск
|           |
|           |
|           |
| 101000.00 | 33700.00
|   5800.00 |  5800.00
Модифицируйте запрос, приведенный выше.
*/

SELECT *
  FROM flights_v;

SELECT flight_id,
	   flight_no
  FROM flights_v
 WHERE departure_city = 'Абакан'
   AND arrival_city = 'Москва' ;

SELECT *
  FROM flights_v
 WHERE departure_city = 'Абакан'
   AND arrival_city = 'Архангельск';

SELECT *
  FROM flights_v AS f
  FULL OUTER JOIN ticket_flights AS tf
    ON f.flight_id = tf.flight_id
 WHERE departure_city = 'Абакан'
   AND arrival_city = 'Архангельск';
  
SELECT *
  FROM flights_v AS f
  FULL OUTER JOIN ticket_flights AS tf
    ON f.flight_id = tf.flight_id
 WHERE departure_city = 'Абакан'
   AND arrival_city = 'Москва';
    
  

SELECT flight_id,
	   flight_no
  FROM flights_v
 GROUP BY flight_id, flight_no;

SELECT f.departure_city, 
	   f.arrival_city,
       MAX(tf.amount), 
       MIN(tf.amount)
  FROM flights_v AS f
  JOIN ticket_flights AS tf 
    ON f.flight_id = tf.flight_id
 GROUP BY 1, 2
 ORDER BY 1, 2;
 
SELECT f.departure_city, 
	   f.arrival_city,
       MAX(tf.amount), 
       MIN(tf.amount)
  FROM flights_v AS f
  LEFT JOIN ticket_flights AS tf 
    ON f.flight_id = tf.flight_id
 GROUP BY 1, 2
 ORDER BY 1, 2;

/*
14. Предположим, что маркетологи нашей авиакомпании хотят знать, как часто встречаются различные имена среди пассажиров? 
Получить распределение частот имен пассажиров в таблице «Билеты» (tickets) поможет такой запрос:

    SELECT left( passenger_name, strpos( passenger_name, ' ' ) - 1 )
           AS firstname, count( * )
      FROM tickets
      GROUP BY 1
      ORDER BY 2 DESC;
     firstname | count
    -----------+-------
     ALEKSANDR | 20328
     SERGEY    | 15133
     VLADIMIR  | 12806
TATYANA
ELENA
OLGA
...
MAGOMED
ASKAR
RASUL
| 12058
| 11291
|  9998
| 14
| 13
| 11
(363 строки)
Напишите запрос для ответа на аналогичный вопрос насчет распределения частот фамилий пассажиров.
Подробные сведения о других функциях для работы со строковыми данными приведены в документации в разделе 9.4 «Строковые функции и операторы».
*/

SELECT *
  FROM tickets;

SELECT *,
	   STRPOS(passenger_name, ' '),
	   STRPOS(passenger_name, ' ') - 1,
	   LEFT(passenger_name, STRPOS(passenger_name, ' ') - 1)  
  FROM tickets;
   

SELECT left( passenger_name, strpos( passenger_name, ' ' ) - 1 ) AS firstname, 
	   COUNT (*)
  FROM tickets
 GROUP BY 1
 ORDER BY 2 DESC;

SELECT RIGHT(passenger_name, LENGTH(passenger_name) - STRPOS(passenger_name, ' ')) AS "Surname",
	   COUNT(*) AS "Surname Counter"
  FROM tickets
 GROUP BY "Surname"
 ORDER BY "Surname Counter" DESC;

/*
15.* В тексте главы были кратко рассмотрены оконные функции. Самостоятельно прочитайте разделы документации, которые рекомендуется 
изучить для более детального ознакомления с этим классом функций.
Подумайте, в какой ситуации, связанной с базой данных «Авиаперевозки», было бы полезно применить оконные функции, и напишите запрос.
 */

/*
Оконные функции могут быть полезны для аналитических запросов, которые требуют вычисления агрегатных функций (например, суммы или среднего значения) 
для различных групп строк.

Для примера, предположим, что у нас есть таблица "Рейсы" с информацией о рейсах и тарифах авиакомпании. Мы хотим вычислить среднюю цену билета 
на каждый месяц года, а также для каждого месяца по годам. Мы можем использовать оконные функции для выполнения этой задачи:

sql
Copy
SELECT 
  EXTRACT(MONTH FROM flight_date) AS month, 
  EXTRACT(YEAR FROM flight_date) AS year, 
  AVG(fare) OVER (PARTITION BY EXTRACT(MONTH FROM flight_date)) AS avg_monthly_fare, 
  AVG(fare) OVER (PARTITION BY EXTRACT(MONTH FROM flight_date), EXTRACT(YEAR FROM flight_date)) AS avg_monthly_fare_by_year
FROM flights
В этом запросе мы используем функцию EXTRACT для извлечения месяца и года из даты полета. Затем мы используем оконную функцию AVG для вычисления 
среднего значения тарифа для каждого месяца (PARTITION BY EXTRACT(MONTH FROM flight_date)) и для каждого месяца в каждом году (PARTITION BY EXTRACT(MONTH FROM flight_date), 

Другой пример использования оконных функций в базе данных может быть связан с вычислением кумулятивных сумм или процентных долей. 
Например, мы можем использовать оконную функцию для вычисления доли каждого рейса в общей сумме доходов авиакомпании.
*/


/*
16.* ВместесагрегатнымифункциямиможетиспользоватьсяпредложениеFILTER. Самостоятельно ознакомьтесь с этой темой, обратившись к разделу 
документации 4.2.7 «Агрегатные выражения». Напишите запрос с использованием предложения FILTER с агрегатной функцией.
 */
 
/*
Предложение FILTER позволяет фильтровать строки, которые будут использоваться для вычисления агрегатной функции. Это полезно в ситуациях, когда требуется 
вычислить агрегатную функцию только для определенных строк.

Например, предположим, что у нас есть таблица "Заказы" с информацией о заказах и их стоимости. Мы хотим вычислить среднюю стоимость заказов, 
которые были выполнены в определенном регионе. Мы можем использовать предложение FILTER с агрегатной функцией AVG, чтобы выполнить эту задачу:

sql
Copy
SELECT 
  region, 
  AVG(order_cost) FILTER (WHERE region = 'Europe') AS avg_cost_in_europe
FROM orders
GROUP BY region
В этом запросе мы используем предложение FILTER для ограничения вычисления средней стоимости заказов только для региона "Europe". 
Это позволяет нам получить только нужную информацию вместо вычисления средней стоимости для всех регионов. Результатом запроса будет 
таблица с двумя столбцами: "region" и "avg_cost_in_europe".
*/

/*
17. В тексте главы в разделе 6.4 мы рассмотрели два способа получения ответа на вопрос: как распределяются места с разными классами обслуживания в самолетах всех типов?
А с помощью какого запроса можно получить результат в таком виде?
     aircraft_code |       model         | fare_conditions | count
    ---------------+---------------------+-----------------+-------
 319           | Airbus A319-100     | Business
 319           | Airbus A319-100     | Economy
...
 CR2           | Bombardier CRJ-200  | Economy
 SU9           | Sukhoi SuperJet-100 | Business
 SU9           | Sukhoi SuperJet-100 | Economy
(17 строк)
| 20 | 96
| 50 | 12 | 85
*/

SELECT a.aircraft_code,
       a.model,
       s.fare_conditions,
       COUNT(*)
  FROM aircrafts as a
  JOIN seats as s
    ON a.aircraft_code = s.aircraft_code
 GROUP BY a.aircraft_code, a.model, s.fare_conditions
 ORDER BY a.aircraft_code;
 

/*
18. В разделе 6.2 мы находили ответ на вопрос: сколько маршрутов обслуживают самолеты каждого типа? Но для повышения наглядности получаемых результатов 
необходимо еще рассчитывать относительные величины, т. е. доли от общего числа маршрутов.
Вот что требуется получить:
     a_code |         model       | r_code | num_routes | fraction
    --------+---------------------+--------+------------+----------
      CR2    | Bombardier CRJ-200  | CR2    |
      CN1    | Cessna 208 Caravan  | CN1    |
      ...
      773    | Boeing 777-300      | 773    |
      320    | Airbus A320-200     |        |
(9 строк)
*/

SELECT *
  FROM aircrafts;
 
SELECT *
  FROM routes;
 
 
SELECT r.aircraft_code AS "Aircraft Code",
	   a.model AS "Model",
	   COUNT(*) AS "A number of routes",
	   ROUND(COUNT(*)::DECIMAL / (SELECT COUNT(*) FROM routes), 3) AS "Fraction"
  FROM routes AS r
  JOIN aircrafts AS a
    ON r.aircraft_code = a.aircraft_code
 GROUP BY r.aircraft_code, a.model 
 ORDER BY "A number of routes" DESC;
    
SELECT ROUND(CAST(232 AS DECIMAL)/ 710, 3);
SELECT ROUND(232::DECIMAL / 710, 3);


  WITH total_routes AS (
SELECT COUNT(*) AS total_count
  FROM routes)
SELECT r.aircraft_code AS "Aircraft Code",
	   a.model AS "Model",
	   COUNT(*) AS "A number of routes",
	   ROUND((COUNT(*)::DECIMAL / (SELECT total_count FROM total_routes)), 3) AS "Fraction"
  FROM routes AS r
  JOIN aircrafts AS a
    ON r.aircraft_code = a.aircraft_code
 GROUP BY r.aircraft_code, a.model 
 ORDER BY "A number of routes" DESC;


/*
19.* В разделе 6.4 мы использовали рекурсивный алгоритм в общем табличном выражении. 
Изучите этот пример, чтобы лучше понять работу рекурсивного алгоритма:

    WITH RECURSIVE ranges ( min_sum, max_sum )
    AS (
         VALUES( 0,      100000 ),
               ( 100000, 200000 ),
               ( 200000, 300000 )
         UNION ALL
         SELECT min_sum + 100000, max_sum + 100000
           FROM ranges
           WHERE max_sum < ( SELECT max( total_amount ) FROM bookings )
   )
   
SELECT * FROM ranges;

 min_sum | max_sum
---------+---------
0| 100000 100000 | 200000 200000 | 300000
  100000 |  200000
  200000 |  300000
  300000 |  400000
  200000 |  300000
  300000 |  400000
  400000 |  500000
  300000 |  400000
  400000 |  500000
  500000 |  600000
  ...
 1000000 | 1100000
 1100000 | 1200000
 1200000 | 1300000
 1100000 | 1200000
 1200000 | 1300000
 1200000 | 1300000
(36 строк)
исходные строки
результат первой итерации
результат второй итерации
результат (n-3)-й итерации
результат (n-2)-й итерации
результат (n-1)-й итерации (предпоследней)

Здесь мы с помощью предложения VALUES специально создали виртуальную таблицу из трех строк, 
хотя для получения требуемого результата достаточно только одной строки (0, 100000). 

Еще важно то, что предложение UNION ALL не удаляет строки-дубликаты, поэтому мы можем видеть весь рекурсивный 
процесс порождения новых строк.

При рекурсивном выполнении запроса
SELECT min_sum + 100000, max_sum + 100000
  FROM ranges
  WHERE max_sum < ( SELECT max( total_amount ) FROM bookings )
каждый раз выполняется проверка в условии WHERE. И на (n − 2)-й итерации это условие отсеивает одну строку, 
т.к. после (n − 3)-й итерации значение атрибута max_sum в третьей строке было равно 1 300 000.

Ведь запрос
SELECT max( total_amount ) FROM bookings;
выдаст значение
    max
------------
 1204500.00
(1 строка)

Таким образом, после (n − 2)-й итерации во временной области остается всего две строки, после (n − 1)-й итерации 
во временной области остается только одна строка.

Заключительная итерация уже не добавляет строк в результирующую таблицу, поскольку единственная строка, поданная 
на вход команде SELECT, будет отклонена условием WHERE. Работа алгоритма завершается.

Задание 1. Модифицируйте запрос, добавив в него столбец level (можно назвать его и iteration). Этот столбец должен 
содержать номер текущей итерации, поэтому нужно увеличивать его значение на единицу на каждом шаге. Не забудьте задать 
начальное значение для добавленного столбца в предложении VALUES.

Задание 2. Для завершения экспериментов замените UNION ALL на UNION и выполните запрос. Сравните этот результат с 
предыдущим, когда мы использовали UNION ALL.
*/

  WITH RECURSIVE ranges (min_sum, max_sum) AS (
VALUES (0, 100000),
       (100000, 200000),
       (200000, 300000)
       
 UNION ALL
 
SELECT min_sum + 100000, max_sum + 100000
  FROM ranges
 WHERE max_sum < (SELECT MAX(total_amount) FROM bookings))
 
SELECT * FROM ranges;

  WITH RECURSIVE ranges (min_sum, max_sum) AS 
(VALUES (0, 100000),
       (100000, 200000),
       (200000, 300000))
SELECT *
  FROM ranges
       
  WITH ranges (min_sum, max_sum) AS 
(VALUES (0, 100000),
       (100000, 200000),
       (200000, 300000))
SELECT *
  FROM ranges
  
   WITH ranges AS 
(VALUES (0, 100000),
       (100000, 200000),
       (200000, 300000))
SELECT *
  FROM ranges 
  
-- 1 
  WITH ranges AS (
VALUES (0, 100000),
       (100000, 200000),
       (200000, 300000))
SELECT *
  FROM ranges; 

-- 2 
  WITH ranges(min_sum, max_sum) AS (
VALUES (0, 100000),
       (100000, 200000),
       (200000, 300000))
SELECT *
  FROM ranges;  
  
-- 3
 
   WITH RECURSIVE ranges(min_sum, max_sum) AS (
VALUES (0, 100000),
       (100000, 200000),
       (200000, 300000))
SELECT *
  FROM ranges;  
 
-- 4
 
   WITH RECURSIVE ranges(min_sum, max_sum) AS (
VALUES (0, 100000),
       (100000, 200000),
       (200000, 300000)
       
 UNION ALL     

SELECT min_sum + 100000, max_sum + 100000
  FROM ranges
 WHERE max_sum < (SELECT MAX(total_amount) FROM bookings)) 

SELECT *
  FROM ranges;  

 -- Ex. 1

WITH RECURSIVE ranges ( level, min_sum, max_sum )
AS (
     VALUES( 1, 0, 100000 ),
           ( 1, 100000, 200000 ),
           ( 1, 200000, 300000 )
     UNION ALL
     SELECT level + 1, min_sum + 100000, max_sum + 100000
       FROM ranges
       WHERE max_sum < ( SELECT max( total_amount ) FROM bookings )
)
   
SELECT * FROM ranges; 
 
-- Ex. 2

   WITH RECURSIVE ranges(min_sum, max_sum) AS (
VALUES (0, 100000),
       (100000, 200000),
       (200000, 300000)
       
 UNION     

SELECT min_sum + 100000, max_sum + 100000
  FROM ranges
 WHERE max_sum < (SELECT MAX(total_amount) FROM bookings)) 

SELECT *
  FROM ranges;  

/*
20.* В тексте главы есть такой запрос, вычисляющий распределение сумм бронирований по диапазонам в 100 тысяч рублей:
    WITH RECURSIVE ranges ( min_sum, max_sum )
    AS (
         VALUES( 0, 100000 )
         UNION ALL
         SELECT min_sum + 100000, max_sum + 100000
FROM ranges
           WHERE max_sum < ( SELECT max( total_amount ) FROM bookings )
       )
    SELECT r.min_sum,
           r.max_sum,
           count( b.* )
      FROM bookings b
      RIGHT OUTER JOIN ranges r
        ON  b.total_amount >= r.min_sum
        AND b.total_amount <  r.max_sum
      GROUP BY r.min_sum, r.max_sum
      ORDER BY r.min_sum;
Как вы думаете, почему функция count получает в качестве параметра выражение b.*, а не просто *? Что изменится, если оставить только *, и почему?
 */ 
/*
Функция count получает в качестве параметра выражение "b.", потому что она должна подсчитывать количество строк, 
содержащих данные в таблице "bookings", которые соответствуют определенному диапазону сумм бронирований из таблицы "ranges". 
Если использовать просто "", то будут учитываться все столбцы таблицы "bookings", что может привести к неверным результатам подсчета.

Если заменить "b." на "", то запрос все еще будет работать, но в результате будут учитываться все столбцы таблицы "bookings", 
что может привести к ненужному расходу ресурсов, если необходимо подсчитать только количество строк. Кроме того, если в 
таблице "bookings" есть много столбцов, то использование "*" может затруднить чтение и понимание запроса.

В целом, использование "b.*" является более предпочтительным, поскольку позволяет уточнить, что именно нужно учитывать в 
подсчете количества строк, и избежать ненужных затрат ресурсов.
 */ 
 
 
/*
21. В тексте главы был приведен запрос, выводящий список городов, в которые нет рейсов из Москвы.
    SELECT DISTINCT a.city
      FROM airports a
      WHERE NOT EXISTS (
        SELECT * FROM routes r
          WHERE r.departure_city = 'Москва'
            AND r.arrival_city = a.city
        )
        AND a.city <> 'Москва'
      ORDER BY city;
Можно предложить другой вариант, в котором используется одна из операций над множествами строк: объединение, пересечение или разность.
Вместо знака «?» поставьте в приведенном ниже запросе нужное ключевое слово — UNION, INTERSECT или EXCEPT — и обоснуйте ваше решение.

    SELECT city
      FROM airports
      WHERE city <> 'Москва'
    ?
    SELECT arrival_city
FROM routes
      WHERE departure_city = 'Москва'
    ORDER BY city;
*/ 
 
 SELECT DISTINCT a.city
   FROM airports a
  WHERE NOT EXISTS (
 SELECT * FROM routes r
  WHERE r.departure_city = 'Москва'
    AND r.arrival_city = a.city
        )
    AND a.city <> 'Москва'
  ORDER BY city; 
 

SELECT city
  FROM airports
 WHERE city <> 'Москва'
EXCEPT
SELECT arrival_city
  FROM routes
 WHERE departure_city = 'Москва'
 ORDER BY city; 
 
/*
22. В тексте главы мы рассматривали такой запрос: получить перечень аэропортов в тех городах, в которых больше одного аэропорта.
    SELECT aa.city, aa.airport_code, aa.airport_name
      FROM (
        SELECT city, count( * )
          FROM airports
          GROUP BY city
          HAVING count( * ) > 1
        ) AS a
      JOIN airports AS aa ON a.city = aa.city
      ORDER BY aa.city, aa.airport_name;
Как вы думаете, обязательно ли наличие функции count в подзапросе в пред- ложении SELECT или можно написать просто
    SELECT city FROM airports
Сначала попробуйте дать ответ теоретически, а потом проверьте вашу гипотезу на компьютере.
*/

SELECT aa.city, 
	   aa.airport_code, 
	   aa.airport_name
 FROM (SELECT city, count( * )
         FROM airports
        GROUP BY city
       HAVING count( * ) > 1) AS a
 JOIN airports AS aa 
   ON a.city = aa.city
ORDER BY aa.city, aa.airport_name;


SELECT aa.city, 
	   aa.airport_code, 
	   aa.airport_name
 FROM (SELECT city--, count( * )
         FROM airports
        GROUP BY city
       HAVING count( * ) > 1) AS a
 JOIN airports AS aa 
   ON a.city = aa.city
ORDER BY aa.city, aa.airport_name;

/*
23. Предположим, что департамент развития нашей авиакомпании задался вопросом: каким будет общее число 
различных маршрутов, которые теоретически можно проложить между всеми городами?

Если в каком-то городе имеется более одного аэропорта, то это учитывать не будем, т.е. маршрутом будем 
считать путь между городами, а не между аэропортами. Здесь мы используем соединение таблицы с самой собой на основе неравенства значений атрибутов.
    SELECT count( * )
      FROM ( SELECT DISTINCT city FROM airports ) AS a1
      JOIN ( SELECT DISTINCT city FROM airports ) AS a2
ON a1.city <> a2.city;
count
    -------
     10100
(1 строка)
Задание. Перепишите этот запрос с общим табличным выражением.
*/
-- 1
SELECT COUNT(*)
  FROM (SELECT DISTINCT city 
  	      FROM airports) AS a1
  JOIN (SELECT DISTINCT city 
  		  FROM airports) AS a2
	ON a1.city <> a2.city;

-- 2	 
  WITH a1 AS (SELECT DISTINCT city 
  				FROM airports),
  	   a2 AS (SELECT DISTINCT city
  	   		    FROM airports)
SELECT COUNT(*) 
  FROM a1
  JOIN a2
    ON a1.city != a2.city;
    
/* 
24. В тексте главы мы рассмотрели использование подзапросов в предикатах EXISTS и IN. Существуют также предикаты многократного сравнения ANY и ALL. Они представлены в документации в разделе 9.22 «Выражения подзапро- сов». Самостоятельно ознакомьтесь с этими предикатами и напишите несколь- ко запросов с их применением.
Предикаты ANY и ALL имеют некоторую связь с предикатом IN. В частности, использование IN эквивалентно использованию конструкции = ANY, а исполь- зование NOT IN эквивалентно использованию конструкции <> ALL.
Пример двух эквивалентных запросов, выбирающих аэропорты в часовых поя- сах Asia/Novokuznetsk и Asia/Krasnoyarsk:
    SELECT * FROM airports
      WHERE timezone IN ( 'Asia/Novokuznetsk', 'Asia/Krasnoyarsk' );
    SELECT * FROM airports
      WHERE timezone = ANY (
        VALUES ( 'Asia/Novokuznetsk' ), ( 'Asia/Krasnoyarsk' )
      );
Еще один пример. В тексте главы мы рассматривали запрос, подсчитывающий количество маршрутов, проложенных из самых восточных аэропортов.
SELECT departure_city, count( * )
  FROM routes
  GROUP BY departure_city
  HAVING departure_city IN (
    SELECT city
      FROM airports
      WHERE longitude > 150
  )
  ORDER BY count DESC;
В этом запросе можно заменить IN на ANY таким образом: HAVING departure_city = ANY ( ... )
 */   
   
SELECT * FROM airports
      WHERE timezone IN ( 'Asia/Novokuznetsk', 'Asia/Krasnoyarsk' );
    SELECT * FROM airports
      WHERE timezone = ANY (
        VALUES ( 'Asia/Novokuznetsk' ), ( 'Asia/Krasnoyarsk' )
      );
      
 SELECT departure_city, count( * )
  FROM routes
  GROUP BY departure_city
  HAVING departure_city IN (
    SELECT city
      FROM airports
      WHERE longitude > 150
  )
  ORDER BY count DESC;    
  
 
/*25.* При планировании новых маршрутов и оценке экономической эффективности уже 
 существующих может потребоваться информация о том, какова усредненная степень 
 заполнения самолетов на всех направлениях.
Будем учитывать только уже прибывшие рейсы.
    WITH tickets_seats
    AS (
         SELECT f.flight_id,
                f.flight_no,
                f.departure_city,
                f.arrival_city,
                f.aircraft_code,
                count( tf.ticket_no ) AS fact_passengers,
                ( SELECT count( s.seat_no )
FROM seats s
                    WHERE s.aircraft_code = f.aircraft_code
                ) AS total_seats
           FROM flights_v f
           JOIN ticket_flights tf ON f.flight_id = tf.flight_id
           WHERE f.status = 'Arrived'
           GROUP BY 1, 2, 3, 4, 5
       )
    SELECT ts.departure_city,
           ts.arrival_city,
           sum( ts.fact_passengers ) AS sum_pass,
           sum( ts.total_seats ) AS sum_seats,
           round( sum( ts.fact_passengers )::numeric /
                  sum( ts.total_seats )::numeric, 2 ) AS frac
      FROM tickets_seats ts
      GROUP BY ts.departure_city, ts.arrival_city
      ORDER BY ts.departure_city;
      
     departure_city |  arrival_city   | sum_pass | sum_seats | frac
    ----------------+-----------------+----------+-----------+------
206
 Абакан
 Абакан
 Абакан
 ...
 Якутск
(361 строка)
| Tomsk
| Novosibirsk
| Moscow
| Санкт-Петербург
| 258| | 217| | 466|
| 352|
360 | 0.72
      348 | 0.62
     1044 | 0.45
3596 | 0.10

Для того чтобы лучше уяснить, как работает запрос,  в целом, вычлените из него что они выводят.
Для того чтобы лучше уяснить, как работает запрос в отдельные подзапросы и выполните их, посмотрите,

Как вы считаете, равносильно ли в данном запросе
    SELECT count( s.seat_no )
и
    SELECT count( s.* )
Почему?
Задание. Модифицируйте этот запрос, чтобы он выводил те же отчетные дан-
ные, но с учетом классов обслуживания, т. е. Business, Comfort и Economy.
*/
 
-- Указанные SELECT вернут одно и то же.
 
    WITH tickets_seats
    AS (
         SELECT f.flight_id,
                f.flight_no,
                f.departure_city,
                f.arrival_city,
                f.aircraft_code,
                count( tf.ticket_no ) AS fact_passengers,
                ( SELECT count( s.seat_no )
FROM seats s
                    WHERE s.aircraft_code = f.aircraft_code
                ) AS total_seats
           FROM flights_v f
           JOIN ticket_flights tf ON f.flight_id = tf.flight_id
           WHERE f.status = 'Arrived'
           GROUP BY 1, 2, 3, 4, 5
       )
    SELECT ts.departure_city,
           ts.arrival_city,
           sum( ts.fact_passengers ) AS sum_pass,
           sum( ts.total_seats ) AS sum_seats,
           round( sum( ts.fact_passengers )::numeric /
                  sum( ts.total_seats )::numeric, 2 ) AS frac
      FROM tickets_seats ts
      GROUP BY ts.departure_city, ts.arrival_city
      ORDER BY ts.departure_city;
     

WITH tickets_seats
AS (
    SELECT f.flight_id,
           f.flight_no,
           f.departure_city,
           f.arrival_city,
           f.aircraft_code,
           tf.fare_conditions,
           count(tf.ticket_no) AS fact_passengers,
           ( SELECT count(s.seat_no)
             FROM seats s
             WHERE s.aircraft_code = f.aircraft_code
           ) AS total_seats
    FROM flights_v f
    JOIN ticket_flights tf 
      ON f.flight_id = tf.flight_id
    WHERE f.status = 'Arrived'
    GROUP BY 1, 2, 3, 4, 5, 6
)
SELECT ts.departure_city,
       ts.arrival_city,
       ts.fare_conditions,
       sum(ts.fact_passengers) AS sum_pass,
       sum(ts.total_seats) AS sum_seats,
       round(sum(ts.fact_passengers)::numeric / sum(ts.total_seats)::numeric, 2) AS frac
FROM tickets_seats ts
GROUP BY ts.departure_city, ts.arrival_city, ts.fare_conditions
ORDER BY ts.departure_city;


/* 
26.* Предположим,чтонекаяконтролирующаяорганизацияпотребовалаинформацию о размещении 
пассажиров одного из рейсов Кемерово — Москва в салоне самолета. Для определенности 
выберем конкретный рейс из тех рейсов, кото- рые уже прибыли на момент времени, 
соответствующий текущему моменту. Текущий момент времени в базе данных «Авиаперевозки» 
определяется с помощью функции bookings.now.

Выполним запрос:
    SELECT *
      FROM flights_v
      WHERE departure_city = 'Кемерово'
        AND arrival_city = 'Москва'
        AND actual_arrival < bookings.now();
        
Выберем для дальнейшей работы рейс, у которого значения атрибутов flight_id — 27584, aircraft_code — SU9.
Получим список пассажиров этого рейса с местами, которые им были назначе- ны в салоне самолета.

SELECT t.passenger_name, b.seat_no
  FROM (
    ticket_flights tf
    JOIN tickets t ON tf.ticket_no = t.ticket_no
  )
  JOIN boarding_passes b
    ON  tf.ticket_no = b.ticket_no
    AND tf.flight_id = b.flight_id
  WHERE tf.flight_id = 27584
  ORDER BY t.passenger_name;
  
 passenger_name      | seat_no
---------------------+---------
 ALEKSANDR ABRAMOV   | 1A
 ALEKSANDR GRIGOREV  | 5C
 ALEKSANDR SERGEEV
 ALEKSEY FEDOROV
 ALEKSEY MELNIKOV
...
 VLADIMIR POPOV
 YAROSLAV KUZMIN
 YURIY ZAKHAROV
(44 строки)
|6F | 11D | 18A
| 11A
| 18F
| 10F

Отсортируем строки по фамилиям пассажиров:
SELECT t.passenger_name,

    substr(   t.passenger_name,
      strpos( t.passenger_name, ' ' ) + 1
    ) AS lastname,
    left(     t.passenger_name,
      strpos( t.passenger_name, ' ' ) - 1
    ) AS firstname,
    b.seat_no
  FROM (
    ticket_flights tf
    JOIN tickets t ON tf.ticket_no = t.ticket_no
  )
  JOIN boarding_passes b
    ON  tf.ticket_no = b.ticket_no
    AND tf.flight_id = b.flight_id
  WHERE tf.flight_id = 27584
  ORDER BY 2, 3;
  
    passenger_name   | lastname  | firstname | seat_no
---------------------+-----------+-----------+---------
 ALEKSANDR ABRAMOV   | ABRAMOV   | ALEKSANDR | 1A
 NIKITA ANDREEV      | ANDREEV   | NIKITA    | 6D
 ANTONINA ANISIMOVA  | ANISIMOVA | ANTONINA  | 11F
 ...
 YURIY ZAKHAROV      | ZAKHAROV  | YURIY     | 10F
 ELENA ZOTOVA        | ZOTOVA    | ELENA     | 20E
(44 строки)

Получим список мест в салоне самолета и пассажиров, которые сидели на этих местах. 
При этом незанятые места также должны быть выведены (поэтому ис- пользуем левое внешнее 
соединение LEFT OUTER JOIN).

SELECT s.seat_no, p.passenger_name
  FROM seats s
  LEFT OUTER JOIN (
    SELECT t.passenger_name, b.seat_no
      FROM (
        ticket_flights tf
        JOIN tickets t ON tf.ticket_no = t.ticket_no
      )
      JOIN boarding_passes b
        ON  tf.ticket_no = b.ticket_no
        AND tf.flight_id = b.flight_id
      WHERE tf.flight_id = 27584
  ) AS p
     ON s.seat_no = p.seat_no
  WHERE s.aircraft_code = 'SU9'
  ORDER BY s.seat_no;
  
 seat_no | passenger_name
---------+---------------------
10A | 10C |
 10D     | NATALYA POPOVA
10E |
 10F     | YURIY ZAKHAROV
 11A     | VLADIMIR POPOV
 11C     | ANNA KUZMINA
 ...
 8F      |
 9A      | MAKSIM CHERNOV
 9C      |
 9D      | LYUDMILA IVANOVA
 9E      |
 9F      | SOFIYA KULIKOVA
(97 строк)

Предположим, что нас попросили отсортировать места в порядке их расположения 
в салоне самолета и вывести также адреса электронной почты пассажиров (у кого они были указаны при бронировании). 
Для выполнения второго требова- ния воспользуемся столбцом contact_data. 
В нем содержатся JSON-объекты,  
содержащие контактные данные пассажиров. Ряд из них имеет ключ email. Модифицированный запрос будет таким:

SELECT s.seat_no, p.passenger_name, p.email
  FROM seats s
  LEFT OUTER JOIN (
    SELECT t.passenger_name, b.seat_no,
           t.contact_data->'email' AS email
      FROM (
        ticket_flights tf
        JOIN tickets t ON tf.ticket_no = t.ticket_no
      )
      JOIN boarding_passes b
        ON  tf.ticket_no = b.ticket_no
        AND tf.flight_id = b.flight_id
      WHERE tf.flight_id = 27584
  ) AS p
     ON s.seat_no = p.seat_no
  WHERE s.aircraft_code = 'SU9'
  ORDER BY
    left( s.seat_no, length( s.seat_no ) - 1 )::integer,
    right( s.seat_no, 1 );
    
 seat_no |   passenger_name  | email
---------+-------------------+------------------------------------
 1A      | ALEKSANDR ABRAMOV |
1C|
1D| DENIS PETROV |
1F| LEONID BARANOV 2A|
2C|
...
9F| SOFIYA KULIKOVA 10A|
10C|
10D | NATALYA POPOVA ...
|
| "baranov.l.1967@postgrespro.ru"
|
|
| "sofiya.kulikova_041963@postgre..."
|
|
| "popova.n_13031976@postgrespro.ru"
 20E     | ELENA ZOTOVA      |
 20F     | LILIYA OSIPOVA    |
(97 строк)

Задание. Перепишите последний запрос с использованием общего табличного выражения и 
добавьте столбец «Класс обслуживания» (fare_conditions).
 */ 

SELECT s.seat_no, p.passenger_name, p.email
  FROM seats s
  LEFT OUTER JOIN (
    SELECT t.passenger_name, b.seat_no,
           t.contact_data->'email' AS email
      FROM (
        ticket_flights tf
        JOIN tickets t ON tf.ticket_no = t.ticket_no
      )
      JOIN boarding_passes b
        ON  tf.ticket_no = b.ticket_no
        AND tf.flight_id = b.flight_id
      WHERE tf.flight_id = 27584
  ) AS p
     ON s.seat_no = p.seat_no
  WHERE s.aircraft_code = 'SU9'
  ORDER BY
    left( s.seat_no, length( s.seat_no ) - 1 )::integer,
    right( s.seat_no, 1 );
   
 -- 2   
 WITH p AS (
    SELECT 
        t.passenger_name, 
        b.seat_no,
        tf.fare_conditions,
        t.contact_data->'email' AS email
    FROM 
        ticket_flights tf
        JOIN tickets t ON tf.ticket_no = t.ticket_no
        JOIN boarding_passes b ON tf.ticket_no = b.ticket_no AND tf.flight_id = b.flight_id
    WHERE 
        tf.flight_id = 27584
)

SELECT 
    s.seat_no, 
    p.passenger_name, 
    p.fare_conditions,
    p.email
FROM 
    seats s
LEFT OUTER JOIN 
    p ON s.seat_no = p.seat_no
WHERE 
    s.aircraft_code = 'SU9'
ORDER BY 
    left(s.seat_no, length(s.seat_no) - 1)::integer,
    right(s.seat_no, 1);
  