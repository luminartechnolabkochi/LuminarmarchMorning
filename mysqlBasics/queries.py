#mysql queries
#query for creating database
#>create database database_name;


#quey for listing all databases

#>show databases;


#query for using a specific database;


#mysql query for creating table;

#>create table table_name (column_name type,column_name datatype,,,,,,);
#varchar =>string array
#int

#create table employee (eid varchar(23),ename varchar(25),desig varchar(25),salary int,exp int,location varchar(25));

#listing all tables;

#>show tables;


#display structure of table;


#>desc tablename;

#>desc employee;

#insert record into table;

#>insert into table_name (column1,column2,,,,,,) values(value1,value2,,,,,);

#insert into employee(eid,ename,desig,salary,exp,location) values('1000','ajay','developer',25000,2,'ekm');


#fetching all records from table;
#>select * from employee;

#>fetching a specif columns

#fetching names from employee tables;

#> select ename from employee;

# fetch employee details whose salary > 22000?
#>select * from employee where salary >22000;

#fetch employee details who are working in ekm;

#>select * from employee where location ='ekm';


#fecth employee details whose salary > 22000 and exp >1?
#> select * from employee where salary > 22000 and exp >1;



