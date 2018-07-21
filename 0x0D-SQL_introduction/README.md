## 0x0D. SQL - Introduction

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/rtcwz.jpg)

**About MySQL**

MySQL is an open source database management software that helps users store, organize, and retrieve data. It is a very powerful program with a lot of flexibility—this tutorial will provide the simplest introduction to MySQL

How to Install MySQL on Ubuntu and CentOS
If you don't have MySQL installed on your droplet, you can quickly download it.

**Ubuntu:**

`sudo apt-get install mysql-server`

How to Access the MySQL shell
Once you have MySQL installed on your droplet, you can access the MySQL shell by typing the following command into terminal:

`mysql -u root -p`

After entering the root MySQL password into the prompt (not to be confused with the root droplet password), you will be able to start building your MySQL database.

**Two points to keep in mind:**

1. All MySQL commands end with a semicolon; if the phrase does not end with a semicolon, the command will not execute.

2. Also, although it is not required, MySQL commands are usually written in uppercase and databases, tables, usernames, or text are in lowercase to make them easier to distinguish. However, the MySQL command line is not case sensitive.
(source: https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)

**What you should learn from this project**

       At the end of this project you are expected to be able to explain to anyone,
       without the help of Google:

* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does DDL and DML stand for
* How to CREATE or ALTER a table
* How to SELECT data from a table
* How to INSERT, UPDATE or DELETE data
* What are subqueries
* How to use MySQL functions

**Requirements for SQL scripts**

* Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)

**Exercises**

**0. List databases**

	Write a script that lists all databases of your MySQL server.

**1. Create a database mandatory**

	Write a script that creates the database hbtn_0c_0 in your MySQL server.

* If the database hbtn_0c_0 already exists, your script should not fail
* You are not allowed to use the SELECT or SHOW statements

**2. Delete a database**

	Write a script that deletes the database hbtn_0c_0 in your MySQL server.

* If the database hbtn_0c_0 doesn’t exist, your script should not fail
* You are not allowed to use the SELECT or SHOW statements

**3. List tables**

	Write a script that lists all the tables of a database in your MySQL server.

* The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)

**4. First table**

	Write a script that creates a table called first_table in the current database in
	your MySQL server.

* first_table description:
	* id INT
	* name VARCHAR(256)
* The database name will be passed as an argument of the mysql command
* If the table first_table already exists, your script should not fail
* You are not allowed to use the SELECT or SHOW statements

**5. Full description**

	Write a script that prints the full description of the table first_table from the
	database hbtn_0c_0 in your MySQL server.

* The database name will be passed as an argument of the mysql command
* You are not allowed to use the DESCRIBE or EXPLAIN statements

**6. List all in table**

	Write a script that lists all rows of the table first_table from the database
	hbtn_0c_0 in your MySQL server.

* All fields should be printed
* The database name will be passed as an argument of the mysql command

**7. First add mandatory**

	Write a script that inserts a new row in the table first_table (database hbtn_0c_0)
	in your MySQL server.

* New row:
	* id = 89
	* name = Holberton School
* The database name will be passed as an argument of the mysql command

**8. Count 89**

	Write a script that displays the number of records with id = 89 in the table
	first_table of the database hbtn_0c_0 in your MySQL server.

* The database name will be passed as an argument of the mysql command

**9. Full creation**

	Write a script that creates a table second_table in the database hbtn_0c_0 in your
	MySQL server and add multiples rows.

* second_table description:
	* id INT
	* name VARCHAR(256)
	* score INT
* The database name will be passed as an argument to the mysql command
* If the table second_table already exists, your script should not fail
* You are not allowed to use the SELECT and SHOW statements
* Your script should create these records:
	* id = 1, name = “John”, score = 10
	* id = 2, name = “Alex”, score = 3
	* id = 3, name = “Bob”, score = 14
	* id = 4, name = “George”, score = 8

**10. List by best**

	Write a script that lists all records of the table second_table of the database
	hbtn_0c_0 in your MySQL server.

* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the mysql command

**11. Select the best**

	Write a script that lists all records with a score >= 10 in the table second_table
	of the database hbtn_0c_0 in your MySQL server.

* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the mysql command

**12. Cheating is bad**

	Write a script that updates the score of Bob to 10 in the table second_table.

* You are not allowed to use Bob’s id value, only the name field
* The database name will be passed as an argument of the mysql command

**13. Score too low**

	Write a script that removes all records with a score <= 5 in the table second_table
	of the database hbtn_0c_0 in your MySQL server.

* The database name will be passed as an argument of the mysql command

**14. Average**

	Write a script that computes the score average of all records in the table
	second_table of the database hbtn_0c_0 in your MySQL server.

* The result column name should be average
* The database name will be passed as an argument of the mysql command

**15. Number by score**

	Write a script that lists the number of records with the same score in the table
	second_table of the database hbtn_0c_0 in your MySQL server.

* The result should display:
	* the score
	* the number of records for this score with the label number
* The list should be sorted by the number of records (descending)
*  The database name will be passed as an argument to the mysql command

**16. Say my name**

	Write a script that lists all records of the table second_table of the database
	hbtn_0c_0 in your MySQL server.

* Don’t list rows without a name value
* Results should display the score and the name (in this order)
* Records should be listed by descending score
* The database name will be passed as an argument to the mysql command
In this example, new data have been added to the table second_table.
