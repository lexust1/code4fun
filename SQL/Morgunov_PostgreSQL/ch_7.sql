DROP TABLE IF EXISTS aircrafts_tmp, aircrafts_log;

CREATE TEMP TABLE aircrafts_tmp AS
SELECT * FROM aircrafts WITH NO DATA;

SELECT * 
  FROM aircrafts_tmp;
  
ALTER TABLE aircrafts_tmp
  ADD PRIMARY KEY (aircraft_code);
  
ALTER TABLE aircrafts_tmp
  ADD UNIQUE (model);
  
CREATE TEMP TABLE aircrafts_log AS
SELECT * FROM aircrafts WITH NO DATA;

 ALTER TABLE aircrafts_log
   ADD COLUMN when_add TIMESTAMP;
  
 ALTER TABLE aircrafts_log
   ADD COLUMN operation TEXT;

SELECT *
  FROM aircrafts_log;
  
 
/*
1. Добавьте в определение таблицы aircrafts_log значение по умолчанию current_timestamp и соответствующим 
образом измените команды INSERT, приведенные в тексте главы. 
*/
 
CREATE TEMP TABLE aircrafts_tmp AS
SELECT * FROM aircrafts WITH NO DATA;

SELECT * 
  FROM aircrafts_tmp;
  
ALTER TABLE aircrafts_tmp
  ADD PRIMARY KEY (aircraft_code);
  
ALTER TABLE aircrafts_tmp
  ADD UNIQUE (model);
  
CREATE TEMP TABLE aircrafts_log AS
SELECT * FROM aircrafts WITH NO DATA;

 ALTER TABLE aircrafts_log
   ADD COLUMN when_add TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
  
 ALTER TABLE aircrafts_log
   ADD COLUMN operation TEXT;

SELECT *
  FROM aircrafts_log;
  

/*
2. В предложении RETURNING можно указывать не только символ «∗», означающий выбор всех столбцов таблицы, 
но и более сложные выражения, сформированные на основе этих столбцов. 
В тексте главы мы копировали содержимое таблицы «Самолеты» в таблицу aircrafts_tmp, используя в предложении
 RETURNING именно «∗». Однако возможен и другой вариант запроса:
  
     WITH add_row AS
     ( INSERT INTO aircrafts_tmp
         SELECT * FROM aircrafts
         RETURNING aircraft_code, model, range,
                   current_timestamp, 'INSERT'
     )
     INSERT INTO aircrafts_log
       SELECT ? FROM add_row;
Что нужно написать в этом запросе вместо вопросительного знака?
 */
     WITH add_row AS
     ( INSERT INTO aircrafts_tmp
         SELECT * FROM aircrafts
         RETURNING aircraft_code, model, range,
                   current_timestamp, 'INSERT'
     )
     SELECT * FROM add_row;
     
  /*
  3. Если бы мы для копирования данных в таблицу aircrafts_tmp использовали команду INSERT без 
  общего табличного выражения 
  INSERT INTO aircrafts_tmp SELECT * FROM aircrafts;
то в качестве выходного результата мы увидели бы сообщение

INSERT 0 9

Как вы думаете, что будет выведено, если дополнить команду предложением RETURNING *?
   INSERT INTO aircrafts_tmp SELECT * FROM aircrafts RETURNING *;
Проверьте ваши предположения на практике. 
Подумайте, каким образом можно использовать выведенный результат?
   */  
    
INSERT INTO aircrafts_tmp SELECT * FROM aircrafts RETURNING *;

/*
4. В тексте главы в предложениях ON CONFLICT команды INSERT мы использовали только выражения, 
состоящие из имени одного столбца. Однако в таблице «Места» (seats) первичный ключ является 
составным и включает два столбца.
Напишите команду INSERT для вставки новой строки в эту таблицу и предусмотрите возможный конфликт
добавляемой строки со строкой, уже имеющеися в таблице. 
 
Сделайте два варианта предложения ON CONFLICT: 
первый — с использованием перечисления имен столбцов для проверки наличия дублирования, 
второй — с использованием предложения ON CONSTRAINT.
Для того чтобы не изменить содержимое таблицы «Места», создайте ее копию и выполняйте все эти 
эксперименты с таблицей-копией.
*/
SELECT * FROM seats;

