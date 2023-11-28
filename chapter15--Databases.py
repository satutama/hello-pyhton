'''
Relational Databases
    Relational databases model data by storing rows and columns in tables.
    The power of the relational databases lies in its ability to efficiently retrieve data from those tables
    and in particular where there are multiple tables and the relationships between those tables involed in the query.

    Terminology
        Database - contains many tables
        Relation (or table) - contains tuples that have the same attributes
        Tuple (or row) - a set of fields that generally represents an "object" like a person or a music trac
        Attribute (also column or field) - on of possibly many elements of data corresponding to the object represented by the row


SQL - Structured Query Language
    Language we use to issue commands to the databse
    . Create a table
    . Retrieve some data
    . Insert data
    . Delete data

Web Applications w/ Databases
    . Application Developer - Builds the logic for the application, the look and feel of the application - monitors the application for problems
    . Database Administrator - Monitors and adjusts the database as the program runs in production
    . Often both people participate in the building of the "Data model"

Database Model 
    or database schema is the structure or format of a database, described in a formal language supported by the database managbement system.
    In other words, a 'database model'is the application of a data model when used in conjunction with a database management system.

Common Database Systems
    Three major Database Management Systems:
    . Oracle - Large, commercial, enterprise-scale, very very tweakable
    . MySql - simpler but very fast an scalable - commercial open source
    . SqlServer - very nice - from microsoft

    Smaller projects, free and open source
    . HSQL, SQLite, Postgres,...


SQLlite is very popular. SQLite is what's called an embedded database system. Python is builtin with it.
It's very popular because it's free, open source and such a tiny little piece of stoftware that you just include it in other software.
SQLite browsers allows us to directly manipulate SQLite files (http://sqlitebrowser.org)

'''

'''
SQL Syntax

check database reference folder on database-handout.txt file
'''


'''
Database Design
    . Building a Data Model basic rule: Don't put the same string data in twice - use a relationship instead
    . Where there is one thing in the "real world" there should be one copy of that thing in the database
    . For each 'piece of info':
        Is the column an boject or an attribut of another object?
        Once we define objects, we need to define the relationships between objects

Database Normalization (3NF)
    . There is *tons* of database theory - way too much to understand witouht escessive predicate calculus
    . Do not replicate data - reference data - point at data
    . Use intergers for keys and for references
    . Add a special "key" column to each table which we will make references to (common to call this column 'id').          

Integer reference Pattern
    . We use integers to reference rows in another table
    . Three kinds of keys: 
        - Primary key, generally an integer auto-increment field
        - logical key, What the outside world uses for lookup
        - foreign key, generally an integer key pointing to a row in another table

    Key Rules
    . Never use your logical key as the primary key
    . Logical keys can and do change, albeit slowly
    . Relationships that are based on matching string fields are less efficient than integers
    
'''

'''
Using Join Across Tables
    Relational Power
    -   By removing the replicated data and replacing it with refrences to a single copy of each bit of data 
        we build a 'web' of information that the relational database can read through very quickly - even for very large amounts of data
    -   Often when you want some data it comes from a number of tables linked by these foreign keys

    
    The JOIN Operation 
    . Links across several tables as part of a select operation
    . You must tell the JOIN how to use the keys that make the connection between the tables using an ON clause
    . Joining two tables without an ON clause gives all possible combination of rows

    SELECT Album.title, Artist.name FROM Album JOIN Artist 
    ON Album.artist_id = Artist.id

    Album.title and Artist.name -> What we want to see
    Album and Artist -> The tables that hold the data
    Album.artist_id = Artist.id -> How the tables linked
    
    Below is the sql that uses data from all tables

    SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.id AND Track.album_id = Album.id 
    AND Album.artist_id = Artist.id
'''