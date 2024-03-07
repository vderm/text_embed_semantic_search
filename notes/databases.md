---
author:
- Vasken Dermardiros
categories: note
draft: false
lastmod: 2020-07-30 07:34:20-04:00
slug: databases
tags:
- programming
- reference
title: Databases
---


## MongoDB

<https://www.mongodb.com/nosql-explained>

Video: [MongoDB in 5 Minutes with Eliot Horowitz](https://www.youtube.com/watch?v=EE8ZTQxa0AM)

Video: [MongoDB Crash Course](https://www.youtube.com/watch?v=-56x56UppqQ)

Database-as-a-Service for MongoDB: <https://mlab.com> (free 500 MB account)

## SQL: relational database {#sql-relational-database}

Preferred approach when trying to minimize data duplication since we have
foreign keys able to describe fully certain data.

Not very flexible since data types need to be defined from the beginning; made a
lot more sense in the past when a project was fully defined before it started.
Not very agile.

Now that we have an understanding of NoSQL databases, let’s contrast them with
what have traditionally been the most popular databases: relational databases
accessed by SQL (Structured Query Language). You can use SQL when interacting
with relational databases where data is stored in tables that have fixed columns
and rows.

Software engineer's job in 1970's: create an entity-relationship (E-R) diagram.

It's basically an Excel sheet on steroids which can go two ways: (1) add columns
for every new entry and you end up with a very sparse database, (2) break the
extra columns into new tables and you end up having to look through N number of
tables to get the information of 1 client. Not fun, but is more secure since you
can easily limit access to a sensitive table to a user or user group.

## NoSQL: non-relational database {#nosql-non-relational-database}

Because storage is very cheap now.

Document databases
: store data in documents similar to JSON (JavaScript
    Object Notation) objects. Each document contains pairs of fields and values.
    The values can typically be a variety of types including things like strings,
    numbers, booleans, arrays, or objects, and their structures typically align
    with objects developers are working with in code. Because of their variety of
    field value types and powerful query languages, document databases are great
    for a wide variety of use cases and can be used as a general purpose database.
    They can horizontally scale-out to accomodate large data volumes. **MongoDB** is
    consistently ranked as the world’s most popular NoSQL database according to
    DB-engines and is an example of a document database. For more on document
    databases, visit [What is a Document Database?](https://www.mongodb.com/document-databases).

Key-value databases
: are a simpler type of database where each item contains
    keys and values. A value can typically only be retrieved by referencing its
    key, so learning how to query for a specific key-value pair is typically
    simple. Key-value databases are great for use cases where you need to store
    large amounts of data but you don’t need to perform complex queries to
    retrieve it. Common use cases include storing user preferences or caching.
    **Redis** and DynanoDB are popular key-value databases.

Wide-column stores
: store data in tables, rows, and dynamic columns.
    Wide-column stores provide a lot of flexibility over relational databases
    because each row is not required to have the same columns. Many consider
    wide-column stores to be two-dimensional key-value databases. Wide-column
    stores are great for when you need to store large amounts of data and you can
    predict what your query patterns will be. Wide-column stores are commonly used
    for storing Internet of Things data and user profile data. Cassandra and HBase
    are two of the most popular wide-column stores.

Graph databases
: store data in nodes and edges. Nodes typically store
    information about people, places, and things while edges store information
    about the relationships between the nodes. Graph databases excel in use cases
    where you need to traverse relationships to look for patterns such as social
    networks, fraud detection, and recommendation engines. Neo4j and JanusGraph
    are examples of graph databases.

## mongoDB (NoSQL document database) {#mongodb--nosql-document-database}

- Document database (json-like syntax)
- Fault tolerance -> redundant copies made automatically
- Scalable -> easily separate databases based on number of users
- Data near users -> latency

Atlas is their platform and works on AWS, Azure and Google Cloud Platform

### Commands {#commands}

brew tap mongodb/brew
: install, Google for instructions

mongo
: go to mongo interface

show dbs
: show the databases

use <db>
: create a new database called <db>

db
: print out current selected database

show collections
:
