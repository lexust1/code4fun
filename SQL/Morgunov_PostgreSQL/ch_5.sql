CREATE TABLE students(
	PRIMARY KEY (record_book),
	record_book NUMERIC(5) NOT NULL,
	name 		TEXT       NOT NULL,
	doc_ser     NUMERIC(4),
	doc_num 	NUMERIC(6)
);

CREATE TABLE progress(
	record_book NUMERIC(5) NOT NULL,
	subject 	TEXT	   NOT NULL,
	acad_year   TEXT	   NOT NULL,
	term 		NUMERIC(1) NOT NULL,
			    CHECK(term = 1 OR term = 2),
	mark		NUMERIC(1) NOT NULL
			    CHECK(mark >= 3 AND MARK <= 5)
			    DEFAULT  5,
	FOREIGN KEY (record_book)
	REFERENCES students (record_book)
	ON DELETE CASCADE
	ON UPDATE CASCADE
);

DROP TABLE progress;

--


SELECT *
  FROM airports
 --LIMIT 10; 
  
  
SHOW search_path;
-- SET search_path = bookings;
-- SET search_path = bookings, public;



/*
 1. При использовании значений по умолчанию с ключевым словом DEFAULT возможны и ситуации, когда типичным 
 будет не конкретное значение данных, а способ его получения. Например, если мы захотим фиксировать в каждой строке 
 таблицы «Студенты» имя пользователя базы данных, добавившего эту строку в таблицу, тогда необходимо в определение 
 таблицы добавить еще один столбец. 
 
 Этот столбец по умолчанию будет получать значение, возвращаемое функцией current_user.
     CREATE TABLE students
     (  record_book numeric( 5 ) NOT NULL,
        name text NOT NULL,
        doc_ser numeric( 4 ),
        doc_num numeric( 6 ),
        who_adds_row text DEFAULT current_user, -- добавленный столбец
        PRIMARY KEY ( record_book )
);
Эта функция — current_user — будет вызываться не при создании таблицы, а при вставке каждой строки. При этом в команде 
INSERT не требуется указывать значение для столбца who_adds_row, поскольку функция current_user будет вызываться самой 
СУБД PostgreSQL:

     INSERT INTO students ( record_book, name, doc_ser, doc_num )
       VALUES ( 12300, 'Иванов Иван Иванович', 0402, 543281 );
       
Давайте пойдем дальше и пожелаем фиксировать не только имя пользователя базы данных, добавившего строку в таблицу, 
но также и момент времени, когда это было сделано. 

Самостоятельно внесите модификацию в определение таблицы students для решения этой задачи, а затем выполните команду 
INSERT для проверки полученного решения.

Если до выполнения этого упражнения вы еще не ознакомились с командой ALTER TABLE, то вместо модифицирования определения 
таблицы сначала удалите ее, а затем создайте заново:

     DROP TABLE students;
     CREATE TABLE students ...
*/

CREATE TABLE students (
	PRIMARY KEY (record_book),
	record_book  numeric(5) NOT NULL,
	name 	     text	    NOT NULL,
	doc_ser      numeric(4) NOT NULL,
	doc_num	     numeric(6) NOT NULL,
	who_adds_row text       DEFAULT CURRENT_USER
);

INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12300, 'Иванов Иван Иванович', 0402, 543281);

SELECT *
  FROM students;
 
ALTER TABLE students
  ADD COLUMN when_add_row TIMESTAMP
  						  DEFAULT CURRENT_TIMESTAMP;
 
DROP TABLE students;


CREATE TABLE students (
	PRIMARY KEY (record_book),
	record_book  NUMERIC(5) NOT NULL,
	name 	     TEXT	    NOT NULL,
	doc_ser 	 NUMERIC(4) NOT NULL,
	doc_num 	 NUMERIC(6) NOT NULL,
	who_adds_row TEXT 	    NOT NULL
				 DEFAULT CURRENT_USER,
	when_add_row TIMESTAMP  NOT NULL  
		         DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12300, 'Иванов Иван Иванович', 0402, 543281);

SELECT *
  FROM students;

 
/*
2. Посмотрите, какие ограничения уже наложены на атрибуты таблицы «Успеваемость» (progress). Воспользуйтесь командой \d утилиты psql. 
А теперь предложите для этой таблицы ограничение уровня таблицы.
В качестве примера рассмотрим такой вариант. Добавьте в таблицу progress еще один атрибут — «Форма проверки знаний» (test_form), который может принимать 
только два значения: «экзамен» или «зачет». 
Тогда набор допустимых значений атрибута «Оценка» (mark) будет зависеть от того, экзамен или зачет предусмотрены по данной дисциплине. 
Если предусмотрен экзамен, тогда допускаются значения 3, 4, 5, если зачет — тогда 0 (не зачтено) или 1 (зачтено).

Не забудьте, что значения NULL для атрибутов test_form и mark не допускаются.
Новое ограничение может быть таким:
   ALTER TABLE progress
     ADD CHECK (
       ( test_form = 'экзамен' AND mark IN ( 3, 4, 5 ) )
       OR
       ( test_form = 'зачет' AND mark IN ( 0, 1 ) )
);
Проверьте, как будет работать новое ограничение в модифицированной таблице progress. Для этого выполните команды INSERT, как удовлетворяющие ограничению, 
так и нарушающие его.

В таблице уже было ограничение на допустимые значения атрибута mark. Как вы думаете, не будет ли оно конфликтовать с новым ограничением? Проверьте эту гипотезу. 
Если ограничения конфликтуют, тогда удалите старое ограничение и снова попробуйте добавить строки в таблицу.
Подумайте, какое еще ограничение уровня таблицы можно предложить для этой таблицы?
*/ 
 
SELECT * 
  FROM progress;

ALTER TABLE progress
  ADD COLUMN test_form TEXT NOT NULL
  					   CHECK (test_form = 'экзамен' OR test_form = 'зачет');
  					   
ALTER TABLE progress
  ADD CHECK (
      (test_form = 'экзамен' AND mark IN (3, 4, 5))
      OR
      (test_form = 'зачет' AND mark IN (0, 1))
  );
  
 
INSERT INTO progress (record_book, subject, acad_year, term, mark, test_form)
VALUES (12300, 'Physics', '3', '2', '1', 'зачет');

ALTER TABLE progress
 DROP CONSTRAINT progress_mark_check;

INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12301, 'Петров Петр Петрович', 0402, 543282);

INSERT INTO progress (record_book, subject, acad_year, term, mark, test_form)
VALUES (12300, 'Physics', '3', '2', '3', 'экзамен');
 
/*
3.* В определении таблицы «Успеваемость» (progress) на атрибуты term и mark наложены как ограничения CHECK, так и ограничение NOT NULL. Возникает вопрос: 
не является ли ограничение NOT NULL избыточным? Ведь в ограничении CHECK явно указаны допустимые значения.
Проверьте гипотезу об избыточности ограничения NOT NULL в данном случае. Для этого модифицируйте таблицу, убрав ограничение NOT NULL, и попробуйте добавить 
в нее строку с отсутствующим значением атрибута term (или mark).
*/

ALTER TABLE progress
ALTER COLUMN term
 DROP NOT NULL; 


INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12302, 'Сидиров Сидр Сидорович', 0402, 543283);

INSERT INTO progress (record_book, subject, acad_year, term, mark, test_form)
VALUES (12302, 'Physics', '3', NULL, '3', 'экзамен');

/*
4. В определении таблицы «Успеваемость» (progress) для атрибута mark не только задано ограничение CHECK, но и установлено значение по умолчанию 
с помощью ключевого слова DEFAULT:
...
mark numeric( 1 ) NOT NULL
  CHECK ( mark >= 3 AND mark <= 5 )
  DEFAULT 5,
...

Как вы думаете, что будет, если в ограничении DEFAULT мы «случайно» допустим ошибку, написав DEFAULT 6? Если в команде INSERT не указать значение 
для атрибута mark, то на каком этапе эта ошибка будет выявлена: уже на этапе создания таблицы или только при вставке строки в нее?
Вот эта команда может быть вам полезной для проверки гипотезы, поскольку в ней отсутствует передаваемое значение для атрибута mark:
     INSERT INTO progress ( record_book, subject, acad_year, term )
       VALUES ( 12300, 'Физика', '2016/2017',1 );
*/

ALTER TABLE progress
ALTER COLUMN mark
SET DEFAULT 6;

INSERT INTO progress (record_book, subject, acad_year, term, mark, test_form)
VALUES (12302, 'Biology', '3', NULL, 5, 'экзамен');
  
SELECT *
  FROM progress;

INSERT INTO progress (record_book, subject, acad_year, term, mark, test_form)
VALUES (12302, 'Biology', '3', NULL, '4', 'экзамен'); 

INSERT INTO progress (record_book, subject, acad_year, term, test_form)
VALUES (12302, 'Biology', '3', NULL,'экзамен'); 

ALTER TABLE progress
ALTER COLUMN mark
  SET DEFAULT 5;
  
DROP TABLE progress;

CREATE TABLE progress(
	record_book NUMERIC(5) NOT NULL,
	subject 	TEXT	   NOT NULL,
	acad_year   TEXT	   NOT NULL,
	term 		NUMERIC(1) NOT NULL,
			    CHECK(term = 1 OR term = 2),
	mark		NUMERIC(1) NOT NULL
			    CHECK(mark >= 3 AND MARK <= 5)
			    DEFAULT  6,
	FOREIGN KEY (record_book)
	REFERENCES students (record_book)
	ON DELETE CASCADE
	ON UPDATE CASCADE
);

ALTER TABLE progress
ALTER COLUMN mark
  SET DEFAULT 5;
 
/*
5. В стандарте SQL сказано, что при наличии ограничения уникальности, включающего один или более столбцов, все же возможны повторяющиеся 
значения этих столбцов в разных строках, но лишь в том случае, если это значения NULL. PostgreSQL придерживается такого же подхода.
Модифицируйте определение таблицы «Студенты» (students), добавив ограничение уникальности по двум столбцам: doc_ser и doc_num. А затем 
проверьте вышеприведенное утверждение, добавив в таблицу не только строки, содержащие конкретные значения этих двух столбцов, но также 
и по две строки, имеющие следующие свойства:
– одинаковые значения столбца doc_ser и NULL-значения столбца doc_num;
– NULL-значения столбца doc_num и столбца doc_ser.
Подобные вещи возможны, так как NULL-значения не считаются совпадающими. Это можно проверить с помощью команды
     SELECT (null = null);
Она даст такой результат (т. е. NULL):
      ?column?
     ----------
(1 строка)
*/
SELECT *
  FROM students;
 
ALTER TABLE students
  ADD UNIQUE (doc_ser, doc_num);

INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12303, 'Surname1 Name1', 001, 111111);
 
INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12304, 'Surname2 Name2', 001, 111112); 

INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12305, 'Surname3 Name3', 002, 111111);

INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12306, 'Surname4 Name4', 001, 111111);

INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12307, 'Surname5 Name5', 001, NULL);

INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12308, 'Surname6 Name6', 001, NULL);

INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12309, 'Surname7 Name7', NULL, NULL);

INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12310, 'Surname8 Name8', NULL, NULL);

