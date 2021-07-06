https://restapi-demo-grame.herokuapp.com/

#Demonstrates working of REST API for GET,UPDATE,POST,DELETE methods

Technology Stack: Backend:{Python + Flask + SQLAlchemy} , Frontend:{Bootstrap + HTML + CSS}

GUI working:

1. The home page consists of a form that provides options for Operations to be performed and text fields for two variables.

2. When a user chooses an operation ,provides two numbers as input and clicks submit, the OUtput is shown on the GUI

3. To Request for new Operations to be added click on add button which takes the user to another form where a user can request for a function to be added in the python file

4. On the Operation Request page , a user can create , update and delete a request.(CRUD)


Approach:

1. App.py uses requests,flask,flask-SQLAlchemy for getting requests from UI and storing it in database.
2. Operations.py consists of all the listed operations on UI
3. Any new operation requested will be added in Operations.py by the backend developer.
4. A user can request,update and delete a new operation requested.
5. The database stores all new operations that have been requested.
6. The information is requested through REST APIs and respective operations are performed.
