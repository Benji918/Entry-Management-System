
# Entry-Management-Software
This project has been developed for solving notification problem for host and visitor. It is a web application based on Python Flask with SQLAlchemy Database and Textlocal API

# Problem-Statement
If you have any client or deal fixing meeting with anyone,then everyone want an website or app that can notify the arrival of the visitor by SMS or Email to the host with information such as Name, Email, Phone Number and Checkin time. And as visitor, everyone want host information with check in and check out time though an registered Email

# Solution 
This web application will trigger an email and an SMS to the host informing him of the details of the visitor. And after checkout by Visitor, he will get an information of host with checkin and checkout time.

# How to Setup the Website
Step 1) Download the zip file of the project and extract it to your local system
Step 2) Open the terminal to the project folder location
<br>** Specifying the path in terminal 
<pre>cd location_of_the_folder </pre>
Step 3) Instaling the packages
<pre>pip install -r requirements.txt</pre>
Step 4) Running the Project on the local system
<pre> python app.py </pre>
Step 5) Open 
<pre> http://localhost:5000 </pre>
on your browser


# How does Application Work
At the Homescreen,User have an two button option, One for Host and One for visitor.First Host have to fill up the detail in the host section. All the host detail get saved into database and screen will show up Thank page to the host.
<br>
Now,If you are visiting as visitor, select the visitor option on the homescreen.
Fillup your detail on the given form, click on the checkin button.Now all the information will get save into the database and now application will trigger an Email and Sms to the Host about the visitor arrival with his information. Checkout page will trigged on the visitor screen with Checkout button. After clicking on the checkout button, Visitor will get an information regarding the host with check-in and check-out time through an Email.Finally Thank message will on the visitor Screen.


# Application Overview 
## Front End
Front has been developed on HTML,CSS,Javascript. It have the following page:
1. <b>index</b> - This is the homescreen page having the two option for host and visitor.
![Screenshot from 2019-11-28 10-31-06](https://user-images.githubusercontent.com/37480057/69778442-56781e00-11ca-11ea-9d63-b1a15eec094c.png)
2. <b>Host</b> - Page is developed for getting information from the host
![Screenshot from 2019-11-28 10-33-24](https://user-images.githubusercontent.com/37480057/69778517-90e1bb00-11ca-11ea-8a80-2744df8003e0.png)
3. <b>Hostthank</b> - Thank you message page with home button.
![Screenshot from 2019-11-28 10-34-47](https://user-images.githubusercontent.com/37480057/69778551-ba9ae200-11ca-11ea-9d6f-7b2aee6b63c1.png)
4. <b>visitor</b> - This page has been developed to get visitor information with checkin time.
![Screenshot from 2019-11-28 10-40-30](https://user-images.githubusercontent.com/37480057/69778755-8b38a500-11cb-11ea-8881-2015900943f8.png)
5. <b>hostcheck</b> This page will be triggered when visitor just check-in to provide an check-out option.
![Screenshot from 2019-11-28 10-41-42](https://user-images.githubusercontent.com/37480057/69778804-c0dd8e00-11cb-11ea-9df6-53bac61fbb6f.png)
6. <b>thankvisitor</b> This is thank giving page to the visitor.
![Screenshot from 2019-11-28 10-43-34](https://user-images.githubusercontent.com/37480057/69778869-0732ed00-11cc-11ea-9a67-52c5554c088c.png)
 
## Backend
Backend is developed using the Python Flask with SQLAlchemy(Object Relational Mapper(ORM)) database and TextLocal API for SMS delivery.
1. <b> Python Flask </b> : Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.
<br>
2. <b> SQLAlchemy</b> : SQLAlchemy is an open-source SQL toolkit and object-relational mapper for the Python programming language released under the MIT License
<br>
3. <b> Twilio Api</b>: I use this API service to send the host an SMS of the guest details.

#### Overview
#### Host Backend Overview
<pre>Information -> Database -> Host Back to Homescreen </pre>
#### Visitor Backend Overview
<pre>Information -> Database -> Information fetch -> Transfered to Email and SMS function -> Successfully Transfered to Host -> checkout by visitor -> Information Email to user End.</pre>

## Basic Overview
![Screenshot from 2019-11-28 11-23-38](https://user-images.githubusercontent.com/37480057/69780549-98f12900-11d1-11ea-9de1-bdcd6f627f35.png)