SELECT (NULL=NULL);

/*
6. Модифицируйте определения таблиц «Студенты» (students) и «Успеваемость» (progress). В таблице students в качестве первичного ключа 
назначьте комбинацию атрибутов doc_ser и doc_num, а в таблице progress соответствующим образом измените определение внешнего ключа.

CREATE TABLE students
   ( record_book numeric( 5 ) NOT NULL UNIQUE,
     name text NOT NULL,
     doc_ser numeric( 4 ),
     doc_num numeric( 6 ),
     PRIMARY KEY ( doc_ser, doc_num )
);
О
братите внимание, что для атрибутов doc_ser и doc_num можно не указывать ограничение NOT NULL: они входят в состав первичного ключа, 
а в нем NULL- значения не допускаются, поэтому ограничение NOT NULL фактически подразумевается при включении атрибута в состав первичного ключа.
   CREATE TABLE progress
   ( doc_ser numeric( 4 ),
     doc_num numeric( 6 ),
     subject text NOT NULL,
     acad_year text NOT NULL,
     term numeric( 1 ) NOT NULL CHECK ( term = 1 OR term = 2 ),
     mark numeric( 1 ) NOT NULL CHECK ( mark >= 3 AND mark <= 5 )
       DEFAULT 5,
     FOREIGN KEY ( doc_ser, doc_num )
       REFERENCES students ( doc_ser, doc_num )
       ON DELETE CASCADE
       ON UPDATE CASCADE
);
Теперь и первичный, и внешний ключи — составные. Проверьте их действие, добавив несколько строк в каждую таблицу.
*/

SELECT *
  FROM students;
 
SELECT * 
  FROM progress;
 
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS progress;

CREATE TABLE IF NOT EXISTS students (
	PRIMARY KEY (doc_ser, doc_num),
	record_book NUMERIC(5) NOT NULL UNIQUE,
	name 	    TEXT       NOT NULL,
	doc_ser     NUMERIC(4),
	doc_num     NUMERIC(6)
);

CREATE TABLE IF NOT EXISTS progress (
	doc_ser   NUMERIC(4),
	doc_num   NUMERIC(6),
	subject   TEXT 		  NOT NULL,
	acad_year TEXT 		  NOT NULL,
	term 	  NUMERIC(1)  NOT NULL
						  CHECK (term = 1 OR term = 2),
	mark 	  NUMERIC(1)  NOT NULL
						  CHECK (mark >= 3 AND mark <= 5)
						  DEFAULT 5,
   FOREIGN KEY (doc_ser, doc_num)
   REFERENCES students (doc_ser, doc_num)
   ON DELETE CASCADE
   ON UPDATE CASCADE
						  
);

INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12340, 'Surname1 Name1', 1000, 100000);

INSERT INTO progress(doc_ser, doc_num, subject, acad_year, term, mark)
VALUES (1000, 100000, 'Physic', 1, 2, 5);

INSERT INTO progress(doc_ser, doc_num, subject, acad_year, term)
VALUES (1000, 100000, 'Physics', 1, 2);


/*
7.* Модифицируйте определение таблицы «Успеваемость» (progress), а если потребуется, то и определение таблицы «Студенты» (students), 
чтобы изучить все варианты реагирования СУБД на обновление строк в ссылочной таблице, в данном случае — students. Последовательно 
изменяйте определение внешнего ключа таблицы progress, испробовав варианты ON UPDATE CASCADE, ON UPDATE RESTRICT, ON UPDATE SET NULL и ON UPDATE SET DEFAULT. 

Для получения информативной картины введите несколько строк в обе таблицы, а затем выполняйте операцию UPDATE, подбирая значения ключевых атрибутов таким образом, 
чтобы вызвать ожидаемую реакцию СУБД.

Учтите, что при использовании фразы ON UPDATE SET DEFAULT необходимо, чтобы, во-первых, с помощью ключевого слова DEFAULT было установлено значение по умолчанию 
для атрибута внешнего ключа в ссылающейся таблице,

а во-вторых, это значение по умолчанию все равно должно присутствовать в одной из строк ссылочной таблицы. Как вы считаете, с учетом сказанного, возможно ли 
использование ON UPDATE SET DEFAULT в нашем случае?
Попробуйте обосновать или, наоборот, опровергнуть целесообразность исполь- зования каждой из этих политик — CASCADE, RESTRICT, SET NULL и SET DEFAULT — 

при выполнении операции UPDATE в реальной информационной системе, предназначенной для учета успеваемости студентов.
 */

/* Option 1: ON UPDATE CASCADE

This option means that when a referenced row in the "students" table is updated, all the related rows in the "progress" table will be updated accordingly. 
To apply this option, we can modify the foreign key constraint in the "progress" table as follows:
*/

SELECT *
  FROM students;
 
SELECT * 
  FROM progress;
 
INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12341, 'Surname2 Name2', 1000, 100001),
	   (12342, 'Surname3 Name3', 1000, 100002),
	   (12343, 'Surname4 Name4', 1000, 100003),
	   (12344, 'Surname5 Name5', 1000, 100004),
	   (12345, 'Surname6 Name6', 1000, 100005);

INSERT INTO progress(doc_ser, doc_num, subject, acad_year, term)
VALUES (1000, 100001, 'Physics', 1, 2),
	   (1000, 100002, 'Math', 1, 2),
	   (1000, 100003, 'Chemistry', 1, 1),
	   (1000, 100004, 'Math', 1, 1),
	   (1000, 100005, 'Math', 1, 2);	  

	  
