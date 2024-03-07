---
author:
- Harry Percival
- Bob Gregory
date: April 5, 2022
categories: book
tags:
- organizing
- mlops
- clearml
- improve
- reference
title: Practical Mlops
links:
- https://www.cosmicpython.com/book/preface.html
- https://github.com/cosmicpython/code/branches/all
- https://plantuml.com/
---

# Preface
+ *Test-driven development* (TDD) helps us to build code that is correct and enables us to refactor or add new features, without fear of regression. But it can be hard to get the best out of our tests: How do we make sure that they run as fast as possible? That we get as much coverage and feedback from fast, dependency-free unit tests and have the minimum number of slower, flaky end-to-end tests?
+ *Domain-driven design* (DDD) asks us to focus our efforts on building a good model of the business domain, but how do we make sure that our models aren’t encumbered with infrastructure concerns and don’t become hard to change?
+ Loosely coupled (micro)services integrated via messages (sometimes called *reactive microservices*) are a well-established answer to managing complexity across multiple applications or business domains. But it’s not always obvious how to make them fit with the established tools of the Python world—​Flask, Django, Celery, and so on.

# Introduction
Software tends towards chaos: big ball of yarn.

Solution: encapsulation and abstractions.

Encapsulation: simplifying behaviour and hiding data. More concerned with first.

Layering is also a way to clean up the chaos:

![Layered architecture](../attachments/2022-04-06-08-37-47.png)

## Dependency Inversion Principle

1. High-level modules should not depend on low-level modules. Both should depend on abstractions.
2. Abstractions should not depend on details. Instead, details should depend on abstractions.

*High-level modules* (business layer) are the code the organization really cares about. This is what organizes clients, trials, etc.

*Low-level modules* are the code the organization doesn't care about. No one gets excited for filesystems and network sockets.

Between them is another layer to then allow them both to be modified/updated independently.

Point of failure is the business layer typically since it erodes up and down the layers.

# Part 1: Building an Architecture to Support Domain Modeling
https://www.cosmicpython.com/book/part1.html

Behaviour should come first and drive storage requirements. Don't start with the database.

Customers care about what the system does.

Build persistence-ignorant code and create stable APIs around our domain so that we can refactor aggressively.

To do that, we present four key design patterns:

+ The Repository pattern, an abstraction over the idea of persistent storage
+ The Service Layer pattern to clearly define where our use cases begin and end
+ The Unit of Work pattern to provide atomic operations
+ The Aggregate pattern to enforce the integrity of our data

![Final App from Building an Architecture to Support Domain Modelling](../attachments/2022-04-06-08-47-49.png)

# 1: Domain Modeling
3-layer architecture == Domain Model

Domain == problem you're trying to solve

Model == map of a process that captures a useful property

In an OO way, set up the classes and assure the rules of the variables cannot be broken: value can't be negative, etc.


# 2: Repository Pattern
Repository pattern decouples the model layer from the data layer.

(Don't really get it)

The Repository pattern is an abstraction over permanent storage, for example.

# 3: A Brief Interlude: On Coupling and Abstractions
Abstract stuff away and don't repeat code.

# 4: Our First Use Case: Flask API and Service Layer
https://www.cosmicpython.com/book/chapter_04_service_layer.html