CREATE TABLE seats_copy AS 
SELECT * FROM seats;

ALTER TABLE seats_copy
ADD PRIMARY KEY (aircraft_code, seat_no);

SELECT * FROM seats_copy;

INSERT INTO seats_copy (aircraft_code, seat_no, fare_conditions)
VALUES ('319', '4A', 'Business')
ON CONFLICT (aircraft_code, seat_no)
DO NOTHING;

INSERT INTO seats_copy (aircraft_code, seat_no, fare_conditions)
VALUES ('319', '6C', 'Economy')
ON CONFLICT (aircraft_code, seat_no) 
DO NOTHING; -- Или DO UPDATE SET fare_conditions = EXCLUDED.fare_conditions;

INSERT INTO seats_copy (aircraft_code, seat_no, fare_conditions)
VALUES ('319', '6C', 'Economy')
ON CONFLICT ON CONSTRAINT seats_copy_pkey
DO NOTHING; -- Или DO UPDATE SET fare_conditions = EXCLUDED.fare_conditions;



/*
5. В предложении DO UPDATE команды INSERT может использоваться и условие WHERE. 
Самостоятельно ознакомьтесь с этой возможностью с помощью документации и напишите 
такую команду INSERT.
 */
INSERT INTO seats_copy (aircraft_code, seat_no, fare_conditions)
VALUES ('319', '6C', 'Economy')
ON CONFLICT (aircraft_code, seat_no)
DO UPDATE SET fare_conditions = EXCLUDED.fare_conditions
WHERE seats_copy.fare_conditions <> EXCLUDED.fare_conditions;


/*
6. Команда COPY по умолчанию ожидает получения вводимых данных в формате text, 
когда значения данных разделяются символами табуляции. Однако можно представлять 
входные данные в формате CSV (Comma Separated Values), т. е. использовать в качестве 
разделителя запятую.
   COPY aircrafts_tmp FROM STDIN WITH ( FORMAT csv );
   Вводите данные для копирования, разделяя строки переводом строки.
   Закончите ввод строкой '\.'.
   
 IL9, Ilyushin IL96, 9800
 I93, Ilyushin IL96-300, 9800
 \.
 
COPY 2
     SELECT * FROM aircrafts_tmp;
      aircraft_code |        model        | range
     ---------------+---------------------+-------
      ...
      CN1           | Cessna 208 Caravan  |  1200
      CR2           | Bombardier CRJ-200  |  2700
      IL9           |  Ilyushin IL96      |  9800
      I93           |  Ilyushin IL96-300  |  9800
(11 строк)
Как вы думаете, почему при выводе данных из таблицы вновь введенные зна- чения в столбце model оказались смещены вправо?

*/

/*
Команда COPY позволяет получить входные данные из файла и поместить их в таблицу. 
Этот файл должен быть доступен тому пользователю операционной системы, от 
имени которого запущен серверный процесс, как правило, это пользователь postgres.

Подготовьте файл, например, /home/postgres/aircrafts_tmp.csv, имеющий такую структуру:
– каждая строка файла соответствует одной строке таблицы aircrafts_tmp;
– значения данных в строке файла разделяются запятыми. Например:
     773,Boeing 777-300,11100
     763,Boeing 767-300,7900
     SU9,Sukhoi SuperJet-100,3000
Введите в этот файл данные о нескольких самолетах, причем часть из них уже должна 
быть представлена в таблице, а часть — нет.

Поскольку при выполнении команды COPY проверяются все ограничения целостности, 
наложенные на таблицу, то дублирующие строки добавлены, конеч- но же, не будут. 
А как вы думаете, строки, содержащиеся в этом же файле, но отсутствующие в таблице, 
будут добавлены или нет?

Проверьте свою гипотезу, выполнив вставку строк в таблицу из этого файла:
   COPY aircrafts_tmp
     FROM '/home/postgres/aircrafts_tmp.csv' WITH ( FORMAT csv );

 */


