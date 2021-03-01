### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  PostgreSQL is an object-relational database management system. It is used as a database warehouse to store data in table form.
- What is the difference between SQL and PostgreSQL?
  SQL is a programming language used in managing data in a relational database. PostgreSQL uses SQL to set up tables and relationships, and to create databases.
- In `psql`, how do you connect to a database?
type psql, then type \l to list all databases
finally type \c and the name of the database to connect(eg:\c pets)

- What is the difference between `HAVING` and `WHERE`?
WHERE is used to filter rows for specific details before GROUP BY.
HAVING is used to filter rows after GROUP BY

- What is the difference between an `INNER` and `OUTER` join?\
INNER join is the common overlap between two tables
OUTER join includes INNER join but also includes data not found in the other table.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
LEFT OUTER and RIGHT OUTER signify the set of data except that they each represent their respective table and the INNER JOIN.

- What is an ORM? What do they do?
Object relational mapping is applying object oriented programming to a database management system. Database management systems are not object oriented and may be difficult to use without the use of ORM.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  Using AJAX to make a request will send the request from the client directly to the server. The user will have to have credentials and authentication on their client.
  Using a request through server-side will allow the user to access all data through the one server.

- What is CSRF? What is the purpose of the CSRF token?
CSRF is cross sight request forgery. It is when malicious users exploit code on a web app to trick other users into submitting information they did not mean to share.
CSRF token is used as a key to ensure that a form sent by the server is was untampered with when a user sends a response. 

- What is the purpose of `form.hidden_tag()`?
This is used alongside a form, but is hidden from the users view. It produces a field that contains the CSRF token sent by the server.