ALTER TABLE progress
 DROP CONSTRAINT progress_doc_ser_doc_num_fkey,
  ADD CONSTRAINT progress_doc_ser_doc_num_fkey
	  FOREIGN KEY (doc_ser, doc_num)
	  REFERENCES students(doc_ser, doc_num)
	  ON DELETE CASCADE
	  ON UPDATE CASCADE;	  
	  
UPDATE students
   SET doc_ser = 2000
 WHERE name = 'Surname1 Name1';

   
/*	  
Option 2: ON UPDATE RESTRICT

This option means that when a referenced row in the "students" table is updated, the update will be prevented 
if there are related rows in the "progress" table. 
To apply this option, we can modify the foreign key constraint in the "progress" table as follows:
*/

ALTER TABLE progress
 DROP CONSTRAINT progress_doc_ser_doc_num_fkey,
  ADD CONSTRAINT progress_doc_ser_doc_num_fkey
	  FOREIGN KEY (doc_ser, doc_num)
	  REFERENCES students(doc_ser, doc_num)
	  ON DELETE CASCADE
	  ON UPDATE RESTRICT;	

SELECT *
  FROM students;
 
SELECT * 
  FROM progress;
 
UPDATE students
   SET doc_ser = 2001
 WHERE name = 'Surname2 Name2';  


/* Option 3: ON UPDATE SET NULL

This option means that when a referenced row in the "students" table is updated, the values of the foreign key columns in 
the related rows in the "progress" table will be set to NULL. 
To apply this option, we can modify the foreign key constraint in the "progress" table as follows:
*/

ALTER TABLE progress
 DROP CONSTRAINT progress_doc_ser_doc_num_fkey,
  ADD CONSTRAINT progress_doc_ser_doc_num_fkey
	  FOREIGN KEY (doc_ser, doc_num)
	  REFERENCES students(doc_ser, doc_num)
	  ON DELETE CASCADE
	  ON UPDATE SET NULL;	

SELECT *
  FROM students;
 
SELECT * 
  FROM progress;	 

UPDATE students
   SET doc_ser = 2002
 WHERE name = 'Surname3 Name3';   
 
/*
Option 4: ON UPDATE SET DEFAULT

This option means that when a referenced row in the "students" table is updated, the values of the foreign key columns 
in the related rows in the "progress" table will be set to the default value of the column (assuming it has one). 

To apply this option, we can modify the foreign key constraint in the "progress" table as follows:
*/

ALTER TABLE progress
 DROP CONSTRAINT progress_doc_ser_doc_num_fkey,
  ADD CONSTRAINT progress_doc_ser_doc_num_fkey
	  FOREIGN KEY (doc_ser, doc_num)
	  REFERENCES students(doc_ser, doc_num)
	  ON DELETE CASCADE
	  ON UPDATE SET DEFAULT;
	 
SELECT *
  FROM students;
 
SELECT * 
  FROM progress;	 

UPDATE students
   SET doc_ser = 2005
 WHERE name = 'Surname5 Name5';  	 
	 
/* 
8. В таблице «Успеваемость» (progress) есть атрибут «Учебная дисциплина» (subject). Это текстовый атрибут. Одинаковые наименования 
учебных дисциплин записываются в таблицу progress многократно. Создайте еще одну таблицу — «Учебные дисциплины» (subjects), 
в которой будет два атрибута: «Идентификатор учебной дисциплины» (subject_id) и «Учебная дисциплина» (subject). 
Тип данных первого из них будет integer, а второго — text. 

В качестве первичного ключа будет служить subject_id, а второй атрибут будет уникальным. Введите в новую таблицу две-три строки для 
различных учебных дисциплин.

Модифицируйте таблицу progress, заменив атрибут subject на subject_id. Тип данных нового атрибута будет integer. Поскольку тип данных изменится, 
то для замены первоначальных значений, хранящихся в этом столбце, на новые придется использовать конструкцию USING (о ней говорится в тексте главы).
Добавьте в определение таблицы progress еще один внешний ключ, который будет ссылаться на таблицу subjects. 

В составе этого внешнего ключа будет только один атрибут — subject_id. Мы видим, что таблица может иметь больше одного внешнего ключа. 
Таким образом, структура связей в реальной базе данных может оказаться весьма сложной.

Теперь введите несколько строк и в таблицу progress, учитывая ее связь с новой таблицей subjects.
*/

SELECT *
  FROM students;
 
SELECT * 
  FROM progress;
 
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS progress;

CREATE TABLE IF NOT EXISTS students (
	PRIMARY KEY (doc_ser, doc_num),
	record_book NUMERIC(5) NOT NULL UNIQUE,
	name 	    TEXT       NOT NULL,
	doc_ser     NUMERIC(4),
	doc_num     NUMERIC(6)
);

CREATE TABLE IF NOT EXISTS progress (
	doc_ser   NUMERIC(4),
	doc_num   NUMERIC(6),
	subject   TEXT 		  NOT NULL,
	acad_year TEXT 		  NOT NULL,
	term 	  NUMERIC(1)  NOT NULL
						  CHECK (term = 1 OR term = 2),
	mark 	  NUMERIC(1)  NOT NULL
						  CHECK (mark >= 3 AND mark <= 5)
						  DEFAULT 5,
   FOREIGN KEY (doc_ser, doc_num)
   REFERENCES students (doc_ser, doc_num)
   ON DELETE CASCADE
   ON UPDATE CASCADE
						  
);

INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12340, 'Surname1 Name1', 1000, 100000),
	   (12341, 'Surname2 Name2', 1000, 100001),
	   (12342, 'Surname3 Name3', 1000, 100002),
	   (12343, 'Surname4 Name4', 1000, 100003),
	   (12344, 'Surname5 Name5', 1000, 100004),
	   (12345, 'Surname6 Name6', 1000, 100005);

