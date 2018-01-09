Disaster-Site-Resources-Locator

Disaster-Site-Resources-Locator App

This app will manage the data of requesters and suppliers of different resources during a Disaster. This data is related to accounts (supplier, needer, administrator), resources, transactions, orders, payment options and many other important relationships between each of these entities. The application manages data from three tables:

    Accounts (suuplier, needer, administrator) - information of the account owner
    Credentials - information to login account
    Address - information of address for a given account
    City - city where the account owner lives
    Region - region where the city is part of
    Resources - information about resources in the system.
    Resource Requested - information of a resource requested by a requester and not available 		as an actual resource.
    Keyword - keywords for a resource of a resource requested
    Category - possible categories for given resources (also sub-categories)
    Transactions - information regarding a resource being sell from a supplier to a needer in an specific order
    Order_Info - order that contain a group of transactions
    Payment (Cash, Credit_Card) - information regarding the payment methods used
    Bank_Account - bank account owned by a supplier
    

The application is organized in three broad layers:

    Main - the main app module takes care to setup the routes for the REST API and calling the proper handler objects to process the request.
    Handlers - the handler modules takes care of implementing the logic of each REST call. In this sense, a handler is a Facade for accessing a given operation on a data collection. Each object handles a particular type of request for a data collection (e.g. Resources). The handlers rely upon the Data Access Objects (DAOs) to extact data from the database. The handlers encode the responses to the client with JSON and provide the appropriate HTTP response code.
    DAOs - implementation for the Data Access Objects (DAOs) that take care of moving data in and out of the database engine by making SQL queries and wrapping the results in the objects and object list of appropriate types.

Requirements

You need the following software installed to run this application:

    PostgreSQL - database engine
    Pyscopg2 - library to connect to PostgreSQL form Python
    PgAdmin3 - app to manage the databases
    Flask - web bases framework to implement the REST API.



Completed 1/9/18
