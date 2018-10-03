# students-grades
Python3.6, Bottle, pytest, SQLAlchemy, jQuery, bootstrap, anychart

A school needs to keep the grade records for the students and also produce some statistics about them.
The teachers need to be able enter the following information for a student:

 - Name
 - Date of birth
 - Student’s class (possible values: IT Class, Math Class, Literature Class)
 - Grade information: 
     1. Year (i.e. 2014)
     2. Quarter (i.e. Q1)
     3. Math grade(i.e. 6)
     4. Computer grade(i.e. 6)
     5. Literature grade(i.e. 6)
 
There are three main charts that need to be shown in order to display the imported data. If you feel you
want to add more representations of the data feel free, but the three charts below are necessary. How
you render them is up to you as long as they display the expected data.
 - User should be able to select a student from the ones available in the system. As soon as one student is
selected the chart will load his total subject grade average per quarter.
 - User should be able to select a subject from the ones available in the system. As soon as a subject (E.g.:
Math) is selected the chart will load grade averages from all students in each quarter.
 - User needs to be able to select from the available quarters (Ex: 2000 – Q1, 2000 – Q2). Upon selection of
a quarter it should show the averages per subject for the selected quarter.

There are two aspects to this application; the server and the client.

THE SERVER

You are asked to create a server application which exposes a web API to handle the submission of
information, storing them in the database and retrieving their statistics.

THE CLIENT

On the client side we give you the freedom to choose what UI you want to give to your API. You can
implement the client as a web application using HTML, Javascript and CSS or as an Android mobile app
Either approach needs to provide a nice and intuitive user interface which allows for simple data entry
which makes it simple to add a lot of students. Both approaches need to use your server API to store
and retrieve data.
Your client needs to have interfaces for:
 - Data entry (entering the student records and their grades for the different subjects and
quarters)
 - Statistics (ability to see the requested charts and data in a nice and useful way!)
 
 MANDATORY TECHNOLOGIES/CONCEPTS
 
There are certain technologies and concepts we definitely want to see you use in your application.
For the server side:
 - Your service needs to be RESTful
 - For the backend engine for development you need to use Python. You are asked to use the Bottle to implement your backend (http://bottlepy.org/docs/dev/index.html). Bottle is a simple
micro framework to give you the basis on which you can build your web server.
 - For the backend database you can use any SQL based DBMS (i.e. MySQL).

For a web based client side: 
- You need to use the obvious HTML, Javascript and CSS
 - You need to appropriately use AJAX on your pages where it makes sense to make the UI more
fluid.

For an android based client side:
 - Should be able to run it on an android phone

GENERAL NOTES

 - Please include some short instructions on how to run the application and the database on our
local machines.
 - Your database implementation should be sent to us as an SQL file which we can deploy on our
local machine. Please include instructions on how to setup your database as part of the short
instructions asked from you above.
 - You can use any other components or libraries. The only limitation is that they have to be free or
open source.