INSERT INTO progress(doc_ser, doc_num, subject, acad_year, term)
VALUES (1000, 100000, 'Math', '2000/2001', 1), 
	   (1000, 100001, 'Physics', '2001/2002', 2),
	   (1000, 100002, 'Math', '2002/2003', 2),
	   (1000, 100003, 'Chemistry', '2003/2004', 1),
	   (1000, 100004, 'Math', '2004/2005', 1),
	   (1000, 100005, 'Math', '2005/2006', 2);	
	   
	  
CREATE TABLE IF NOT EXISTS subjects (
	PRIMARY KEY (subject_id),
	subject_id INTEGER NOT NULL,
	subject	   TEXT    NOT NULL UNIQUE
);	  


INSERT INTO subjects
VALUES (1001, 'Math'),
	   (1002, 'Physics'),
	   (1003, 'Chemistry')
	   
SELECT *
  FROM subjects;
  
ALTER TABLE progress
RENAME COLUMN subject TO subject_id;

ALTER TABLE progress
ALTER COLUMN subject_id TYPE INTEGER
USING (CASE 
	       WHEN subject_id = 'Math' THEN 1001
	       WHEN subject_id = 'Physics' THEN 1002
	       WHEN subject_id = 'Chemistry' THEN 1003
	   END);
	       

SELECT * 
  FROM progress;

ALTER TABLE progress
ADD CONSTRAINT fk_subject_id
FOREIGN KEY (subject_id)
REFERENCES subjects(subject_id);


INSERT INTO progress(doc_ser, doc_num, subject_id, acad_year, term)
VALUES (1000, 100000, 1001, '2002/2003', 2), 
	   (1000, 100001, 1002, '2002/2003', 2),
	   (1000, 100002, 1003, '2002/2003', 2);

	  
/*
9. В таблице «Студенты» (students) есть текстовый атрибут name, на который наложено ограничение NOT NULL. Как вы думаете, 
что будет, если при вводе новой строки в эту таблицу дать атрибуту name в качестве значения пустую строку? 

Например:
     INSERT INTO students ( record_book, name, doc_ser, doc_num )
       VALUES ( 12300, '', 0402, 543281 );

Наверное, проектируя эту таблицу, мы хотели бы все же, чтобы пустые строки в качестве значения атрибута name не проходили в базу данных? 
Какое решение вы можете предложить? Видимо, нужно добавить ограничение CHECK для столбца name. Если вы еще не изучили команду ALTER TABLE, 
то удалите таблицу students и создайте ее заново с учетом нового ограничения, а если вы уже познакомились с командой ALTER TABLE, то сделайте так:
    ALTER TABLE students ADD CHECK ( name <> '' );

Добавив ограничение, попробуйте теперь вставить в таблицу students строку (row), в которой значение атрибута name было бы пустой строкой (string).

Давайте продолжим эксперименты и предложим в качестве значения атрибута name строку, содержащую сначала один пробел, а потом — два пробела.
    INSERT INTO students VALUES ( 12346, ' ', 0406, 112233 );
    INSERT INTO students VALUES ( 12347, '  ', 0407, 112234 );

Для того чтобы «увидеть» эти пробелы в выборке, сделаем так:
    SELECT *, length( name ) FROM students;

Оказывается, эти невидимые значения имеют ненулевую длину. Что делать, чтобы не допустить таких значений-невидимок? Один из способов: 
возложить проверку таких ситуаций на прикладную программу. А что можно сделать на уровне определения таблицы students? Какое ограничение нужно предложить? 
В разделе 9.4 документации «Строковые функции и операторы» есть функция trim. Попробуйте воспользоваться ею. Если вы еще не изучили команду ALTER TABLE, 
то удалите таблицу students и создайте ее заново с учетом нового ограничения, а если уже познакомились с ней, то сделайте так:

    ALTER TABLE students ADD CHECK (...);
    
Есть ли подобные слабые места в таблице «Успеваемость» (progress)?
 */

SELECT *
  FROM students;
	  
INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12346, '', 1000, 100006);

ALTER TABLE students
  ADD CHECK (name != '');
 
ALTER TABLE students
 DROP CONSTRAINT students_name_check1;
 
DELETE FROM students
 WHERE name = '';
	  
INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12346, ' ', 1000, 100006),
	   (12347, '  ', 1000, 100007);
	  
SELECT *,
	   LENGTH(name)
  FROM students;
 
ALTER TABLE students
  ADD CONSTRAINT invisible_chars 
 	  CHECK (TRIM(name) != '');
 
DELETE FROM students
 WHERE TRIM(name) = '';
 
SELECT *
  FROM progress;
  
ALTER TABLE progress
  ADD CONSTRAINT progress_invisible_chars
      CHECK (TRIM(acad_year) != '');
      

/*
10. В таблице «Студенты» (students) атрибут «Серия документа, удостоверяющего личность» (doc_ser) имеет числовой тип, однако в сериях таких документов 
могут встречаться лидирующие нули, которые в числовых столбцах не сохраняются. Например, при записи значения серии «0402» первый ноль не сохранится.
Модифицируйте таблицу students, заменив числовой тип данных на символьный, например, character. 
Как вы думаете, эта операция пройдет без затруднений или они все же возможны? Проверьте ваши предположения, выполнив модификацию.
*/     
     
SELECT * 
  FROM students;

ALTER TABLE progress 
 DROP CONSTRAINT progress_doc_ser_doc_num_fkey;
 
ALTER TABLE students
ALTER COLUMN doc_ser TYPE CHAR(4);

ALTER TABLE progress
ALTER COLUMN doc_ser TYPE CHAR(4);

