---
author:
- James Lewis
- Martin Fowler
categories: website
date: March 25, 2014
links: https://martinfowler.com/articles/microservices.html
tags:
- programming
- improve
title: Microservices
---

<!-- related backlinks: [[containerization]], [[python_microservices_with_grpc]] -->

![Monoliths and Microservices](../attachments/2021-11-09-09-07-53.png)

Frustration with monoliths: if a module has to be updated, the whole monolith has to be updated. It's also very hard to keep the modules within to be completely decoupled.

# Characteristics of a Microservice Architecture

Software built as plugging together components.

Our definition is that a component is a unit of software that is independently replaceable and upgradeable.

Microservice architectures will use libraries, but their primary way of componentizing their own software is by breaking down into services.

We define **libraries** as components that are linked into a program and called using in-memory function calls, while **services** are out-of-process components who communicate with a mechanism such as a web service request, or remote procedure call.

Having services makes it so that components can be replaced easily, but it makes the interface between components awkward and slow or crude.

# Organized around Business Capabilities

If management focuses on the technology layer, it leads to splitting teams as: UI, server-side logic and database teams. Which then leads to having logic code on all three layers.

![Conway's Law in Action](../attachments/2021-11-12-09-16-44.png)

Microservice approach to division is different. It's split about **business capability** which leads to teams being cross-functional.

![Service boundaries reinforced by team boundaries](../attachments/2021-11-12-09-17-07.png)

Teams are split around a product!

# Products not Projects

The developers of the products also run it and interact with the users. There's no simple hand-off.

*Waking up at 3AM every night by your pages is certainly a powerful incentive to focus on quality when writing your code.*

# Decentralized Governance

Use the best tool for the job. If a service is better written in C++, use C++.

Have the common tools around that solve common problems: data storage, inter-process communication, infrastructure automation, etc.

# Decentralized Data Management

Let each service have their own database.

![Application Databases](../attachments/2021-11-12-09-28-59.png)

# Infrastructure Automation

CI/CD pipelines have been greatly improved with the evolution of the cloud and AWS.

![Basic Build Pipeline](../attachments/2021-11-12-09-31-42.png)

# Design for Failure

Applications need to be designed so that they can tolerate the failure of services.

Netflix' Simian Army, now [Chaos Monkey](https://github.com/Netflix/chaosmonkey) (catastrophe testing) is used to test resilience of the architecture to many different types of failures.

Since services can fail at any time, it's important to be able to detect the failures quickly and, if possible, automatically restore service -> need real-time monitoring.

# Evolutionary Design

Microservice practitioners come from an evolutionary design background.

Whenever you try to break a software system into components, you're faced with the decision of how to divide up the pieces - what are the principles on which we decide to slice up our application? The key property of a component is the notion of independent replacement and upgradeability - which implies we look for points where we can imagine rewriting a component without affecting its collaborators. Indeed many microservice groups take this further by explicitly expecting many services to be scrapped rather than evolved in the longer term.

To test a monolith before prod, you need to test the whole thing. For a microservice, you can test just the service. Care must be taken to assure it doesn't break expected use. As a last resort, you can rely on versioning the services.

# Are Microservices the Future?

Looks like it.