ALTER TABLE progress 
  ADD CONSTRAINT progress_doc_ser_doc_num_fkey
  	  FOREIGN KEY (doc_ser, doc_num)
  	  REFERENCES students (doc_ser, doc_num)
  	  ON DELETE CASCADE
  	  ON UPDATE CASCADE;
  
INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12346, 'Surname7 Name7', 0001, 100006);


INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12347, 'Surname8 Name8', 0002, 100007);

INSERT INTO students (record_book, name, doc_ser, doc_num)
VALUES (12348, 'Surname9 Name9', '0003', 100008);


/*
11.* В таблице «Рейсы» (flights) есть ограничение, которое регулирует соотношения значений фактического времени вылета и фактического времени прилета. 
Как вы думаете, не является ли выражение actual_arrival IS NOT NULL во второй части условного оператора OR избыточным?
    CREATE TABLE flights
    ( ...
      CHECK ( actual_arrival IS NULL OR
              ( actual_departure IS NOT NULL AND
), ...
  actual_arrival IS NOT NULL AND
  actual_arrival > actual_departure
)
Проверьте ваши предположения на практике. Для этого сначала удалите существующее ограничение с помощью команды
     ALTER TABLE flights DROP CONSTRAINT имя-ограничения;

Как определить имя этого ограничения? С помощью команды
\d flights
получите описание таблицы flights, а в нем есть названия всех ограничений.

Затем создайте это же ограничение, но в модифицированном виде:
     ALTER TABLE flights
       ADD CHECK ( actual_arrival IS NULL OR
         ( actual_departure IS NOT NULL AND
           actual_arrival > actual_departure
) );
Попробуйте добавить в таблицу flights две-три строки, подбирая такие зна- чения атрибутов actual_departure и actual_arrival, чтобы проверить
все возможные исходы этих проверок. Конечно, вместо добавления новых строк можно модифицировать одну и ту же строку с помощью команды UPDATE.
*/

SELECT * 
  FROM flights;
  
 
SELECT MAX(flight_id)
  FROM flights;
 
ALTER TABLE flights
 DROP CONSTRAINT flights_check1;

ALTER TABLE flights
  ADD CONSTRAINT flights_check1 
  	  CHECK (actual_arrival IS NULL 
  	  OR (actual_departure IS NOT NULL AND actual_arrival > actual_departure));
 
  	 
INSERT INTO flights (
	--flight_id, 
	flight_no, 
	scheduled_departure, 
	scheduled_arrival, 
	departure_airport, 
	arrival_airport, 
	status, 
	aircraft_code, 
	actual_departure, 
	actual_arrival
)
VALUES (
	'AI0001',
	'2022-03-10 03:10:00-2',
	'2022-03-10 07:20:00-2',
	'DME',
	'LED',
	'Scheduled',
	'763',
	NULL,
	NULL
); 
 
-- 214867
 

 
SELECT * FROM flights WHERE flight_id = 4;
 
SELECT * FROM flights_flight_id_seq;
 
SELECT setval('flights_flight_id_seq', (SELECT MAX(flight_id) FROM flights));
 
 
SELECT MAX(flight_id)
  FROM flights;  
 
SELECT *
  FROM flights
 WHERE flight_id = (SELECT MAX(flight_id) FROM flights);
 
 
INSERT INTO flights (
	--flight_id, 
	flight_no, 
	scheduled_departure, 
	scheduled_arrival, 
	departure_airport, 
	arrival_airport, 
	status, 
	aircraft_code, 
	actual_departure, 
	actual_arrival
)
VALUES (
	'AI0001',
	'2022-03-11 03:10:00-2',
	'2022-03-11 07:20:00-2',
	'DME',
	'LED',
	'Scheduled',
	'763',
	'2022-03-11 03:10:15-2',
	NULL
); 


INSERT INTO flights (
	--flight_id, 
	flight_no, 
	scheduled_departure, 
	scheduled_arrival, 
	departure_airport, 
	arrival_airport, 
	status, 
	aircraft_code, 
	actual_departure, 
	actual_arrival
)
VALUES (
	'AI0001',
	'2022-03-12 03:10:00-2',
	'2022-03-12 07:20:00-2',
	'DME',
	'LED',
	'Scheduled',
	'763',
	NULL,
	'2022-03-12 07:20:15-2'
); 
  
INSERT INTO flights (
	--flight_id, 
	flight_no, 
	scheduled_departure, 
	scheduled_arrival, 
	departure_airport, 
	arrival_airport, 
	status, 
	aircraft_code, 
	actual_departure, 
	actual_arrival
)
VALUES (
	'AI0001',
	'2022-03-12 03:10:00-2',
	'2022-03-12 07:20:00-2',
	'DME',
	'LED',
	'Scheduled',
	'763',
	'2022-03-12 07:20:16-2',
	'2022-03-12 07:20:15-2'
);  

INSERT INTO flights (
	--flight_id, 
	flight_no, 
	scheduled_departure, 
	scheduled_arrival, 
	departure_airport, 
	arrival_airport, 
	status, 
	aircraft_code, 
	actual_departure, 
	actual_arrival
)
VALUES (
	'AI0001',
	'2022-03-12 03:10:00-2',
	'2022-03-12 07:20:00-2',
	'DME',
	'LED',
	'Scheduled',
	'763',
	'2022-03-12 07:20:14-2',
	'2022-03-12 07:20:15-2'
);  
 
SELECT * FROM flights WHERE flight_id = 4;
 
SELECT * FROM flights_flight_id_seq;
 
SELECT setval('flights_flight_id_seq', (SELECT MAX(flight_id) FROM flights)); 

SELECT setval('flights_flight_id_seq', (SELECT MIN(flight_id) FROM flights)); 

INSERT INTO flights (
	flight_id, 
	flight_no, 
	scheduled_departure, 
	scheduled_arrival, 
	departure_airport, 
	arrival_airport, 
	status, 
	aircraft_code, 
	actual_departure, 
	actual_arrival
)
VALUES (
	DEFAULT,
	'AI0001',
	'2022-03-13 03:10:00-2',
	'2022-03-13 07:20:00-2',
	'DME',
	'LED',
	'Scheduled',
	'763',
	'2022-03-13 07:20:14-2',
	'2022-03-13 07:20:15-2'
);  

INSERT INTO flights (
	flight_id, 
	flight_no, 
	scheduled_departure, 
	scheduled_arrival, 
	departure_airport, 
	arrival_airport, 
	status, 
	aircraft_code, 
	actual_departure, 
	actual_arrival
)
VALUES (
	DEFAULT,
	'AI0001',
	'2022-03-14 03:10:00-2',
	'2022-03-14 07:20:00-2',
	'DME',
	'LED',
	'Scheduled',
	'763',
	'2022-03-14 07:20:14-2',
	'2022-03-14 07:20:15-2'
);  

SELECT MAX(flight_id) FROM flights;

SELECT nextval('flights_flight_id_seq');

/* 
12. Команда ALTER TABLE позволяет переименовать таблицу. Например: ALTER TABLE table_name RENAME TO new_table_name;
Поскольку в командах создания таблиц базы данных «Авиаперевозки» мы не указывали имена ограничений для первичных и 
внешних ключей, то их имена были сформированы автоматически самой СУБД. Как вы думаете, получили ли эти ограничения 
новые имена после переименования таблицы?
Проверьте ваши предположения, выполнив такую операцию с одной из таблиц базы данных «Авиаперевозки», имеющих внешние ключи.
*/
 ALTER TABLE flights
	   RENAME TO flights_new;

 ALTER TABLE flights_new
	   RENAME TO flights;
	  

/*
13. И представление «Рейсы» (flights_v), и материализованное представление «Маршруты» (routes) построены на основе 
таблиц «Рейсы» (flights) и «Аэропорты» (airports). Логично предположить, что при каскадном удалении, например, таблицы «Аэропорты», 
представление «Рейсы» будет также удалено, поскольку при удалении базовой таблицы этому представлению просто неоткуда будет брать данные.

А что вы можете предположить насчет материализованного представления «Маршруты»: будет ли оно также удалено или нет? 
Ведь оно уже содержит данные, в отличие от обычного представления. Так ли, условно говоря, сильна его связь с таблицами, 
на основе которых оно сконструировано?

Проведите необходимые эксперименты, начав с команды
    
    DROP TABLE airports;
    
Если вам потребуется восстановить все объекты базы данных, то вы всегда сможете воспользоваться файлом demo_small.sql и просто 
повторить процедуру развертывания учебной базы данных, которая описана в главе 2. Поэтому смело экспериментируйте с таблицами и представлениями.
*/

SELECT *
  FROM flights_v;
 
DROP TABLE flights CASCADE;

/*
14. Представления (views) могут быть обновляемыми. Это значит, что можно с помощью команд INSERT, UPDATE и DELETE, применяемых 
к представлению, внести изменения в таблицу, лежащую в основе этого представления.
Самостоятельно ознакомьтесь с этим вопросом с помощью документации (см. описание команды CREATE VIEW) и, создав простое представление 
над одной из таблиц базы данных «Авиаперевозки», выполните несколько команд с целью внесения изменений в эту таблицу.
 */

SELECT * 
  FROM ticket_flights;


-- VIEW FROM ONE TABLE
CREATE OR REPLACE VIEW tickets_v_one_table AS
SELECT ticket_no, 
	   fare_conditions
  FROM ticket_flights;

SELECT *
  FROM tickets_v_one_table; 
 
UPDATE tickets_v_one_table
   SET fare_conditions = 'Comfort'
 WHERE ticket_no = '0005432688048'
   AND fare_conditions = 'Business';  
  
SELECT *
  FROM tickets_v_one_table
 WHERE ticket_no = '0005432688048'; 

SELECT *
  FROM ticket_flights
 WHERE ticket_no = '0005432688048'; 



CREATE OR REPLACE VIEW tickets_v AS
SELECT tf.ticket_no, tf.fare_conditions, t.passenger_id
FROM ticket_flights AS tf
JOIN tickets AS t
  ON tf.ticket_no = t.ticket_no;

CREATE OR REPLACE FUNCTION update_tickets_v_function()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE bookings.ticket_flights
    SET fare_conditions = NEW.fare_conditions
    WHERE ticket_no = NEW.ticket_no;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER update_tickets_v
INSTEAD OF UPDATE ON bookings.tickets_v
FOR EACH ROW
EXECUTE FUNCTION update_tickets_v_function();


SELECT *
  FROM tickets;

UPDATE tickets_v
SET fare_conditions = 'Comfort'
WHERE ticket_no = '0005434849212'
  AND fare_conditions = 'Business'; 
  
SELECT *
  FROM ticket_flights
 WHERE ticket_no = '0005434849212'; 


/* 15. Определение таблицы можно изменить с помощью команды ALTER TABLE. 
   Аналогичные команды существуют и для изменения представлений и материализованных представлений: ALTER VIEW и ALTER MATERIALIZED VIEW. 
   Самостоятельно ознакомьтесь с их возможностями с помощью документации.*/


DROP VIEW IF EXISTS tickets_v;


CREATE VIEW tickets_v AS
SELECT tf.ticket_no, tf.fare_conditions, t.passenger_id, t.passenger_name AS modified_passenger_name
FROM ticket_flights AS tf
JOIN bookings.tickets AS t ON tf.ticket_no = t.ticket_no;

SELECT *
  FROM tickets_v;

 
ALTER TABLE tickets
DROP COLUMN contact_data;

SELECT *
  FROM tickets;
 
/* 
16. Как вы думаете, при изменении данных в таблицах, на основе которых сконструировано материализованное представление, 
содержимое этого представления тоже синхронно изменяется или нет?
Если содержимое материализованного представления изменяется синхронно с базовыми таблицами, то продемонстрируйте это. 
Если же оно остается неизменным, то покажите, как его синхронизировать с базовыми таблицами. 
*/
 
CREATE MATERIALIZED VIEW my_materialized_view AS
SELECT tf.ticket_no, tf.fare_conditions, t.passenger_id
  FROM ticket_flights AS tf
  JOIN bookings.tickets AS t ON tf.ticket_no = t.ticket_no;


REFRESH MATERIALIZED VIEW my_materialized_view;

REFRESH MATERIALIZED VIEW my_materialized_view WITH DATA;

DROP MATERIALIZED VIEW my_materialized_view;


/*
17. Представления могут быть, условно говоря, вертикальными и горизонтальными. При создании вертикального представления 
в список его столбцов включается лишь часть столбцов базовой таблицы (таблиц). 
Например:
     CREATE VIEW airports_names AS
       SELECT airport_code, airport_name, city
       FROM airports;
     SELECT * FROM airports_names;

В горизонтальное представление включаются не все строки базовой таблицы (таблиц), а производится их отбор с помощью фраз WHERE или HAVING.

Например:
     CREATE VIEW siberian_airports AS
       SELECT * FROM airports
       WHERE city = 'Новосибирск' OR city = 'Кемерово';
     SELECT * FROM siberian_airports;

Конечно, вполне возможен и смешанный вариант, когда ограничивается как список столбцов, так и множество строк при создании представления.
Подумайте, какие представления было бы целесообразно создать для нашей базы данных «Авиаперевозки». 

Необходимо учесть наличие различных групп пользователей, например: пилоты, диспетчеры, пассажиры, кассиры.
Создайте представления и проверьте их в работе.
*/

CREATE OR REPLACE VIEW airports_names AS 
SELECT airport_code AS "Airport Code",
	   airport_name AS "Airport Name",
	   city AS "City" 
  FROM airports
 WHERE city IN ('Новосибирск', 'Кемерово', 'Красноярск', 'Иркутск', 'Томск', 'Братск', 'Тюмень');
 
SELECT *
  FROM airports_names;
  
 /*
 18.* Предположим,что нам понадобилось иметь в базе данных сведения о технических характеристиках самолетов, 
 эксплуатируемых в авиакомпании. Пусть это будут такие сведения, как число членов экипажа (пилоты), тип двигателей и их количество.
 
 Следовательно, необходимо добавить новый столбец в таблицу «Самолеты» (aircrafts). Дадим ему имя specifications, а в качестве типа 
 данных выберем jsonb. 
 
 Если впоследствии потребуется добавить и другие характеристики, то мы сможем это сделать, не модифицируя определение таблицы.
 
ALTER TABLE aircrafts ADD COLUMN specifications jsonb;
ALTER TABLE

Добавим сведения для модели самолета Airbus A320-200:
UPDATE aircrafts
  SET specifications =
      '{ "crew": 2,
         "engines": { "type": "IAE V2500",
"num": 2 }
       }'::jsonb
  WHERE aircraft_code = '320';
UPDATE 1

Посмотрим, что получилось:

SELECT model, specifications
  FROM aircrafts
  WHERE aircraft_code = '320';
      model      |              specifications
-----------------+-------------------------------------------
 Airbus A320-200 | {"crew": 2, "engines": {"num": 2, "type":
                    "IAE V2500"}}
(1 строка)
Можно посмотреть только сведения о двигателях:
SELECT model, specifications->'engines' AS engines
  FROM aircrafts
  WHERE aircraft_code = '320';
      model      |            engines
-----------------+---------------------------------
 Airbus A320-200 | {"num": 2, "type": "IAE V2500"}
(1 строка)

Чтобы получить еще более детальные сведения, например, о типе двигателей, нужно учитывать, что созданный JSON-объект имеет сложную структуру: 
он содержит вложенный JSON-объект. Поэтому нужно использовать оператор #> для указания пути доступа к ключу второго уровня.

SELECT model, specifications #> '{ engines, type }'
  FROM aircrafts
  WHERE aircraft_code = '320';
      model      |  ?column?
-----------------+-------------
 Airbus A320-200 | "IAE V2500"
(1 строка)

Задание. Подумайте, какие еще таблицы было бы целесообразно дополнить столбцами типа json/jsonb. Вспомните, что, например, в таблице «Билеты» (tickets) 
уже есть столбец такого типа — contact_data. Выполните модификации таблиц и измените в них одну-две строки для проверки правильности ваших решений.
*/

 
  ALTER TABLE aircrafts 
    ADD COLUMN specifications jsonb;
    
  SELECT *
    FROM aircrafts
   LIMIT 100; 
  
  UPDATE aircrafts
     SET specifications =
      '{ "crew": 2,
         "engines": { "type": "IAE V2500", "num": 2 }
       }'::jsonb
   WHERE aircraft_code = '320';

SELECT model, specifications
  FROM aircrafts
 WHERE aircraft_code = '320'; 
 
SELECT model, specifications -> 'engines' AS engines
  FROM aircrafts
 WHERE aircraft_code = '320';
  
SELECT model, specifications #> '{ engines, type }'
  FROM aircrafts
 WHERE aircraft_code = '320'; 